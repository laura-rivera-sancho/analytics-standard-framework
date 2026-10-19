# Launch Impact Assessment

**Evidence status:** Reproducible observational case study with adjusted interrupted-time-series analysis and a finished executive readout.

[Read the FinFlow stakeholder readout](reports/stakeholder_readout.md) · [Download the five-slide deck](reports/stakeholder_readout.pptx) · [Inspect the analysis](src/analyze_pre_post.py)

## Business decision

Should FinFlow continue scaling an automated transaction-verification workflow, change the rollout, or pause for additional validation?

The workflow launched to all eligible traffic at once, so a randomized Control group is unavailable. The analysis must separate the observed before-and-after movement from trend, seasonality, traffic mix, ramp effects, and concurrent changes.

## What this case demonstrates

- an explicit intervention date, analytical population, and comparison design;
- consistent primary, secondary, and guardrail definitions across periods;
- baseline-trend, seasonality, ramp, and stable-post assessment;
- traffic-mix and concurrent-event diagnostics;
- simple and adjusted interrupted-time-series estimates;
- a model-based counterfactual with transparent assumptions;
- causal-confidence calibration and alternative explanations; and
- a continue, iterate, rollback, or validate-further recommendation.

## Review path

| Evidence | Purpose |
|---|---|
| [Stakeholder readout](reports/stakeholder_readout.md) | Finished decision memo, executive preview, limitations, and recommendation |
| [Business case](case_study/business_case.md) | FinFlow decision, intervention, constraints, and stakeholders |
| [Inspectable data sample](data/raw/finflow_verification_pre_post_sample.csv) | Schema, analytical grain, and deliberate quality issues |
| [Reproducible analysis notebook](notebooks/reproducible_analysis.ipynb) | Workflow through adjusted interrupted time series and recommendation |
| [Method notes](method_notes.md) | Appropriate use, design choices, and causal limitations |
| [Analytical methodology](methodology.md) | Reusable execution and quality-control process |
| [Reference findings](templates/reference_findings.md) | Expected analytical narrative and interpretation boundary |
| [Quality and acceptance checklist](templates/quality_acceptance_checklist.md) | Review criteria for a decision-ready impact assessment |
| [Reference analysis](src/analyze_pre_post.py) | Reproducible estimation and business-impact implementation |

## Delivery workflow

1. Define the decision, intervention, comparison periods, population, and exclusions.
2. Lock primary, secondary, and guardrail measures.
3. Validate data quality and metric consistency across periods.
4. Inspect baseline trends, seasonality, ramp behavior, and structural differences.
5. Identify concurrent changes and likely confounders.
6. Estimate observed and adjusted changes with uncertainty.
7. Review segments and alternative explanations.
8. Calibrate causal confidence and translate findings into business impact.
9. Recommend continuation, iteration, rollback, or additional validation.

## Reproduce the evidence

From the `02_pre_post_analysis` directory:

```bash
pip install -r requirements.txt
python src/generate_synthetic_data.py
python src/analyze_pre_post.py
jupyter notebook notebooks/reproducible_analysis.ipynb
```

The full generated datasets remain untracked; the compact 1,000-row sample supports inspection without running the generator. An optional [analysis workbench](reference/learning_lab/analysis_workbench.ipynb) is retained in the secondary reference area and is not part of the primary buyer journey.

## Demonstration boundary

FinFlow, the intervention, the dataset, and the reported results are synthetic. A before-and-after difference is not automatically causal. A real engagement would require representative operational data, confirmed concurrent events, agreed confidence thresholds, and decision-owner review.

## Decision principle

The objective is not to force a causal claim. It is to determine which conclusions the evidence supports, which alternatives remain credible, and what action is justified now.
