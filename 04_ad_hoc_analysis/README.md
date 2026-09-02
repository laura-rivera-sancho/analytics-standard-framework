# Ad Hoc Analysis Standard Framework

> **Status: Complete.** This module turns an ambiguous, time-sensitive KPI question into a bounded, reproducible diagnostic and decision-ready response.

**Portfolio shortcut:** Review the [Finished stakeholder readout](reports/stakeholder_readout.md) for the diagnostic conclusion, evidence hierarchy, immediate action, and follow-up measurement plan.

## Business question

OrbitMart's checkout completion rate fell week over week even though checkout starts increased. Leadership needs to know whether the decline is real, where it occurs, what can be concluded today, and what action should happen next.

The reference analysis finds a **0.97 percentage-point decline**, localized primarily to **Android 8.4 digital-wallet traffic**. Payment approval is the only KPI-tree stage with a material movement. At the prior-week completion rate, the current week would have produced about **254 additional orders** and **$15.5K more revenue**.

## What this module demonstrates

- structured intake, decision deadlines, and a documented stopping rule
- stable KPI definitions, denominators, comparison periods, and materiality thresholds
- data validation before exploratory slicing
- KPI-tree diagnosis and rate-versus-mix decomposition
- pre-specified drill-down dimensions, minimum sample sizes, and false-discovery-rate control
- separation of observed facts, supported hypotheses, and unresolved causal questions
- concise recommendations, operational escalation, and follow-up measurement
- reproducible synthetic data, code, tests, notebooks, and executive communication

## Navigate the module

| Resource | Purpose |
|---|---|
| [Ad hoc analysis fundamentals](ad_hoc_analysis_fundamentals.md) | Core concepts, guardrails, failure modes, and stopping rules |
| [Methodology](methodology.md) | Reusable intake-to-handoff workflow and quality gates |
| [Business case](case_study/business_case.md) | OrbitMart decision, timeline, hypotheses, and constraints |
| [Data dictionary](case_study/data_dictionary.md) | Grain, metric fields, dimensions, and timing |
| [Expected results](case_study/expected_results.md) | Deterministic outputs and evidence interpretation |
| [Guided notebook](notebooks/guided_ad_hoc_analysis.ipynb) | Worked diagnostic from validation through recommendation |
| [Challenge notebook](notebooks/challenge_ad_hoc_analysis.ipynb) | Independent time-bounded diagnostic practice |
| [Reference diagnostic](src/diagnose_kpi_change.py) | Reusable KPI tree, decomposition, inference, and impact functions |
| [Synthetic generator](src/generate_synthetic_data.py) | Deterministic checkout data with deliberate quality defects |
| [Stakeholder readout](reports/stakeholder_readout.md) | Finished analytical memo and executive artifacts |

## Analytical lifecycle

1. Clarify the decision, audience, deadline, and action options.
2. Write the primary question, KPI contract, comparison period, and materiality threshold.
3. Define a KPI tree and bounded hypothesis map before exploring.
4. Validate freshness, uniqueness, completeness, categories, and funnel logic.
5. Confirm the headline movement on a matched comparison period.
6. Diagnose the KPI tree to locate the failing stage.
7. Drill only into pre-specified dimensions, with sample-size and multiplicity controls.
8. Decompose within-segment performance from traffic-mix effects.
9. Estimate business impact and triangulate against operational signals.
10. Separate facts, supported hypotheses, and speculation.
11. Recommend an action, owner, rollback or mitigation, and follow-up measurement.
12. Stop when the decision is supported or the agreed timebox expires; document unresolved questions.

## Run locally

From the repository root:

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements-dev.txt
python 04_ad_hoc_analysis/src/generate_synthetic_data.py
python 04_ad_hoc_analysis/src/diagnose_kpi_change.py
pytest tests/test_ad_hoc_analysis.py
```

On macOS or Linux, activate with `source .venv/bin/activate`.

The generator writes a full local dataset and a compact tracked sample. The full dataset and processed summary are ignored and can be reproduced from seed 505.

## Interpretation boundary

The analysis shows where the decline is concentrated and which funnel rate moved. It does not prove whether the Android release, wallet processor, or their interaction caused the issue. Operational logs, incident records, and a controlled rollback or routing change are required for causal confirmation.

## Portfolio connection

Return to the [repository overview](../README.md) to compare experimentation, observational impact evaluation, target design, diagnostic analysis, customer strategy, and market intelligence workflows.
