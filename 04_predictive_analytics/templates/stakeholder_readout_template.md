# Predictive Analytics Stakeholder Readout Template

Use this structure for a concise decision-focused presentation. Keep model mechanics in an appendix unless they change the business decision.

## Slide 1 — Decision and recommendation

**Title:** Should we pilot model-ranked retention outreach?

Include:

- one-sentence recommendation
- target population and prediction horizon
- operating capacity
- expected incremental value versus the current approach
- confidence level and primary caveat

## Slide 2 — Business problem and action

Explain:

- the current targeting process
- the decision the prediction improves
- who acts on the score and when
- the cost of false positives and false negatives
- why a ranked list is more relevant than a 0.50 threshold

## Slide 3 — Data and validation design

Show:

- observation window and prediction horizon
- chronological Train, Validation, and Test periods
- analytical population and target prevalence
- leakage exclusions
- important data-quality decisions

Do not imply that a random split represents future deployment if the use case is temporal.

## Slide 4 — Model comparison

Compare the business rule, Logistic Regression, and candidate models using:

- PR AUC as the primary imbalanced-class ranking metric
- ROC AUC
- calibration/Brier where scores are probabilities
- precision and lift at operational capacity
- interpretability and deployment complexity

Call out when performance differences are too small to justify complexity.

## Slide 5 — Performance at outreach capacity

Lead with the actual policy:

- customers contacted
- expected inactive customers captured
- precision@capacity
- recall@capacity
- lift@capacity
- incremental captures versus the current rule

Include a gain or capacity curve when available.

## Slide 6 — Segment performance and risk

Review important markets, devices, tenure/value tiers, or other decision-relevant groups.

For every segment, consider:

- sample size and prevalence
- discrimination
- calibration
- selection rate and customer impact
- whether additional safeguards or monitoring are needed

## Slide 7 — Business-value sensitivity

State the formula and assumptions explicitly:

`captured inactive customers × intervention success rate × retained value − outreach cost`

Show conservative, base, and optimistic scenarios. Distinguish predicted value from experimentally validated impact.

## Slide 8 — Pilot and monitoring plan

Define:

- pilot population and duration
- randomized or phased measurement design
- success and guardrail metrics
- feature and scoring ownership
- data-quality and drift alerts
- retraining or rollback triggers
- decision date and accountable owner

## Executive communication rules

- Lead with the decision, not the algorithm.
- Separate ranking performance from probability calibration.
- Compare against the current business process.
- Express uncertainty and assumptions visibly.
- Never describe a predictor as a causal business lever without separate evidence.
- End with a specific action, owner, and validation plan.
