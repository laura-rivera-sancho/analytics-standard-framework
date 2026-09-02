from pathlib import Path

import pandas as pd
from generate_synthetic_data import (
    EXTRACT_AT,
    FACTORIAL_EXPERIMENT,
    SPLIT_EXPERIMENT,
    factorial_arm_catalog,
)

SPLIT_ARMS = {"control_current_reminder", "treatment_lifecycle_message"}
VALID_SEGMENTS = {"At Risk", "Needs Attention"}
VALID_VALUE_BANDS = {"High", "Medium", "Standard"}
TIMESTAMP_FIELDS = [
    "assigned_at",
    "extract_at",
    "outcome_matured_at",
    "exposed_at",
    "conversion_timestamp",
]


def normalize_experiment_data(df):
    """Normalize types without silently repairing experiment-integrity defects."""
    normalized = df.copy()
    for field in TIMESTAMP_FIELDS:
        normalized[field] = pd.to_datetime(normalized[field], errors="coerce", utc=True)
    for field in ["email_consent", "sms_consent", "is_holdout"]:
        if normalized[field].dtype == object:
            normalized[field] = normalized[field].map({"True": True, "False": False})
        normalized[field] = normalized[field].fillna(False).astype(bool)
    binary_fields = [
        "delivered_email",
        "delivered_sms",
        "converted_14d",
        "refunded_30d",
        "unsubscribed_14d",
        "complained_14d",
        "sms_opt_out_14d",
    ]
    for field in binary_fields:
        normalized[field] = pd.to_numeric(normalized[field], errors="coerce")
    return normalized


def invalid_row_masks(df, extract_at=EXTRACT_AT):
    """Return named row-level defects used by the publication gate."""
    data = normalize_experiment_data(df)
    factorial_arms = set(factorial_arm_catalog())
    valid_experiment = data["experiment_id"].isin([SPLIT_EXPERIMENT, FACTORIAL_EXPERIMENT])
    experiment_type_matches = (
        data["experiment_id"].eq(SPLIT_EXPERIMENT) & data["experiment_type"].eq("split_test")
    ) | (data["experiment_id"].eq(FACTORIAL_EXPERIMENT) & data["experiment_type"].eq("factorial"))
    valid_arm = (data["experiment_id"].eq(SPLIT_EXPERIMENT) & data["arm"].isin(SPLIT_ARMS)) | (
        data["experiment_id"].eq(FACTORIAL_EXPERIMENT) & data["arm"].isin(factorial_arms)
    )
    required_missing = data[["assignment_id", "customer_id", "assigned_at"]].isna().any(axis=1)
    required_missing |= ~data["lifecycle_segment"].isin(VALID_SEGMENTS)
    required_missing |= ~data["value_band"].isin(VALID_VALUE_BANDS)
    consent_violation = ~data["email_consent"]
    consent_violation |= data["experiment_id"].eq(FACTORIAL_EXPERIMENT) & ~data["sms_consent"]
    consent_violation |= data["channel_plan"].eq("email_plus_sms") & ~data["sms_consent"]
    exposure_before_assignment = data["exposed_at"].notna() & data["exposed_at"].lt(
        data["assigned_at"]
    )
    conversion_before_assignment = data["conversion_timestamp"].notna() & data[
        "conversion_timestamp"
    ].lt(data["assigned_at"])
    conversion_after_window = data["conversion_timestamp"].notna() & data[
        "conversion_timestamp"
    ].gt(data["outcome_matured_at"])
    conversion_inconsistent = data["converted_14d"].eq(1) & data["conversion_timestamp"].isna()
    conversion_inconsistent |= data["converted_14d"].eq(0) & data["conversion_timestamp"].notna()
    conversion_inconsistent |= data["converted_14d"].eq(0) & data["recognized_revenue_14d"].gt(0)
    immature_window = data["outcome_matured_at"].gt(pd.Timestamp(extract_at))
    duplicate_assignment = data.duplicated("assignment_id", keep="first")
    duplicate_customer = data.duplicated(["experiment_id", "customer_id"], keep="first")
    return {
        "duplicate_assignment": duplicate_assignment,
        "duplicate_customer_experiment": duplicate_customer,
        "invalid_experiment": ~valid_experiment | ~experiment_type_matches,
        "invalid_arm": ~valid_arm,
        "missing_required_fields": required_missing,
        "consent_violation": consent_violation,
        "exposure_before_assignment": exposure_before_assignment,
        "conversion_before_assignment": conversion_before_assignment,
        "conversion_after_window": conversion_after_window,
        "conversion_inconsistent": conversion_inconsistent,
        "immature_window": immature_window,
    }


def validation_report(df, extract_at=EXTRACT_AT):
    """Summarize raw quality and the reconciled quarantine population."""
    masks = invalid_row_masks(df, extract_at)
    any_invalid = pd.concat(masks, axis=1).any(axis=1)
    report = {name: int(mask.sum()) for name, mask in masks.items()}
    report.update(
        {
            "raw_rows": len(df),
            "quarantined_rows": int(any_invalid.sum()),
            "valid_rows": int((~any_invalid).sum()),
        }
    )
    return report


def clean_experiment_data(df, extract_at=EXTRACT_AT):
    """Quarantine critical defects while preserving valid assigned non-deliveries."""
    normalized = normalize_experiment_data(df)
    masks = invalid_row_masks(normalized, extract_at)
    any_invalid = pd.concat(masks, axis=1).any(axis=1)
    return normalized.loc[~any_invalid].reset_index(drop=True)


def assignment_counts(df):
    """Return assigned counts and planned shares for downstream SRM analysis."""
    return (
        df.groupby(["experiment_id", "arm"], as_index=False)
        .agg(
            assigned_customers=("customer_id", "nunique"),
            planned_allocation=("planned_allocation", "first"),
        )
        .sort_values(["experiment_id", "arm"])
    )


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_path = module_root / "data" / "raw" / "harbor_pine_experiment_assignments_full.csv"
    processed_root = module_root / "data" / "processed"
    raw = pd.read_csv(raw_path)
    clean = clean_experiment_data(raw)
    processed_root.mkdir(parents=True, exist_ok=True)
    clean.to_csv(processed_root / "validated_experiment_assignments.csv", index=False)
    assignment_counts(clean).to_csv(processed_root / "assignment_counts.csv", index=False)
    print(pd.Series(validation_report(raw)).to_string())
    print(f"\nPublished {len(clean):,} validated assignments.")


if __name__ == "__main__":
    main()
