from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "05_ad_hoc_analysis/data/raw/orbitmart_checkout_diagnostic_sample.csv"


def test_sample_quality_and_cleaning(adhoc_analysis):
    raw = pd.read_csv(SAMPLE)
    report = adhoc_analysis.quality_report(raw)
    clean = adhoc_analysis.clean_data(raw)

    assert len(raw) == 2_500
    assert report["missing_channel"] > 0
    assert not clean.duplicated(adhoc_analysis.KEY).any()
    assert clean[adhoc_analysis.FUNNEL].ge(0).all().all()
    assert clean["payment_attempts"].le(clean["checkout_starts"]).all()
    assert clean["payment_approvals"].le(clean["payment_attempts"]).all()
    assert clean["orders_completed"].le(clean["payment_approvals"]).all()


def test_period_summary_and_kpi_identity(adhoc_analysis, adhoc_generator):
    clean = adhoc_analysis.clean_data(adhoc_generator.generate_raw_data())
    summary = adhoc_analysis.period_summary(clean)
    tree = adhoc_analysis.kpi_tree(clean)

    prior_product = tree["prior"].prod()
    current_product = tree["current"].prod()
    assert np.isclose(prior_product, summary.loc["checkout_completion_rate", "prior"])
    assert np.isclose(current_product, summary.loc["checkout_completion_rate", "current"])
    assert summary.loc["checkout_completion_rate", "absolute_change"] < 0
    assert tree.loc["approval_rate", "absolute_change"] < 0


def test_segment_diagnostics_identify_localized_issue(adhoc_analysis, adhoc_generator):
    clean = adhoc_analysis.clean_data(adhoc_generator.generate_raw_data())
    version = adhoc_analysis.segment_diagnostics(clean, "app_version")
    payment = adhoc_analysis.segment_diagnostics(clean, "payment_method")

    assert version.index[0] == "android-8.4"
    assert version.loc["android-8.4", "material_decline"]
    assert payment.index[0] == "Digital wallet"
    assert payment.loc["Digital wallet", "change_pp"] < -2
    assert version["q_value"].between(0, 1).all()


def test_benjamini_hochberg_is_bounded_and_monotonic(adhoc_analysis):
    pvalues = np.array([0.04, 0.001, 0.02, 0.80])
    qvalues = adhoc_analysis.benjamini_hochberg(pvalues)
    order = np.argsort(pvalues)
    assert qvalues.min() >= 0 and qvalues.max() <= 1
    assert np.all(np.diff(qvalues[order]) >= 0)


def test_end_to_end_impact_is_decision_ready(adhoc_analysis, adhoc_generator):
    results = adhoc_analysis.run_analysis(adhoc_generator.generate_raw_data())

    assert results["impact"]["estimated_lost_orders"] > 0
    assert results["impact"]["estimated_revenue_gap_usd"] > 0
    assert set(results["segments"]) == {
        "country",
        "platform",
        "app_version",
        "payment_method",
        "acquisition_channel",
    }
