from pathlib import Path

import numpy as np
import pandas as pd

CAMPAIGN_CAPACITY = 6_000
EXPECTED_ADOPTION_RATE = {"High": 0.18, "Medium": 0.10, "Standard": 0.05}
MONTHLY_CONTRIBUTION_PER_ADOPTION = 40


def quality_report(df):
    """Return the validation checks required before eligibility is applied."""
    normalized_country = df["country"].astype(str).str.upper()
    return {
        "rows": len(df),
        "duplicate_merchant_id": int(df.duplicated("merchant_id").sum()),
        "missing_industry": int(df["industry"].isna().sum()),
        "invalid_country_casing": int((df["country"].astype(str) != normalized_country).sum()),
        "negative_volume": int((df["monthly_payment_volume_usd"] < 0).sum()),
        "invalid_tenure": int((df["tenure_months"] < 0).sum()),
    }


def clean_population(df):
    """Normalize fields, remove duplicates, and quarantine impossible values."""
    clean = df.copy()
    clean["country"] = clean["country"].astype(str).str.upper()
    clean["industry"] = clean["industry"].fillna("Unknown")
    clean = clean.drop_duplicates("merchant_id", keep="first")
    clean = clean.loc[
        clean["monthly_payment_volume_usd"].ge(0) & clean["tenure_months"].ge(0)
    ].copy()
    return clean.reset_index(drop=True)


def eligibility_masks(df):
    """Return ordered, auditable campaign eligibility rules."""
    return {
        "Active account": df["account_status"].eq("Active"),
        "Verified KYC": df["kyc_status"].eq("Verified"),
        "At least 3 months tenure": df["tenure_months"].ge(3),
        "Not already enabled": df["instant_settlement_enabled"].eq(0),
        "No contact in prior 30 days": df["contacted_last_30d"].eq(0),
        "Low or medium risk": df["risk_tier"].isin(["Low", "Medium"]),
        "At least $5k monthly volume": df["monthly_payment_volume_usd"].ge(5_000),
    }


def eligibility_funnel(df):
    """Apply rules sequentially and preserve a denominator-consistent audit trail."""
    remaining = pd.Series(True, index=df.index)
    rows = [{"stage": "Total merchant population", "remaining": int(remaining.sum())}]
    for label, mask in eligibility_masks(df).items():
        remaining &= mask
        rows.append({"stage": label, "remaining": int(remaining.sum())})
    funnel = pd.DataFrame(rows)
    funnel["excluded_at_stage"] = (
        funnel["remaining"].shift(1).sub(funnel["remaining"]).fillna(0).astype(int)
    )
    funnel["share_of_total"] = funnel["remaining"] / len(df)
    return funnel


def apply_eligibility(df):
    """Return merchants satisfying every eligibility rule."""
    masks = eligibility_masks(df)
    combined = np.logical_and.reduce([mask.to_numpy() for mask in masks.values()])
    return df.loc[combined].copy()


def score_population(eligible):
    """Assign transparent need, value, and fit points; this is not a propensity model."""
    scored = eligible.copy()
    scored["need_score"] = (
        2 * scored["avg_settlement_delay_hours"].ge(36).astype(int)
        + scored["support_contacts_90d"].ge(2).astype(int)
        + scored["payout_failure_rate_90d"].ge(0.02).astype(int)
    )
    scored["value_score"] = np.select(
        [
            scored["monthly_payment_volume_usd"].ge(50_000),
            scored["monthly_payment_volume_usd"].ge(20_000),
        ],
        [2, 1],
        default=0,
    )
    scored["fit_score"] = (
        scored["mobile_app_active"].eq(1).astype(int)
        + scored["profitability_tier"].isin(["Medium", "High"]).astype(int)
        + scored["risk_tier"].eq("Low").astype(int)
    )
    scored["priority_score"] = scored[["need_score", "value_score", "fit_score"]].sum(axis=1)
    scored["priority_tier"] = pd.cut(
        scored["priority_score"], bins=[-1, 3, 5, 9], labels=["Standard", "Medium", "High"]
    ).astype(str)
    return scored


def select_capacity(scored, capacity=CAMPAIGN_CAPACITY):
    """Select the top auditable priorities with deterministic tie-breaking."""
    ranked = scored.sort_values(
        ["priority_score", "monthly_payment_volume_usd", "merchant_id"],
        ascending=[False, False, True],
    ).copy()
    ranked["priority_rank"] = np.arange(1, len(ranked) + 1)
    ranked["selected"] = ranked["priority_rank"].le(min(capacity, len(ranked)))
    return ranked


def segment_summary(ranked, segment):
    """Profile eligible and selected populations without causal interpretation."""
    return (
        ranked.groupby(segment, dropna=False)
        .agg(
            eligible_merchants=("merchant_id", "size"),
            selected_merchants=("selected", "sum"),
            median_monthly_volume_usd=("monthly_payment_volume_usd", "median"),
            avg_priority_score=("priority_score", "mean"),
        )
        .assign(
            selection_rate=lambda frame: frame["selected_merchants"] / frame["eligible_merchants"]
        )
        .sort_values("selected_merchants", ascending=False)
    )


def estimate_opportunity(ranked):
    """Estimate planning value using explicit, editable assumptions."""
    selected = ranked.loc[ranked["selected"]].copy()
    selected["expected_adoption_rate"] = selected["priority_tier"].map(EXPECTED_ADOPTION_RATE)
    selected["expected_adopters"] = selected["expected_adoption_rate"]
    expected_adopters = selected["expected_adopters"].sum()
    return {
        "selected_merchants": len(selected),
        "expected_adopters": float(expected_adopters),
        "expected_adoption_rate": float(expected_adopters / len(selected))
        if len(selected)
        else 0.0,
        "annualized_contribution_usd": float(
            expected_adopters * MONTHLY_CONTRIBUTION_PER_ADOPTION * 12
        ),
    }


def capacity_sensitivity(scored, capacities=(3_000, 6_000, 9_000)):
    """Show how scale changes mix, expected response, and illustrative value."""
    rows = []
    for capacity in capacities:
        ranked = select_capacity(scored, capacity)
        opportunity = estimate_opportunity(ranked)
        selected = ranked.loc[ranked["selected"]]
        rows.append(
            {
                "capacity": capacity,
                **opportunity,
                "average_priority_score": selected["priority_score"].mean(),
                "high_priority_share": selected["priority_tier"].eq("High").mean(),
            }
        )
    return pd.DataFrame(rows)


def run_analysis(df, capacity=CAMPAIGN_CAPACITY):
    """Run the complete reference workflow and return activation-ready outputs."""
    clean = clean_population(df)
    funnel = eligibility_funnel(clean)
    eligible = apply_eligibility(clean)
    scored = score_population(eligible)
    ranked = select_capacity(scored, capacity)
    return {
        "quality": quality_report(df),
        "clean": clean,
        "funnel": funnel,
        "ranked": ranked,
        "country_summary": segment_summary(ranked, "country"),
        "industry_summary": segment_summary(ranked, "industry"),
        "opportunity": estimate_opportunity(ranked),
        "sensitivity": capacity_sensitivity(scored),
    }


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_path = module_root / "data" / "raw" / "lumina_settlement_target_full.csv"
    output_path = module_root / "data" / "processed" / "lumina_activation_target.csv"
    results = run_analysis(pd.read_csv(raw_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results["ranked"].loc[lambda frame: frame["selected"]].to_csv(output_path, index=False)
    print(results["funnel"].to_string(index=False))
    print(results["opportunity"])
    print(f"Wrote activation target to {output_path}")


if __name__ == "__main__":
    main()
