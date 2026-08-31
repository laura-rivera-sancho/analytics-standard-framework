# Marketing Experimentation Suite

> **Status: In progress.** This module extends the Harbor & Pine customer-value case into a governed retention experimentation program covering a simple split test and a full-factorial multivariate test.

## Business question

Harbor & Pine needs to determine which retention message, offer, and channel plan increases completed purchases and contribution margin among disengaging customers without creating unacceptable unsubscribe, opt-out, refund, or contact-pressure risk.

The suite separates two learning goals:

1. a two-arm split test establishes the basic randomized-analysis workflow and tests whether lifecycle-informed messaging improves outcomes over the current reminder
2. a `2 × 2 × 2` factorial experiment estimates message, offer, and channel-plan effects, prespecified interactions, and performance relative to a no-contact holdout

## What this module will demonstrate

- a decision-first experiment charter with explicit estimands
- eligibility, consent, exclusion, and randomization-unit governance
- power and minimum detectable effect planning
- sample-ratio mismatch and assignment-integrity checks
- intention-to-treat analysis with fixed outcome windows
- absolute and relative effect sizes with confidence intervals
- factorial main effects and prespecified interaction effects
- family-wise error and false-discovery controls
- primary, secondary, guardrail, and business-value metrics
- segment analysis that distinguishes prespecified heterogeneity from post-hoc exploration
- staged rollout guidance with monitoring and stop rules

## Navigate the current foundation

| Resource | Purpose |
|---|---|
| [Experimentation fundamentals](marketing_experimentation_fundamentals.md) | Core concepts, design tradeoffs, interview questions, and interpretation rules |
| [Business case](case_study/business_case.md) | Decision, population, test designs, metrics, governance, and acceptance criteria |
| [Portfolio roadmap](../ROADMAP.md) | A7 scope and relationship to the broader Data & AI portfolio |

Implementation assets—including the data dictionary, methodology, synthetic data, reusable analysis, guided notebook, tests, and stakeholder readout—will be added in the next A7 steps.

## Relationship to A6

The candidate audience begins with the At Risk and Needs Attention lifecycle groups defined in [A6 — Customer Value & Lifecycle Analytics](../06_customer_value_lifecycle/README.md). A6 describes observed customer behavior and prioritizes a controlled audience; A7 tests whether specific treatments cause incremental outcomes. The experiment does not treat RFM labels as response predictions.

## Decision boundary

This is a synthetic portfolio case, not a real campaign or proof that a particular discount strategy will generalize. No broad rollout is authorized from descriptive differences alone. Valid randomization, complete exposure logging, fixed measurement windows, multiplicity control, guardrail review, and a positive contribution-margin case are required before recommending scale.
