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
- `src/generate_synthetic_data.py` to generate reproducible clean, raw, and compact PayWave datasets.
- `src/train_evaluate_models.py` for the reference temporal modeling and evaluation workflow.
- `requirements.txt` for the Python environment.

Guided/challenge notebooks, evaluation artifacts, and a stakeholder readout template will be added next.

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

## Important principle

A predictive model is useful only when its output improves a real decision. High model accuracy alone is not the goal; the model must identify the right cases at the right time, with acceptable error trade-offs, stable behavior, and a clear operational action.
