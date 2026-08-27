from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

PRIOR_START = pd.Timestamp("2026-08-03")
PRIOR_END = pd.Timestamp("2026-08-09")
CURRENT_START = pd.Timestamp("2026-08-10")
CURRENT_END = pd.Timestamp("2026-08-16")
KEY = ["date", "country", "platform", "app_version", "payment_method", "acquisition_channel"]
FUNNEL = ["checkout_starts", "payment_attempts", "payment_approvals", "orders_completed"]


def quality_report(df):
    """Measure defects before any diagnostic conclusion is attempted."""
    return {
        "rows": len(df),
        "duplicate_grain": int(df.duplicated(KEY).sum()),
        "missing_channel": int(df["acquisition_channel"].isna().sum()),
        "invalid_country_casing": int(
            (df["country"].astype(str) != df["country"].astype(str).str.upper()).sum()
        ),
        "negative_checkout_starts": int(df["checkout_starts"].lt(0).sum()),
        "invalid_funnel_sequence": int(
            (
                df["payment_attempts"].gt(df["checkout_starts"])
                | df["payment_approvals"].gt(df["payment_attempts"])
                | df["orders_completed"].gt(df["payment_approvals"])
            ).sum()
        ),
    }


def clean_data(df):
    """Normalize dimensions, deduplicate the grain, and quarantine impossible funnels."""
    clean = df.copy()
    clean["date"] = pd.to_datetime(clean["date"])
    clean["country"] = clean["country"].astype(str).str.upper()
    clean["acquisition_channel"] = clean["acquisition_channel"].fillna("Unknown")
    clean = clean.drop_duplicates(KEY, keep="first")
    valid = clean[FUNNEL].ge(0).all(axis=1)
    valid &= clean["payment_attempts"].le(clean["checkout_starts"])
    valid &= clean["payment_approvals"].le(clean["payment_attempts"])
    valid &= clean["orders_completed"].le(clean["payment_approvals"])
    return clean.loc[valid].reset_index(drop=True)


def _period_filter(df, start, end):
    return df.loc[df["date"].between(pd.Timestamp(start), pd.Timestamp(end))]


def _aggregate_period(df, start, end):
    period = _period_filter(df, start, end)
    totals = period[[*FUNNEL, "revenue_usd", "checkout_support_contacts"]].sum()
    starts = totals["checkout_starts"]
    attempts = totals["payment_attempts"]
    approvals = totals["payment_approvals"]
    orders = totals["orders_completed"]
    return {
        "checkout_starts": int(starts),
        "payment_attempts": int(attempts),
        "payment_approvals": int(approvals),
        "orders_completed": int(orders),
        "checkout_completion_rate": orders / starts,
        "attempt_rate": attempts / starts,
        "approval_rate": approvals / attempts,
        "post_approval_completion_rate": orders / approvals,
        "revenue_usd": float(totals["revenue_usd"]),
        "support_contacts": int(totals["checkout_support_contacts"]),
        "average_order_value_usd": float(totals["revenue_usd"] / orders),
    }


def period_summary(df):
    """Compare the agreed current week with the immediately prior matched week."""
    prior = _aggregate_period(df, PRIOR_START, PRIOR_END)
    current = _aggregate_period(df, CURRENT_START, CURRENT_END)
    rows = []
    for metric in prior:
        rows.append(
            {
                "metric": metric,
                "prior": prior[metric],
                "current": current[metric],
                "absolute_change": current[metric] - prior[metric],
                "relative_change": current[metric] / prior[metric] - 1 if prior[metric] else np.nan,
            }
        )
    return pd.DataFrame(rows).set_index("metric")


def kpi_tree(df):
    """Show which multiplicative checkout-funnel rate moved most."""
    summary = period_summary(df)
    metrics = ["attempt_rate", "approval_rate", "post_approval_completion_rate"]
    return summary.loc[metrics, ["prior", "current", "absolute_change", "relative_change"]]


def _two_proportion_pvalue(success_current, total_current, success_prior, total_prior):
    pooled = (success_current + success_prior) / (total_current + total_prior)
    standard_error = np.sqrt(pooled * (1 - pooled) * (1 / total_current + 1 / total_prior))
    if standard_error == 0:
        return 1.0
    z_score = (success_current / total_current - success_prior / total_prior) / standard_error
    return float(2 * norm.sf(abs(z_score)))


