# PayWave Predictive Analytics Challenge Scoring Rubric

Use this 100-point rubric to review the challenge notebook.

| Area | Points | Full-credit standard |
|---|---:|---|
| Business framing | 10 | Defines the decision, target, eligible population, prediction horizon, unit, action, and 5,000-contact constraint. |
| Data quality and leakage | 15 | Detects deliberate defects, documents cleaning, identifies all leakage fields, and uses only information available at scoring. |
| Temporal validation | 10 | Uses the documented chronological split and explains why random splitting would weaken deployment realism. |
| Reproducible preprocessing | 10 | Fits imputation, encoding, and scaling on Train only through reusable pipelines. |
| Baselines and candidate models | 10 | Compares the business rule, Logistic Regression, Random Forest, and Gradient Boosting without assuming complexity is better. |
| Model evaluation | 15 | Correctly interprets ROC AUC, PR AUC, Brier/calibration, class prevalence, and the distinction between rankings and probabilities. |
| Capacity policy | 10 | Evaluates precision, recall, lift, and positives captured at 5,000 contacts per scoring cycle. |
| Segment and risk review | 8 | Reviews important segments with prevalence and sample size, avoids unsupported fairness claims, and identifies monitoring needs. |
| Business value | 7 | Uses transparent assumptions, performs or proposes sensitivity analysis, and separates expected from realized value. |
| Recommendation and communication | 5 | Gives a decision-focused recommendation with limitations, ownership, pilot requirements, and monitoring actions. |

## Performance bands

| Score | Interpretation |
|---|---|
| 90-100 | Portfolio-ready, decision-focused predictive analysis |
| 80-89 | Strong analysis with limited gaps |
| 70-79 | Technically credible but missing important decision or validation elements |
| 60-69 | Partial workflow; material analytical gaps remain |
| Below 60 | Requires substantial revision before stakeholder use |

## Automatic review concerns

Flag the work for revision if it:

- uses a deliberate leakage field
- selects a model using Test results
- relies on accuracy as the primary metric
- applies a default 0.50 threshold without operational justification
- reports the raw business-rule score as a calibrated probability
- claims causal retention impact from predictive performance alone
- omits limitations or segment monitoring
