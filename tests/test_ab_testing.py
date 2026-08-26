from __future__ import annotations

import pandas as pd
import pytest


def test_generator_is_deterministic(ab_generator):
    first = ab_generator.generate_clean_data(n=500, seed=42)
    second = ab_generator.generate_clean_data(n=500, seed=42)
    pd.testing.assert_frame_equal(first, second)


def test_quality_cleaning_and_inference(ab_generator, ab_analysis):
    raw = ab_generator.generate_raw_data(n=2_000, seed=42)
    report = ab_analysis.quality_report(raw)

    assert report["duplicate_customer_ids"] == 24
    assert report["missing_experiment_group"] == 12
    assert report["lowercase_country_values"] == 18

    clean = ab_analysis.clean_data(raw)
    assert clean["customer_id"].is_unique
    assert set(clean["experiment_group"]) == {"Control", "Treatment"}
    assert clean["country"].str.fullmatch(r"[A-Z]{2}").all()

    ratio = ab_analysis.sample_ratio_check(clean)
    assert ratio["control_n"] + ratio["treatment_n"] == len(clean)
    assert 0 <= ratio["p_value"] <= 1

    result = ab_analysis.two_proportion_test(clean, "checkout_completed")
    assert 0 <= result.control_rate <= 1
    assert 0 <= result.treatment_rate <= 1
    assert result.ci_low <= result.absolute_lift <= result.ci_high


def test_schema_validation_rejects_missing_fields(ab_analysis):
    with pytest.raises(ValueError, match="Missing required columns"):
        ab_analysis.validate_schema(pd.DataFrame({"customer_id": ["C1"]}))
