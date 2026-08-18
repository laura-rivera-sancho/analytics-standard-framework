from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats

LAUNCH_DATE = pd.Timestamp("2026-04-01")
RAMP_END = LAUNCH_DATE + pd.Timedelta(days=6)
CAMPAIGN_START = pd.Timestamp("2026-05-04")
CAMPAIGN_END = pd.Timestamp("2026-05-10")
BINARY_COLUMNS = [
    "verification_completed",
    "manual_review",
    "payment_declined",
    "support_contact",
    "fraud_confirmed",
]
REQUIRED_COLUMNS = {
    "transaction_id",
    "customer_id",
    "transaction_date",
    "country",
    "device_type",
    "customer_tenure",
    "risk_tier",
    "transaction_value_usd",
    "verification_completed",
    "verification_time_seconds",
    "manual_review",
    "payment_declined",
    "support_contact",
    "fraud_confirmed",
}


@dataclass
class RateComparison:
    pre_rate: float
    post_rate: float
    absolute_change: float
    relative_change: float
    z_stat: float
    p_value: float
    ci_low: float
    ci_high: float


def validate_schema(df):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def quality_report(df):
    validate_schema(df)
    date = pd.to_datetime(df["transaction_date"], errors="coerce")
    report = {
        "rows": len(df),
        "duplicate_transaction_ids": int(df.duplicated("transaction_id").sum()),
        "missing_transaction_date": int(date.isna().sum()),
        "missing_risk_tier": int(df["risk_tier"].isna().sum()),
        "missing_device_type": int(df["device_type"].isna().sum()),
        "missing_verification_time": int(df["verification_time_seconds"].isna().sum()),
        "lowercase_country_values": int(df["country"].astype(str).str.fullmatch(r"[a-z]{2}").sum()),
        "negative_duration_rows": int((pd.to_numeric(df["verification_time_seconds"], errors="coerce") < 0).sum()),
        "implausibly_high_duration_rows": int((pd.to_numeric(df["verification_time_seconds"], errors="coerce") > 3600).sum()),
    }
    for col in BINARY_COLUMNS:
        report[f"invalid_binary_{col}"] = int((~df[col].isin([0, 1]) & df[col].notna()).sum())
    return report


def clean_data(df):
    validate_schema(df)
    out = df.copy()
    out["transaction_date"] = pd.to_datetime(out["transaction_date"], errors="coerce")
    out = out.dropna(subset=["transaction_date", "transaction_id"]).copy()
    out["country"] = out["country"].astype(str).str.upper()
    out = out.drop_duplicates("transaction_id", keep="first")

    # Re-derive all intervention timing fields from the transaction date.
    out["period"] = np.where(out["transaction_date"] < LAUNCH_DATE, "Pre", "Post")
    out["post_flag"] = (out["transaction_date"] >= LAUNCH_DATE).astype(int)
    out["days_from_launch"] = (out["transaction_date"] - LAUNCH_DATE).dt.days
    out["ramp_flag"] = ((out["transaction_date"] >= LAUNCH_DATE) & (out["transaction_date"] <= RAMP_END)).astype(int)
    out["campaign_flag"] = ((out["transaction_date"] >= CAMPAIGN_START) & (out["transaction_date"] <= CAMPAIGN_END)).astype(int)

    # Exclude impossible duration values from duration analysis while keeping rows for rate KPIs.
    duration = pd.to_numeric(out["verification_time_seconds"], errors="coerce")
    out["verification_time_seconds"] = duration.mask((duration < 0) | (duration > 3600))
    return out.reset_index(drop=True)


def kpi_summary(df):
    return (
        df.groupby("period")
        .agg(
            transactions=("transaction_id", "nunique"),
            verification_completion_rate=("verification_completed", "mean"),
            avg_verification_time_seconds=("verification_time_seconds", "mean"),
            median_verification_time_seconds=("verification_time_seconds", "median"),
            manual_review_rate=("manual_review", "mean"),
            payment_decline_rate=("payment_declined", "mean"),
            support_contact_rate=("support_contact", "mean"),
            fraud_confirmed_rate=("fraud_confirmed", "mean"),
            avg_transaction_value_usd=("transaction_value_usd", "mean"),
        )
        .sort_index()
    )


def two_proportion_pre_post(df, metric, post_mask=None):
    if post_mask is None:
        post_mask = df["period"].eq("Post")
    pre = df.loc[df["period"].eq("Pre"), metric].dropna().astype(float)
    post = df.loc[post_mask, metric].dropna().astype(float)

    x1, n1 = pre.sum(), len(pre)
    x2, n2 = post.sum(), len(post)
    p1, p2 = x1 / n1, x2 / n2
    pooled = (x1 + x2) / (n1 + n2)
    se_pooled = np.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se_pooled if se_pooled else np.nan
    p_value = 2 * stats.norm.sf(abs(z)) if np.isfinite(z) else np.nan

    se_unpooled = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    diff = p2 - p1
    ci_low = diff - 1.96 * se_unpooled
    ci_high = diff + 1.96 * se_unpooled
    rel = diff / p1 if p1 else np.nan
    return RateComparison(p1, p2, diff, rel, z, p_value, ci_low, ci_high)


def continuous_pre_post(df, metric, post_mask=None):
    if post_mask is None:
        post_mask = df["period"].eq("Post")
    pre = df.loc[df["period"].eq("Pre"), metric].dropna().astype(float)
    post = df.loc[post_mask, metric].dropna().astype(float)
    welch = stats.ttest_ind(post, pre, equal_var=False)
    mann = stats.mannwhitneyu(post, pre, alternative="two-sided")
    return {
        "pre_n": len(pre),
        "post_n": len(post),
        "pre_mean": pre.mean(),
        "post_mean": post.mean(),
        "mean_change": post.mean() - pre.mean(),
        "pre_median": pre.median(),
        "post_median": post.median(),
        "median_change": post.median() - pre.median(),
        "pre_skew": pre.skew(),
        "post_skew": post.skew(),
        "welch_t_p_value": float(welch.pvalue),
        "mann_whitney_p_value": float(mann.pvalue),
    }


