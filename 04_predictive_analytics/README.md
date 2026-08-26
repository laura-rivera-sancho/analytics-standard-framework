# Predictive Analytics Standard Framework

This module defines a repeatable process for building, validating, interpreting, and operationalizing predictive models for business decision support.

## How to use this module

The module follows the same portfolio structure as the experimentation sections:

1. **Fundamentals** — understand predictive modeling concepts, problem types, evaluation metrics, and common pitfalls.
2. **Methodology** — follow a standard end-to-end modeling lifecycle.
3. **Practice** — apply the framework using a synthetic business case.
4. **Stakeholder communication** — translate model performance into a business decision and deployment recommendation.

Start here:

- `predictive_analytics_fundamentals.md` for core concepts and terminology.
- `methodology.md` for the analytical and modeling execution standard.
- `case_study/business_case.md` for the fictional PayWave scenario.
- `case_study/data_dictionary.md` for the synthetic dataset definition.
- `case_study/expected_results.md` for the deterministic validation and held-out Test results.
- `notebooks/guided_predictive_analytics.ipynb` for the complete decision-focused modeling workflow.
- `notebooks/challenge_predictive_analytics.ipynb` for independent practice without worked solutions.
- `reports/stakeholder_readout.md` for the finished PayWave decision memo, executive preview, and downloadable PowerPoint readout.
- `src/generate_synthetic_data.py` to generate reproducible clean, raw, and compact PayWave datasets.
- `src/train_evaluate_models.py` for the reference temporal modeling and evaluation workflow.
- `templates/challenge_answer_key.md` for expected reasoning and interpretation.
- `templates/challenge_scoring_rubric.md` for a 100-point portfolio review standard.
- `templates/stakeholder_readout_template.md` for the executive presentation structure.
- `requirements.txt` for the Python environment.

## Standard lifecycle

1. Frame the business decision.
2. Define the prediction target and prediction horizon.
3. Define the scoring population and unit of analysis.
4. Confirm target availability and avoid leakage.
5. Define success metrics before modeling.
6. Validate data quality and temporal consistency.
7. Establish a simple baseline.
8. Split data using a strategy that matches the real deployment setting.
9. Engineer features using information available at prediction time.
10. Train candidate models.
11. Evaluate discrimination, calibration, and threshold performance.
12. Compare performance across important segments.
13. Interpret model drivers without confusing prediction with causation.
14. Translate scores into an operational decision policy.
15. Estimate business value, capacity requirements, and trade-offs.
16. Define monitoring, drift, retraining, and governance requirements.
17. Communicate the recommendation and limitations.

## Case study

The predictive case uses **PayWave**, a fictional digital-payments company that wants to predict which active customers are likely to become inactive within the next 30 days so the Retention team can prioritize outreach.

The model must identify high-risk customers early enough to act while avoiding leakage and accounting for class imbalance, probability calibration, limited outreach capacity, and segment-level performance.

The synthetic data include repeated customers across scoring cohorts, mild temporal drift, non-linear inactivity risk, missing feature values, deliberate leakage candidates, and a minority positive class.

All data and results in this module are synthetic and created solely for training and portfolio purposes.

## Running the reference workflow

From the `04_predictive_analytics` directory:

```bash
pip install -r requirements.txt
python src/generate_synthetic_data.py
python src/train_evaluate_models.py
```

The generator writes:

- `data/raw/paywave_inactivity_full.csv`
- `data/raw/paywave_inactivity_sample.csv`
- `data/processed/paywave_inactivity_clean_reference.csv`

The reference workflow then:

1. validates data quality and identifies leakage fields
2. cleans impossible values and standardizes categories
3. creates a chronological Train / Validation / Test split
4. compares a recency-based business rule with Logistic Regression, Random Forest, and Gradient Boosting
5. evaluates ROC AUC, PR AUC, Brier score, precision@5,000, recall@5,000, and lift@5,000
6. selects a candidate model on Validation rather than Test
7. evaluates the held-out Test cohort
8. checks segment-level model performance
9. estimates illustrative business value under explicit retention assumptions

To open the guided analysis:

```bash
jupyter notebook notebooks/guided_predictive_analytics.ipynb
```

To complete the independent challenge:

```bash
jupyter notebook notebooks/challenge_predictive_analytics.ipynb
```

## Reference decision snapshot

The deterministic held-out Test cohort contains 29,999 customers and an outreach capacity of 5,000.

| Metric | Gradient Boosting | Recency rule |
|---|---:|---:|
| PR AUC | 0.6943 | 0.6122 |
| Precision@5,000 | 77.06% | 66.02% |
| Recall@5,000 | 42.99% | 36.83% |
| Lift@5,000 | 2.58x | 2.21x |
| Inactive customers captured | 3,853 | 3,301 |

Within the same capacity, the selected model identifies 552 more future-inactive customers than the current rule. Under the documented illustrative assumptions, estimated net value is $46,450.90 per scoring cycle.

**Recommendation:** proceed to a controlled operational pilot, validate retention intervention lift separately, and monitor calibration, drift, segment outcomes, and realized value before wider deployment.

See the [full expected results](case_study/expected_results.md) for assumptions, segment performance, and limitations.

## Important principle

A predictive model is useful only when its output improves a real decision. High model accuracy alone is not the goal; the model must identify the right cases at the right time, with acceptable error trade-offs, stable behavior, and a clear operational action.
