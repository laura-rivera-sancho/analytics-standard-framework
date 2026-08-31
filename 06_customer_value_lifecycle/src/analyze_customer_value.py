from pathlib import Path

import numpy as np
import pandas as pd

CURRENT_AS_OF = pd.Timestamp("2026-08-31")
PRIOR_AS_OF = pd.Timestamp("2026-05-31")
LOOKBACK_DAYS = 365
SEGMENT_VALUE = {
    "Hibernating": 1,
    "At Risk": 2,
    "Needs Attention": 3,
    "New or Potential": 3,
    "Loyal Customers": 4,
    "Champions": 5,
}


def quality_report(df, as_of_date=CURRENT_AS_OF):
    """Describe defects before calculating customer value."""
    order_dates = pd.to_datetime(df["order_timestamp"], errors="coerce")
    return {
        "rows": len(df),
        "duplicate_order_ids": int(df.duplicated("order_id").sum()),
        "missing_acquisition_channel": int(df["acquisition_channel"].isna().sum()),
        "nonpositive_revenue": int(
            pd.to_numeric(df["recognized_revenue"], errors="coerce").le(0).sum()
        ),
        "future_orders": int(order_dates.gt(pd.Timestamp(as_of_date)).sum()),
        "unparseable_order_dates": int(order_dates.isna().sum()),
    }


def clean_transactions(df, as_of_date=CURRENT_AS_OF):
    """Normalize customer attributes and quarantine invalid transactions."""
    clean = df.copy()
    clean["customer_created_at"] = pd.to_datetime(clean["customer_created_at"], errors="coerce")
    clean["order_timestamp"] = pd.to_datetime(clean["order_timestamp"], errors="coerce")
    clean["recognized_revenue"] = pd.to_numeric(clean["recognized_revenue"], errors="coerce")
    clean["acquisition_channel"] = clean["acquisition_channel"].fillna("unknown").str.lower()
    clean["country_code"] = clean["country_code"].astype(str).str.upper()
    clean = clean.drop_duplicates("order_id", keep="first")
    valid = clean["customer_id"].notna() & clean["order_id"].notna()
    valid &= clean["customer_created_at"].notna() & clean["order_timestamp"].notna()
    valid &= clean["order_timestamp"].le(pd.Timestamp(as_of_date))
    valid &= clean["order_timestamp"].ge(clean["customer_created_at"])
    valid &= clean["recognized_revenue"].gt(0)
    return clean.loc[valid].reset_index(drop=True)


def _score(series, higher_is_better=True):
    percentile = series.rank(method="average", pct=True)
    score = np.ceil(percentile * 5).clip(1, 5).astype(int)
    return score if higher_is_better else 6 - score


def _segment(row):
    r, f, m = row["recency_score"], row["frequency_score"], row["monetary_score"]
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    if r >= 3 and f >= 3:
        return "Loyal Customers"
    if r >= 4 and f <= 2:
        return "New or Potential"
    if r <= 2 and f >= 3:
        return "At Risk"
    if r <= 2 and f <= 2:
        return "Hibernating"
    return "Needs Attention"


def rfm_snapshot(df, as_of_date=CURRENT_AS_OF, lookback_days=LOOKBACK_DAYS):
    """Create a deterministic customer-level RFM snapshot at an explicit cutoff."""
    as_of_date = pd.Timestamp(as_of_date)
    eligible = df.loc[df["customer_created_at"].le(as_of_date)].copy()
    customer = (
        eligible.sort_values("order_timestamp")
        .groupby("customer_id", as_index=False)
        .agg(
            customer_created_at=("customer_created_at", "first"),
            acquisition_channel=("acquisition_channel", "first"),
            country_code=("country_code", "first"),
            marketing_consent=("marketing_consent", "first"),
        )
    )
    history = eligible.loc[eligible["order_timestamp"].le(as_of_date)]
    last_order = history.groupby("customer_id")["order_timestamp"].max()
    window_start = as_of_date - pd.Timedelta(days=lookback_days)
    window = history.loc[history["order_timestamp"].gt(window_start)]
    measures = window.groupby("customer_id").agg(
        frequency=("order_id", "nunique"), monetary_value=("recognized_revenue", "sum")
    )
    snapshot = customer.set_index("customer_id").join(last_order.rename("last_order_date"))
    snapshot = snapshot.join(measures).fillna({"frequency": 0, "monetary_value": 0})
    snapshot["recency_days"] = (as_of_date - snapshot["last_order_date"]).dt.days
    snapshot["recency_days"] = snapshot["recency_days"].fillna(lookback_days + 1).astype(int)
    snapshot["frequency"] = snapshot["frequency"].astype(int)
    snapshot["recency_score"] = _score(snapshot["recency_days"], higher_is_better=False)
    snapshot["frequency_score"] = _score(snapshot["frequency"])
    snapshot["monetary_score"] = _score(snapshot["monetary_value"])
    snapshot.loc[snapshot["frequency"].eq(0), ["frequency_score", "monetary_score"]] = 1
    snapshot["rfm_segment"] = snapshot.apply(_segment, axis=1)
    snapshot["as_of_date"] = as_of_date
    return snapshot.reset_index()


