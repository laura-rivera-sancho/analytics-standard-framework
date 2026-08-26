from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "02_pre_post_analysis/data/raw/finflow_verification_pre_post_sample.csv"


def test_sample_quality_and_cleaning(prepost_analysis):
    raw = pd.read_csv(SAMPLE)
    report = prepost_analysis.quality_report(raw)

    assert len(raw) == 1_000
    assert report["duplicate_transaction_ids"] == 30
    assert report["negative_duration_rows"] == 4
    assert report["implausibly_high_duration_rows"] == 6

    clean = prepost_analysis.clean_data(raw)
    assert clean["transaction_id"].is_unique
    assert clean["country"].str.fullmatch(r"[A-Z]{2}").all()
    assert clean["verification_time_seconds"].dropna().between(0, 3600).all()

    expected_post = (clean["transaction_date"] >= prepost_analysis.LAUNCH_DATE).astype(int)
    pd.testing.assert_series_equal(clean["post_flag"], expected_post, check_names=False)


def test_pre_post_statistics_are_well_formed(prepost_analysis):
    raw = pd.read_csv(SAMPLE)
    clean = prepost_analysis.clean_data(raw)

    primary = prepost_analysis.two_proportion_pre_post(clean, "verification_completed")
    assert 0 <= primary.pre_rate <= 1
    assert 0 <= primary.post_rate <= 1
    assert primary.ci_low <= primary.absolute_change <= primary.ci_high

    duration = prepost_analysis.continuous_pre_post(clean, "verification_time_seconds")
    assert duration["pre_n"] > 0
    assert duration["post_n"] > 0
    assert 0 <= duration["welch_t_p_value"] <= 1

    daily = prepost_analysis.daily_aggregate(clean)
    assert daily["transaction_date"].is_monotonic_increasing
    assert {"post", "ramp", "campaign", "dow"}.issubset(daily.columns)


def test_schema_validation_rejects_missing_fields(prepost_analysis):
    with pytest.raises(ValueError, match="Missing required columns"):
        prepost_analysis.validate_schema(pd.DataFrame({"transaction_id": ["T1"]}))
