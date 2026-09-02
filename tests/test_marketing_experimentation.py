from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = (
    ROOT / "06_marketing_experimentation/data/raw/harbor_pine_experiment_assignments_sample.csv"
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


def test_power_plan_and_srm_are_decision_ready(experimentation_generator, experimentation_analysis):
    results = experimentation_analysis.run_analysis(experimentation_generator.generate_raw_data())

    assert results["power_plan"]["required_per_group"].gt(0).all()
    assert results["power_plan"]["detectable_effect_validated"].between(0, 0.05).all()
    assert results["srm"]["passes_at_0_01"].all()


def test_split_and_factorial_effects_include_uncertainty_and_multiplicity(
    experimentation_generator, experimentation_analysis
):
    results = experimentation_analysis.run_analysis(experimentation_generator.generate_raw_data())
    split = results["split_effects"].set_index("metric")
    factorial = results["factorial_effects"]
    cells = results["factorial_cells"]

    assert split.loc["converted_14d", "absolute_effect"] > 0
    assert split.loc["converted_14d", "ci_low"] < split.loc["converted_14d", "ci_high"]
    assert len(factorial) == 5
    assert factorial["adjusted_p_value"].between(0, 1).all()
    assert len(cells) == 8
    assert cells["adjusted_p_value"].between(0, 1).all()
    assert cells["incremental_margin_per_customer"].notna().all()


def test_recommendation_requires_effect_margin_and_guardrails(
    experimentation_generator, experimentation_analysis
):
    results = experimentation_analysis.run_analysis(experimentation_generator.generate_raw_data())
    recommended = results["recommended_cell"]
    candidate = results["factorial_cells"].set_index("arm").loc[recommended]
    guardrails = results["guardrails"]

    assert candidate["credible_after_holm"]
    assert candidate["positive_margin"]
    assert guardrails.loc[guardrails["arm"].eq(recommended), "passes"].all()


def test_reference_results_are_deterministic(experimentation_generator, experimentation_analysis):
    results = experimentation_analysis.run_analysis(experimentation_generator.generate_raw_data())
    split = results["split_effects"].set_index("metric")
    offer = results["factorial_effects"].set_index("effect").loc["offer: discount vs free shipping"]
    winner = results["factorial_cells"].iloc[0]

    assert len(results["clean"]) == 25_942
    assert abs(split.loc["converted_14d", "absolute_effect"] - 0.01440747) < 1e-7
    assert abs(offer["absolute_effect"] - 0.01365035) < 1e-7
    assert offer["credible_after_holm"]
    assert winner["arm"] == "urgency_led__discount_10__email_only"
    assert abs(winner["absolute_effect"] - 0.02665763) < 1e-7
    assert results["recommended_cell"] == winner["arm"]