def daily_aggregate(df):
    daily = (
        df.groupby("transaction_date")
        .agg(
            transactions=("transaction_id", "nunique"),
            verification_completion_rate=("verification_completed", "mean"),
            avg_verification_time_seconds=("verification_time_seconds", "mean"),
            median_verification_time_seconds=("verification_time_seconds", "median"),
            manual_review_rate=("manual_review", "mean"),
            payment_decline_rate=("payment_declined", "mean"),
            support_contact_rate=("support_contact", "mean"),
            fraud_confirmed_rate=("fraud_confirmed", "mean"),
            new_customer_share=("customer_tenure", lambda x: (x == "New").mean()),
            mobile_share=("device_type", lambda x: (x == "Mobile").mean()),
            high_risk_share=("risk_tier", lambda x: (x == "High").mean()),
        )
        .reset_index()
        .sort_values("transaction_date")
    )
    daily["time_index"] = np.arange(len(daily))
    daily["post"] = (daily["transaction_date"] >= LAUNCH_DATE).astype(int)
    launch_index = int(daily.loc[daily["transaction_date"].eq(LAUNCH_DATE), "time_index"].iloc[0])
    daily["time_after_launch"] = np.where(daily["post"].eq(1), daily["time_index"] - launch_index, 0)
    daily["ramp"] = ((daily["transaction_date"] >= LAUNCH_DATE) & (daily["transaction_date"] <= RAMP_END)).astype(int)
    daily["campaign"] = ((daily["transaction_date"] >= CAMPAIGN_START) & (daily["transaction_date"] <= CAMPAIGN_END)).astype(int)
    daily["dow"] = daily["transaction_date"].dt.day_name().str[:3]
    return daily


def interrupted_time_series(df, metric="verification_completion_rate", adjusted=True):
    daily = daily_aggregate(df)
    if adjusted:
        formula = (
            f"{metric} ~ time_index + post + time_after_launch + ramp + campaign "
            "+ new_customer_share + mobile_share + high_risk_share + C(dow)"
        )
    else:
        formula = f"{metric} ~ time_index + post + time_after_launch"

    # Weight by daily transaction count so higher-volume days contribute more information.
    model = smf.wls(formula=formula, data=daily, weights=daily["transactions"]).fit(cov_type="HC3")
    return model, daily


def mix_comparison(df, column):
    table = pd.crosstab(df[column], df["period"], normalize="columns") * 100
    return table.round(2)


def segment_completion(df, segment):
    grouped = df.groupby([segment, "period"])["verification_completed"].agg(["mean", "count"]).reset_index()
    rates = grouped.pivot(index=segment, columns="period", values="mean")
    counts = grouped.pivot(index=segment, columns="period", values="count")
    out = pd.DataFrame(index=rates.index)
    out["pre_rate"] = rates.get("Pre")
    out["post_rate"] = rates.get("Post")
    out["absolute_change_pp"] = (out["post_rate"] - out["pre_rate"]) * 100
    out["pre_n"] = counts.get("Pre")
    out["post_n"] = counts.get("Post")
    return out.sort_values("absolute_change_pp", ascending=False)


def stable_post_mask(df):
    return df["transaction_date"] > RAMP_END


def main():
    module_root = Path(__file__).resolve().parents[1]
    path = module_root / "data" / "raw" / "finflow_verification_pre_post_full.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} does not exist. Run src/generate_synthetic_data.py first."
        )

    raw = pd.read_csv(path)
    print("DATA QUALITY")
    print(pd.Series(quality_report(raw)))

    df = clean_data(raw)
    print(f"\nFinal analytical rows: {len(df):,}")
    print(f"Date range: {df.transaction_date.min().date()} to {df.transaction_date.max().date()}")

    print("\nKPI SUMMARY")
    print(kpi_summary(df).round(4))

    print("\nPRIMARY KPI — SIMPLE PRE/POST")
    primary = two_proportion_pre_post(df, "verification_completed")
    print(pd.Series(primary.__dict__).round(6))

    print("\nPRIMARY KPI — STABLE POST (EXCLUDING 7-DAY RAMP)")
    primary_stable = two_proportion_pre_post(df, "verification_completed", stable_post_mask(df))
    print(pd.Series(primary_stable.__dict__).round(6))

    print("\nVERIFICATION TIME")
    print(pd.Series(continuous_pre_post(df, "verification_time_seconds")).round(4))

    print("\nGUARDRAILS")
    for metric in ["manual_review", "payment_declined", "support_contact", "fraud_confirmed"]:
        result = two_proportion_pre_post(df, metric)
        print(f"\n{metric}")
        print(pd.Series(result.__dict__).round(6))

    print("\nTRAFFIC MIX")
    for col in ["country", "device_type", "customer_tenure", "risk_tier"]:
        print(f"\n{col}")
        print(mix_comparison(df, col))

    print("\nINTERRUPTED TIME SERIES — ADJUSTED")
    model, _ = interrupted_time_series(df, adjusted=True)
    terms = ["time_index", "post", "time_after_launch", "ramp", "campaign"]
    print(model.summary2().tables[1].loc[terms].round(6))

    print("\nSEGMENT COMPLETION")
    for col in ["device_type", "country", "customer_tenure", "risk_tier"]:
        print(f"\n{col}")
        print(segment_completion(df, col).round(4))


if __name__ == "__main__":
    main()
