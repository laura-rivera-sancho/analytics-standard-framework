from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "04_predictive_analytics/data/raw/paywave_inactivity_sample.csv"


def test_sample_quality_leakage_and_cleaning(predictive_analysis):
    raw = pd.read_csv(SAMPLE)
    report = predictive_analysis.quality_report(raw)

    assert len(raw) == 2_500
    assert report["duplicate_customer_scoring_date"] == 30
    assert report["leakage_columns_present"] == 3

    clean = predictive_analysis.clean_data(raw)
    assert not clean.duplicated(["customer_id", "scoring_date"]).any()
    assert set(clean[predictive_analysis.TARGET].unique()).issubset({0, 1})
    assert clean["days_since_last_transaction"].ge(0).all()
    assert clean["transactions_30d"].ge(0).all()
    assert clean["customer_tenure_days"].ge(90).all()


def test_uncalibrated_rule_does_not_report_brier(predictive_analysis):
    raw = pd.read_csv(SAMPLE)
    clean = predictive_analysis.clean_data(raw)
    scores = predictive_analysis.business_rule_scores(clean)
    metrics = predictive_analysis.evaluate_predictions(
        clean[predictive_analysis.TARGET],
        scores,
        k=500,
        probability_scores=False,
    )

    assert np.isnan(metrics.brier)
    assert 0 <= metrics.precision_at_k <= 1
    assert metrics.k == 500


def test_small_end_to_end_model_workflow(monkeypatch, predictive_generator, predictive_analysis):
    monkeypatch.setattr(predictive_generator, "N_CUSTOMERS", 800)
    raw = predictive_generator.generate_raw_data(seed=126)
    clean = predictive_analysis.clean_data(raw)
    train, validation, test = predictive_analysis.temporal_split(clean)

    assert len(train) > len(test) > 0
    assert train["scoring_date"].max() < validation["scoring_date"].min()
    assert validation["scoring_date"].max() < test["scoring_date"].min()

    models = predictive_analysis.build_models(random_state=42)
    models["random_forest"].set_params(model__n_estimators=20, model__n_jobs=1)
    models["gradient_boosting"].set_params(model__max_iter=30)
    results = predictive_analysis.fit_and_score(models, train, validation, test)

    assert results["selected_name"] in models
    assert set(models).issubset(results["validation_table"].index)
    assert results["test_metrics"].k == len(test)
    assert 0 <= results["test_metrics"].pr_auc <= 1
    assert results["rule_test_metrics"].brier != results["rule_test_metrics"].brier
