from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "06_customer_value_lifecycle/data/raw/harbor_pine_orders_sample.csv"


def test_quality_controls_find_and_remove_deliberate_defects(
    lifecycle_generator, lifecycle_analysis
):
    raw = lifecycle_generator.generate_raw_data(customers=500)
    report = lifecycle_analysis.quality_report(raw)
    clean = lifecycle_analysis.clean_transactions(raw)

    assert report["duplicate_order_ids"] == 30
    assert report["missing_acquisition_channel"] >= 25
    assert report["nonpositive_revenue"] >= 15
    assert report["future_orders"] >= 12
    assert not clean.duplicated("order_id").any()
    assert clean["recognized_revenue"].gt(0).all()
    assert clean["order_timestamp"].le(lifecycle_analysis.CURRENT_AS_OF).all()


def test_rfm_snapshot_has_one_customer_per_cutoff_and_bounded_scores(
    lifecycle_generator, lifecycle_analysis
):
    clean = lifecycle_analysis.clean_transactions(
        lifecycle_generator.generate_raw_data(customers=700)
    )
    snapshot = lifecycle_analysis.rfm_snapshot(clean)

    assert len(snapshot) == snapshot["customer_id"].nunique()
    assert snapshot["as_of_date"].nunique() == 1
    assert snapshot["recency_score"].between(1, 5).all()
    assert snapshot["frequency_score"].between(1, 5).all()
    assert snapshot["monetary_score"].between(1, 5).all()
    assert snapshot["rfm_segment"].isin(lifecycle_analysis.SEGMENT_VALUE).all()


def test_segment_profiles_reconcile_and_identify_concentrated_value(
    lifecycle_generator, lifecycle_analysis
):
    clean = lifecycle_analysis.clean_transactions(
        lifecycle_generator.generate_raw_data(customers=1_000)
    )
    snapshot = lifecycle_analysis.rfm_snapshot(clean)
    profiles = lifecycle_analysis.segment_profiles(snapshot)

    assert profiles["customers"].sum() == len(snapshot)
    assert abs(profiles["customer_share"].sum() - 1) < 1e-10
    assert abs(profiles["value_share"].sum() - 1) < 1e-10
    assert profiles.loc["Champions", "value_share"] > profiles.loc["Champions", "customer_share"]


def test_lifecycle_migration_and_activation_are_decision_ready(
    lifecycle_generator, lifecycle_analysis
):
    results = lifecycle_analysis.run_analysis(
        lifecycle_generator.generate_raw_data(customers=1_200), capacity=200
    )
    migration = results["migration"]
    activation = results["activation"]

    assert len(migration) == results["current_snapshot"]["customer_id"].nunique()
    assert set(migration["movement"]) == {"Improved", "Declined", "Stable"}
    assert len(activation) == 200
    assert activation["marketing_consent"].all()
    assert set(activation["rfm_segment"]).issubset({"At Risk", "Needs Attention"})
    assert activation["priority_score"].is_monotonic_decreasing


def test_tracked_sample_is_compact_and_inspectable():
    sample = pd.read_csv(SAMPLE)

    assert len(sample) == 3_000
    assert {
        "customer_id",
        "customer_created_at",
        "marketing_consent",
        "order_id",
        "order_timestamp",
        "recognized_revenue",
    }.issubset(sample.columns)
