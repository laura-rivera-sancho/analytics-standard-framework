"""Reference analysis for the synthetic NovaPay A/B test.

This script demonstrates the standard workflow:
validation -> cleaning -> experiment health -> KPI summary -> inference -> segmentation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

REQUIRED_COLUMNS = {
    "customer_id",
    "experiment_group",
    "experiment_date",
    "country",
    "device_type",
    "customer_tenure",
    "transaction_value_usd",
    "checkout_completed",
    "checkout_time_seconds",
    "payment_declined",
    "support_contact",
    "fraud_flag",
}

VALID_GROUPS = {"Control", "Treatment"}
BINARY_COLUMNS = ["checkout_completed", "payment_declined", "support_contact", "fraud_flag"]


@dataclass
class ProportionTestResult:
    control_rate: float
    treatment_rate: float
    absolute_lift: float
    relative_lift: float
    z_stat: float
    p_value: float
    ci_low: float
    ci_high: float


def validate_schema(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def quality_report(df: pd.DataFrame) -> dict:
    validate_schema(df)
    report = {
        "rows": len(df),
        "duplicate_customer_ids": int(df["customer_id"].duplicated().sum()),
        "missing_experiment_group": int(df["experiment_group"].isna().sum()),
        "invalid_experiment_group": int(
            (~df["experiment_group"].isin(VALID_GROUPS) & df["experiment_group"].notna()).sum()
        ),
        "lowercase_country_values": int(df["country"].fillna("").str.islower().sum()),
    }
    for col in BINARY_COLUMNS:
        report[f"invalid_{col}"] = int((~df[col].isin([0, 1]) & df[col].notna()).sum())
    return report


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    validate_schema(df)
    out = df.copy()
    out["country"] = out["country"].str.upper()
    out = out[out["experiment_group"].isin(VALID_GROUPS)].copy()
    out = out.drop_duplicates(subset=["customer_id"], keep="first")
    out["experiment_date"] = pd.to_datetime(out["experiment_date"], errors="raise")
    return out


def sample_ratio_check(df: pd.DataFrame, expected_treatment_share: float = 0.50) -> dict:
    counts = df["experiment_group"].value_counts()
    control = int(counts.get("Control", 0))
    treatment = int(counts.get("Treatment", 0))
    total = control + treatment
    observed = np.array([control, treatment])
    expected = np.array([(1 - expected_treatment_share) * total, expected_treatment_share * total])
    chi2, p_value = stats.chisquare(observed, f_exp=expected)
    return {
        "control_n": control,
        "treatment_n": treatment,
        "treatment_share": treatment / total,
        "chi_square": float(chi2),
        "p_value": float(p_value),
    }


def two_proportion_test(df: pd.DataFrame, outcome: str) -> ProportionTestResult:
    control = df.loc[df["experiment_group"] == "Control", outcome]
    treatment = df.loc[df["experiment_group"] == "Treatment", outcome]

    x1, n1 = int(control.sum()), len(control)
    x2, n2 = int(treatment.sum()), len(treatment)
    p1, p2 = x1 / n1, x2 / n2

    pooled = (x1 + x2) / (n1 + n2)
    se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se_pooled
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))

    se_unpooled = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    diff = p2 - p1
    ci_low = diff - 1.96 * se_unpooled
    ci_high = diff + 1.96 * se_unpooled
    relative = diff / p1 if p1 else float("nan")

    return ProportionTestResult(
        control_rate=p1,
        treatment_rate=p2,
        absolute_lift=diff,
        relative_lift=relative,
        z_stat=float(z),
        p_value=float(p_value),
        ci_low=float(ci_low),
        ci_high=float(ci_high),
    )


def continuous_metric_analysis(df: pd.DataFrame, metric: str) -> dict:
    control = df.loc[df["experiment_group"] == "Control", metric].dropna()
    treatment = df.loc[df["experiment_group"] == "Treatment", metric].dropna()

    welch = stats.ttest_ind(treatment, control, equal_var=False)
    mann_whitney = stats.mannwhitneyu(treatment, control, alternative="two-sided")

    return {
        "control_mean": float(control.mean()),
        "treatment_mean": float(treatment.mean()),
        "control_median": float(control.median()),
        "treatment_median": float(treatment.median()),
        "mean_difference": float(treatment.mean() - control.mean()),
        "welch_t_p_value": float(welch.pvalue),
        "mann_whitney_p_value": float(mann_whitney.pvalue),
        "control_skew": float(control.skew()),
        "treatment_skew": float(treatment.skew()),
    }


def kpi_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("experiment_group")
        .agg(
            customers=("customer_id", "nunique"),
            checkout_completion_rate=("checkout_completed", "mean"),
            avg_checkout_time_seconds=("checkout_time_seconds", "mean"),
            median_checkout_time_seconds=("checkout_time_seconds", "median"),
            payment_decline_rate=("payment_declined", "mean"),
            support_contact_rate=("support_contact", "mean"),
            fraud_rate=("fraud_flag", "mean"),
            avg_transaction_value_usd=("transaction_value_usd", "mean"),
            median_transaction_value_usd=("transaction_value_usd", "median"),
        )
        .round(4)
    )


def segment_completion(df: pd.DataFrame, segment: str) -> pd.DataFrame:
    pivot = (
        df.groupby([segment, "experiment_group"])["checkout_completed"]
        .agg(["mean", "count"])
        .reset_index()
    )
    rates = pivot.pivot(index=segment, columns="experiment_group", values="mean")
    counts = pivot.pivot(index=segment, columns="experiment_group", values="count")
    result = pd.DataFrame(
        {
            "control_rate": rates.get("Control"),
            "treatment_rate": rates.get("Treatment"),
            "absolute_lift": rates.get("Treatment") - rates.get("Control"),
            "control_n": counts.get("Control"),
            "treatment_n": counts.get("Treatment"),
        }
    )
    return result.sort_values("absolute_lift", ascending=False)


def main() -> None:
    module_root = Path(__file__).resolve().parents[1]
    input_path = module_root / "data" / "raw" / "novapay_checkout_experiment_full.csv"

    if not input_path.exists():
        raise FileNotFoundError(
            "Generate the synthetic data first with: python src/generate_synthetic_data.py"
        )

    raw = pd.read_csv(input_path)
    print("\nRAW DATA QUALITY")
    print(quality_report(raw))

    df = clean_data(raw)
    print(f"\nFinal analytical population: {len(df):,} rows")

    print("\nSAMPLE RATIO CHECK")
    print(sample_ratio_check(df))

    print("\nKPI SUMMARY")
    print(kpi_summary(df))

    print("\nPRIMARY KPI: CHECKOUT COMPLETION")
    print(two_proportion_test(df, "checkout_completed"))

    print("\nGUARDRAILS")
    for outcome in ["payment_declined", "support_contact", "fraud_flag"]:
        print(outcome, two_proportion_test(df, outcome))

    print("\nCHECKOUT TIME")
    print(continuous_metric_analysis(df, "checkout_time_seconds"))

    print("\nDEVICE SEGMENT")
    print(segment_completion(df, "device_type"))

    print("\nCOUNTRY SEGMENT")
    print(segment_completion(df, "country"))

    print("\nCUSTOMER TENURE SEGMENT")
    print(segment_completion(df, "customer_tenure"))


if __name__ == "__main__":
    main()