def benjamini_hochberg(pvalues):
    """Return false-discovery-rate-adjusted q-values."""
    values = np.asarray(pvalues, dtype=float)
    order = np.argsort(values)
    ranked = values[order]
    adjusted = ranked * len(values) / np.arange(1, len(values) + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    result = np.empty_like(adjusted)
    result[order] = np.clip(adjusted, 0, 1)
    return result


def segment_diagnostics(df, dimension, min_starts=300):
    """Compare segment rates, separate within-segment and mix effects, and control FDR."""
    prior = _period_filter(df, PRIOR_START, PRIOR_END)
    current = _period_filter(df, CURRENT_START, CURRENT_END)
    prior_grouped = prior.groupby(dimension).agg(
        prior_starts=("checkout_starts", "sum"), prior_orders=("orders_completed", "sum")
    )
    current_grouped = current.groupby(dimension).agg(
        current_starts=("checkout_starts", "sum"), current_orders=("orders_completed", "sum")
    )
    result = prior_grouped.join(current_grouped, how="outer").fillna(0)
    result = result.loc[
        result["prior_starts"].ge(min_starts) & result["current_starts"].ge(min_starts)
    ].copy()
    result["prior_rate"] = result["prior_orders"] / result["prior_starts"]
    result["current_rate"] = result["current_orders"] / result["current_starts"]
    result["change_pp"] = 100 * (result["current_rate"] - result["prior_rate"])

    prior_total_rate = prior["orders_completed"].sum() / prior["checkout_starts"].sum()
    result["prior_weight"] = result["prior_starts"] / result["prior_starts"].sum()
    result["current_weight"] = result["current_starts"] / result["current_starts"].sum()
    result["within_effect_pp"] = (
        100 * result["current_weight"] * (result["current_rate"] - result["prior_rate"])
    )
    result["mix_effect_pp"] = (
        100
        * (result["current_weight"] - result["prior_weight"])
        * (result["prior_rate"] - prior_total_rate)
    )
    result["p_value"] = [
        _two_proportion_pvalue(
            row.current_orders, row.current_starts, row.prior_orders, row.prior_starts
        )
        for row in result.itertuples()
    ]
    result["q_value"] = benjamini_hochberg(result["p_value"])
    result["material_decline"] = result["change_pp"].le(-2.0) & result["q_value"].lt(0.05)
    return result.sort_values("within_effect_pp")


def impact_estimate(df):
    """Estimate current-week orders and revenue below the prior-week baseline."""
    summary = period_summary(df)
    prior_rate = summary.loc["checkout_completion_rate", "prior"]
    current_starts = summary.loc["checkout_starts", "current"]
    current_orders = summary.loc["orders_completed", "current"]
    prior_aov = summary.loc["average_order_value_usd", "prior"]
    expected_orders = current_starts * prior_rate
    lost_orders = max(0.0, expected_orders - current_orders)
    return {
        "expected_orders_at_prior_rate": float(expected_orders),
        "estimated_lost_orders": float(lost_orders),
        "estimated_revenue_gap_usd": float(lost_orders * prior_aov),
    }


def run_analysis(df):
    """Run the bounded reference diagnostic and return decision-ready evidence."""
    clean = clean_data(df)
    dimensions = ["country", "platform", "app_version", "payment_method", "acquisition_channel"]
    return {
        "quality": quality_report(df),
        "clean": clean,
        "period_summary": period_summary(clean),
        "kpi_tree": kpi_tree(clean),
        "segments": {dimension: segment_diagnostics(clean, dimension) for dimension in dimensions},
        "impact": impact_estimate(clean),
    }


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_path = module_root / "data" / "raw" / "orbitmart_checkout_diagnostic_full.csv"
    output_path = module_root / "data" / "processed" / "orbitmart_diagnostic_summary.csv"
    results = run_analysis(pd.read_csv(raw_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results["period_summary"].to_csv(output_path)
    print(results["period_summary"].to_string())
    print("\nKPI tree\n", results["kpi_tree"].to_string())
    print("\nImpact\n", results["impact"])
    print(f"Wrote diagnostic summary to {output_path}")


if __name__ == "__main__":
    main()
