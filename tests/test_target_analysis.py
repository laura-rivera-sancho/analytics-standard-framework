from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "03_target_analysis/data/raw/lumina_settlement_target_sample.csv"


def test_sample_quality_and_cleaning(target_analysis):
    raw = pd.read_csv(SAMPLE)
    report = target_analysis.quality_report(raw)
    clean = target_analysis.clean_population(raw)

    assert len(raw) == 2_500
    assert report["missing_industry"] > 0
    assert not clean["merchant_id"].duplicated().any()
    assert clean["monthly_payment_volume_usd"].ge(0).all()
    assert clean["tenure_months"].ge(0).all()
    assert clean["country"].str.fullmatch(r"[A-Z]{2}").all()


def test_eligibility_rules_and_funnel(target_analysis, target_generator):
    raw = target_generator.generate_raw_data(seed=314, n_merchants=2_000)
    clean = target_analysis.clean_population(raw)
    eligible = target_analysis.apply_eligibility(clean)
    funnel = target_analysis.eligibility_funnel(clean)

    assert eligible["account_status"].eq("Active").all()
    assert eligible["kyc_status"].eq("Verified").all()
    assert eligible["tenure_months"].ge(3).all()
    assert eligible["instant_settlement_enabled"].eq(0).all()
    assert eligible["contacted_last_30d"].eq(0).all()
    assert eligible["risk_tier"].isin(["Low", "Medium"]).all()
    assert eligible["monthly_payment_volume_usd"].ge(5_000).all()
    assert funnel["remaining"].is_monotonic_decreasing


def test_scoring_capacity_and_sensitivity(target_analysis, target_generator):
    raw = target_generator.generate_raw_data(seed=314, n_merchants=12_000)
    clean = target_analysis.clean_population(raw)
    scored = target_analysis.score_population(target_analysis.apply_eligibility(clean))
    ranked = target_analysis.select_capacity(scored, capacity=600)
    sensitivity = target_analysis.capacity_sensitivity(scored, capacities=(300, 600, 900))

    assert ranked["priority_score"].between(0, 9).all()
    assert ranked["selected"].sum() == 600
    assert (
        ranked.loc[ranked["selected"], "priority_score"].min()
        >= ranked.loc[~ranked["selected"], "priority_score"].max()
    )
    assert sensitivity["selected_merchants"].is_monotonic_increasing
    assert sensitivity["expected_adopters"].is_monotonic_increasing
    assert sensitivity["average_priority_score"].is_monotonic_decreasing


def test_small_end_to_end_workflow(target_analysis, target_generator):
    raw = target_generator.generate_raw_data(seed=314, n_merchants=5_000)
    results = target_analysis.run_analysis(raw, capacity=500)

    assert results["ranked"]["selected"].sum() == 500
    assert results["opportunity"]["selected_merchants"] == 500
    assert 0 < results["opportunity"]["expected_adoption_rate"] < 1
    assert set(results["country_summary"].index).issubset({"US", "MX", "BR", "CR"})
