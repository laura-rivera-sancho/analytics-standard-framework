# PayWave Predictive Analytics Challenge Answer Key

This answer key describes the expected analytical reasoning. Exact values should match the deterministic [reference results](../case_study/expected_results.md) when the supplied generator and workflow are used unchanged.

## 1. Business framing

The model supports a weekly ranked outreach list, not a generic classification decision at probability 0.50. The relevant unit is an eligible customer at a scoring date, the target is inactivity in the next 30 days, and the operational constraint is 5,000 contacts per scoring cycle.

## 2. Leakage and data quality

A strong solution explicitly excludes `transactions_next_30d`, `future_inactivity_status`, and `retention_case_opened_after_score`. These fields are unavailable at prediction time or reveal the outcome.

The solution should detect duplicates, casing defects, impossible negative values, missingness, and increasing target prevalence. Cleaning should preserve rows with valid analytical meaning while excluding impossible eligibility records.

## 3. Temporal validation

Random splitting is not appropriate for the primary evaluation because the production question is whether past cohorts generalize to future cohorts. Use January-May for Train, June-July for Validation, and August for the final held-out Test cohort.

All preprocessing must be fit on Train only. Validation selects the model and informs the operating policy; Test is evaluated once after decisions are frozen.

## 4. Baselines and model selection

Compare the candidate models with the recency business rule and Logistic Regression. Gradient Boosting has the highest Validation PR AUC, but only narrowly exceeds Logistic Regression. A strong recommendation acknowledges that this small gain may not justify additional operational complexity in every production setting.

The recency rule is an uncalibrated score. It supports ranking metrics but should not receive a probability-calibration score unless it is calibrated on separate data.

## 5. Held-out performance

Expected selected-model Test performance:

- ROC AUC: 0.8125
- PR AUC: 0.6943
- Brier: 0.1478
- precision@5,000: 77.06%
- recall@5,000: 42.99%
- lift@5,000: 2.58x
- future-inactive customers captured: 3,853

Within the same capacity, the rule captures 3,301. The model therefore identifies 552 additional future-inactive customers.

## 6. Segment interpretation

Performance is broadly consistent across markets and devices. Segment PR AUC should not be compared without considering prevalence. The lower prevalence of the High-value tier helps explain its lower PR AUC, while its Brier score remains favorable.

A strong answer does not claim fairness or production safety from these tables alone. It recommends continued segment monitoring and an investigation of business impact and contact experience.

## 7. Business value

Under the supplied assumptions, the model produces an illustrative net value of $46,450.90 per scoring cycle. This is not realized value because the 18% intervention-success assumption has not been experimentally validated.

Sensitivity analysis should vary success rate, retained value, and contact cost. The model predicts risk; it does not prove that outreach changes behavior.

## 8. Recommendation

Expected recommendation: proceed to a controlled operational pilot.

The pilot should validate intervention effectiveness, feature availability, calibration, workflow capacity, customer experience, and segment outcomes. Deployment monitoring should cover data quality, drift, prevalence, score distribution, calibration, top-k performance, and realized business outcomes.
