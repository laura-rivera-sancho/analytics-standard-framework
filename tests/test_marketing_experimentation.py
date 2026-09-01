from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = (
    ROOT / "07_marketing_experimentation/data/raw/harbor_pine_experiment_assignments_sample.csv"
)


def test_clean_generators_are_balanced_and_preserve_declared_grain(
    experimentation_generator,
):
    split = experimentation_generator.generate_split_test(per_arm=300)
    factorial = experimentation_generator.generate_factorial_test(per_cell=120)

    assert len(split) == 600
    assert split["assignment_id"].is_unique
    assert split.groupby("arm").size().nunique() == 1
    assert split["customer_id"].is_unique

    assert len(factorial) == 9 * 120
    assert factorial["assignment_id"].is_unique
    assert factorial.groupby("arm").size().nunique() == 1
    assert factorial["customer_id"].is_unique
    assert factorial.loc[factorial["is_holdout"], "exposed_at"].isna().all()
    assert factorial["email_consent"].all() and factorial["sms_consent"].all()


def test_validation_detects_documented_defects_and_reconciles(
    experimentation_generator, experimentation_validation
):
    raw = experimentation_generator.generate_raw_data()
    report = experimentation_validation.validation_report(raw)
    clean = experimentation_validation.clean_experiment_data(raw)

    assert report["duplicate_assignment"] == 20
    assert report["exposure_before_assignment"] >= 12
    assert report["conversion_before_assignment"] >= 10
    assert report["consent_violation"] >= 10
    assert report["missing_required_fields"] >= 10
    assert report["invalid_arm"] >= 8
    assert report["immature_window"] >= 8
    assert report["raw_rows"] == report["quarantined_rows"] + report["valid_rows"]
    assert len(clean) == report["valid_rows"]


def test_clean_population_keeps_assigned_non_deliveries(
    experimentation_generator, experimentation_validation
):
    raw = experimentation_generator.generate_raw_data()
    clean = experimentation_validation.clean_experiment_data(raw)

    assert clean["assignment_id"].is_unique
    assert not clean.duplicated(["experiment_id", "customer_id"]).any()
    assert clean["outcome_matured_at"].le(experimentation_generator.EXTRACT_AT).all()
    assert clean["email_consent"].all()
    factorial = clean["experiment_id"].eq(experimentation_generator.FACTORIAL_EXPERIMENT)
    assert clean.loc[factorial, "sms_consent"].all()
    assert clean.loc[clean["delivered_email"].eq(0) & ~clean["is_holdout"]].shape[0] > 0


def test_tracked_experiment_sample_is_compact_and_inspectable():
    sample = pd.read_csv(SAMPLE)

    assert len(sample) == 4_000
    assert {
        "assignment_id",
        "customer_id",
        "experiment_id",
        "arm",
        "message_framing",
        "offer",
        "channel_plan",
        "converted_14d",
        "recognized_revenue_14d",
        "unsubscribed_14d",
    }.issubset(sample.columns)
