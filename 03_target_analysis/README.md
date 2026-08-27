# Target Analysis Standard Framework

> **Status: Complete.** This module defines, sizes, profiles, and prioritizes an activation-ready population using transparent business rules and explicit assumptions.

**Portfolio shortcut:** Review the [Finished stakeholder readout](reports/stakeholder_readout.md) for the recommendation, population funnel, capacity tradeoff, safeguards, and activation plan.

## Business decision

LuminaPay can contact 6,000 merchants about Instant Settlement. The decision is not who is most likely to adopt; it is which merchants are operationally eligible and should be prioritized using interpretable need, value, and fit criteria.

The reference result identifies **25,805 eligible merchants** from a clean population of 59,960 and recommends a first wave of **6,000**: every high-priority merchant plus the strongest medium-priority merchants. Under explicitly illustrative assumptions, the wave is expected to produce about **806 adopters** and **$386.8K annualized contribution**.

## What this module demonstrates

- decision framing, unit of analysis, as-of date, and ownership
- denominator-consistent eligibility funnel and exclusion audit
- target sizing and descriptive segment profiling
- transparent prioritization under a hard capacity constraint
- sensitivity analysis for scale, expected adoption, and value assumptions
- activation controls, suppression rules, monitoring, and measurement handoff
- reproducible synthetic data, analysis code, tests, and executive communication

## Navigate the module

| Resource | Purpose |
|---|---|
| [Target-analysis fundamentals](target_analysis_fundamentals.md) | Core concepts, boundaries, failure modes, and review questions |
| [Methodology](methodology.md) | Reusable end-to-end workflow and quality gates |
| [Business case](case_study/business_case.md) | LuminaPay decision, constraints, assumptions, and stakeholders |
| [Data dictionary](case_study/data_dictionary.md) | Field definitions, lineage, timing, and allowed uses |
| [Expected results](case_study/expected_results.md) | Deterministic reference outputs and interpretation |
| [Guided notebook](notebooks/guided_target_analysis.ipynb) | Worked analysis from validation through activation handoff |
| [Challenge notebook](notebooks/challenge_target_analysis.ipynb) | Independent practice with decision prompts and safeguards |
| [Reference analysis](src/analyze_targets.py) | Reusable eligibility, scoring, sizing, and sensitivity functions |
| [Synthetic generator](src/generate_synthetic_data.py) | Deterministic population with deliberate quality defects |
| [Stakeholder readout](reports/stakeholder_readout.md) | Finished recommendation and executive artifacts |

## Analytical lifecycle

1. Define the action, decision owner, unit, and as-of date.
2. Validate source coverage, uniqueness, missingness, and valid values.
3. Translate policy into ordered and auditable eligibility rules.
4. Reconcile the population funnel to a stable denominator.
5. Profile the eligible population without causal claims.
6. Assign transparent need, value, and fit points.
7. Rank deterministically and select to operational capacity.
8. Test alternative capacities and planning assumptions.
9. Export only activation-required fields and document suppression logic.
10. Monitor delivery, adoption, segment coverage, complaints, and incremental impact.

## Run locally

From the repository root:

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements-dev.txt
python 03_target_analysis/src/generate_synthetic_data.py
python 03_target_analysis/src/analyze_targets.py
pytest tests/test_target_analysis.py
```

On macOS or Linux, activate with `source .venv/bin/activate`.

The generator writes a full local population and a compact tracked sample. The full dataset and activation export are intentionally ignored; regenerate them locally from the fixed seed.

## Interpretation boundary

The priority score is an auditable policy device, not a predicted probability, causal effect, or entitlement. Expected adoption and contribution are planning scenarios, not observed results. Country and industry are used to monitor operational coverage, not to infer protected characteristics or award points. A controlled activation test is still required to estimate incremental impact.

## Next module

Use [Ad Hoc Analysis](../05_ad_hoc_analysis/README.md) when the question is exploratory, time-bounded, and does not yet warrant a standardized recurring workflow.