def segment_profiles(snapshot):
    """Summarize the size, value, behavior, and contactability of each RFM segment."""
    total_customers = len(snapshot)
    result = snapshot.groupby("rfm_segment").agg(
        customers=("customer_id", "nunique"),
        average_recency_days=("recency_days", "mean"),
        average_frequency=("frequency", "mean"),
        average_customer_value=("monetary_value", "mean"),
        total_customer_value=("monetary_value", "sum"),
        contactable_customers=("marketing_consent", "sum"),
    )
    result["customer_share"] = result["customers"] / total_customers
    result["value_share"] = result["total_customer_value"] / result["total_customer_value"].sum()
    return result.sort_values("total_customer_value", ascending=False)


def lifecycle_migration(prior_snapshot, current_snapshot):
    """Compare customer segments across two snapshots without treating movement as causal."""
    migration = prior_snapshot[["customer_id", "rfm_segment"]].merge(
        current_snapshot[["customer_id", "rfm_segment", "monetary_value"]],
        on="customer_id",
        how="outer",
        suffixes=("_prior", "_current"),
    )
    migration["rfm_segment_prior"] = migration["rfm_segment_prior"].fillna("New Customer")
    migration["rfm_segment_current"] = migration["rfm_segment_current"].fillna("Exited")
    prior_value = migration["rfm_segment_prior"].map(SEGMENT_VALUE).fillna(0)
    current_value = migration["rfm_segment_current"].map(SEGMENT_VALUE).fillna(0)
    migration["movement"] = np.select(
        [current_value > prior_value, current_value < prior_value],
        ["Improved", "Declined"],
        default="Stable",
    )
    return migration


def migration_summary(migration):
    return (
        migration.groupby("movement")
        .agg(customers=("customer_id", "nunique"), current_value=("monetary_value", "sum"))
        .sort_values("customers", ascending=False)
    )


def activation_plan(snapshot, capacity=500):
    """Prioritize consented retention audiences using transparent RFM evidence."""
    candidates = snapshot.loc[
        snapshot["marketing_consent"].astype(bool)
        & snapshot["rfm_segment"].isin(["At Risk", "Needs Attention"])
    ].copy()
    candidates["priority_score"] = (
        0.45 * candidates["monetary_score"]
        + 0.35 * candidates["frequency_score"]
        + 0.20 * (6 - candidates["recency_score"])
    )
    candidates = candidates.sort_values(
        ["priority_score", "monetary_value", "customer_id"],
        ascending=[False, False, True],
    )
    selected = candidates.head(capacity).copy()
    selected["recommended_action"] = np.where(
        selected["rfm_segment"].eq("At Risk"),
        "Retention offer with randomized holdout",
        "Re-engagement message with value reminder",
    )
    return selected


def run_analysis(df, capacity=500):
    clean = clean_transactions(df)
    prior = rfm_snapshot(clean, PRIOR_AS_OF)
    current = rfm_snapshot(clean, CURRENT_AS_OF)
    migration = lifecycle_migration(prior, current)
    return {
        "quality": quality_report(df),
        "clean": clean,
        "prior_snapshot": prior,
        "current_snapshot": current,
        "profiles": segment_profiles(current),
        "migration": migration,
        "migration_summary": migration_summary(migration),
        "activation": activation_plan(current, capacity),
    }


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_path = module_root / "data" / "raw" / "harbor_pine_orders_full.csv"
    processed = module_root / "data" / "processed"
    results = run_analysis(pd.read_csv(raw_path))
    processed.mkdir(parents=True, exist_ok=True)
    results["current_snapshot"].to_csv(processed / "customer_rfm_snapshot.csv", index=False)
    results["profiles"].to_csv(processed / "segment_profiles.csv")
    results["migration"].to_csv(processed / "lifecycle_migration.csv", index=False)
    results["activation"].to_csv(processed / "retention_activation_plan.csv", index=False)
    print(results["profiles"].round(3).to_string())
    print("\nLifecycle movement\n", results["migration_summary"].round(2).to_string())
    print(f"\nSelected {len(results['activation']):,} customers for controlled activation.")


if __name__ == "__main__":
    main()
