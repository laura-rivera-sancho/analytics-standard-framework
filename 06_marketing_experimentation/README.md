# Marketing Experimentation Suite

> **Status: Complete.** This module extends the Harbor & Pine customer-value case into a governed retention experimentation program covering a simple split test and a full-factorial multivariate test.

**Portfolio shortcut:** [Finished stakeholder readout](reports/stakeholder_readout.md)

## Business question

Harbor & Pine needs to determine which retention message, offer, and channel plan increases completed purchases and contribution margin among disengaging customers without creating unacceptable unsubscribe, opt-out, refund, or contact-pressure risk.

The suite separates two learning goals:

1. a two-arm split test establishes the basic randomized-analysis workflow and tests whether lifecycle-informed messaging improves outcomes over the current reminder
2. a `2 × 2 × 2` factorial experiment estimates message, offer, and channel-plan effects, prespecified interactions, and performance relative to a no-contact holdout

## What this module demonstrates

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
| [Methodology](methodology.md) | Reusable experiment workflow from charter through rollout monitoring |
| [Data dictionary](case_study/data_dictionary.md) | Assignment grain, fields, factor catalog, outcomes, guardrails, and defect rules |
| [Expected results](case_study/expected_results.md) | Deterministic validity, split-test, factorial, margin, and decision narrative |
| [Guided notebook](notebooks/guided_marketing_experimentation.ipynb) | Worked validation, inference, multiplicity, economics, and recommendation |
| [Synthetic generator](src/generate_synthetic_data.py) | Deterministic split and factorial assignments with deliberate defects |
| [Validation gate](src/validate_experiment_data.py) | Executable consent, assignment, timestamp, maturity, and reconciliation controls |
| [Analytical engine](src/analyze_marketing_experiments.py) | Power, SRM, split effects, factorial contrasts, multiplicity, margin, and guardrails |
| [Stakeholder readout](reports/stakeholder_readout.md) | Executive recommendation, evidence, economics, guardrails, and controlled next stage |
| [Readout template](templates/stakeholder_readout_template.md) | Reusable experiment decision communication structure |
| [Portfolio roadmap](../ROADMAP.md) | A7 scope and relationship to the broader Data & AI portfolio |

The publication package includes the executive preview, Markdown stakeholder readout, and editable five-slide PowerPoint deck. The module passed its technical, analytical, communication, and portfolio review gates.

## Run the analysis

From the repository root:

```bash
python 06_marketing_experimentation/src/generate_synthetic_data.py
python 06_marketing_experimentation/src/validate_experiment_data.py
python 06_marketing_experimentation/src/analyze_marketing_experiments.py
pytest tests/test_marketing_experimentation.py
```

The full raw and processed datasets are reproducible from seed `707` and remain untracked. A compact 4,000-row raw sample is versioned for inspection.

## Relationship to A6

The candidate audience begins with the At Risk and Needs Attention lifecycle groups defined in [A6 — Customer Value & Lifecycle Analytics](../05_customer_value_lifecycle/README.md). A6 describes observed customer behavior and prioritizes a controlled audience; A7 tests whether specific treatments cause incremental outcomes. The experiment does not treat RFM labels as response predictions.

## Decision boundary

This is a synthetic portfolio case, not a real campaign or proof that a particular discount strategy will generalize. No broad rollout is authorized from descriptive differences alone. Valid randomization, complete exposure logging, fixed measurement windows, multiplicity control, guardrail review, and a positive contribution-margin case are required before recommending scale.
