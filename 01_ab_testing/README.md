# Checkout Experiment Decision Analysis

**Evidence status:** Reproducible case study with tested analysis code, inspectable synthetic data, and a finished executive readout.

[Read the NovaPay stakeholder readout](reports/stakeholder_readout.md) · [Download the five-slide deck](reports/stakeholder_readout.pptx) · [Inspect the analysis](src/analyze_experiment.py)

## Business decision

Should NovaPay roll out a simplified digital checkout experience, iterate on it, or stop the change?

The case demonstrates how a randomized experiment is translated into an evidence-calibrated recommendation using implementation checks, prespecified metrics, uncertainty, practical significance, segment review, and business impact.

## What this case demonstrates

- decision framing, hypotheses, and success measures defined before outcome review;
- eligible population, randomization unit, Control, and Treatment design;
- sample-size, power, minimum-detectable-effect, and duration planning;
- experiment-integrity and data-quality validation;
- effect size, confidence interval, and practical-significance reporting;
- segment and guardrail review without causal overclaiming; and
- an executive recommendation with rollout and monitoring conditions.

## Review path

| Evidence | Purpose |
|---|---|
| [Stakeholder readout](reports/stakeholder_readout.md) | Finished decision memo, result interpretation, limitations, and recommendation |
| [Business case](case_study/business_case.md) | Decision, constraints, stakeholders, and expected use |
| [Data dictionary](case_study/data_dictionary.md) | Field definitions, grain, timing, and quality rules |
| [Reproducible analysis notebook](notebooks/reproducible_analysis.ipynb) | Inspectable workflow from validation through recommendation |
| [Method notes](method_notes.md) | Design choices, interpretation guidance, and common failure modes |
| [Analytical methodology](methodology.md) | Reusable execution and review process |
| [Reference analysis](src/analyze_experiment.py) | Tested statistical and business-impact implementation |
| [Synthetic-data generator](src/generate_synthetic_data.py) | Deterministic input generation for independent reproduction |

## Delivery workflow

1. Frame the business decision and possible actions.
2. Define the hypothesis, eligible population, and unit of randomization.
3. Lock primary, secondary, and guardrail measures before reading outcomes.
4. Confirm power, minimum detectable effect, and test duration.
5. Validate implementation, assignment integrity, and analytical data.
6. Estimate absolute and relative effects with uncertainty.
7. Review practical significance, important segments, and guardrails.
8. Translate the result into business impact and a rollout decision.
9. Define monitoring, rollback conditions, and the next evidence required.

## Reproduce the evidence

From the `01_ab_testing` directory:

```bash
pip install -r requirements.txt
python src/generate_synthetic_data.py
python src/analyze_experiment.py
jupyter notebook notebooks/reproducible_analysis.ipynb
```

An optional [analysis workbench](reference/learning_lab/analysis_workbench.ipynb) is retained in the secondary reference area. It is not part of the primary buyer review path.

## Demonstration boundary

NovaPay, the dataset, and the reported results are synthetic. The case demonstrates analytical design, validation, reproducibility, and executive communication; it does not claim a real checkout lift or authorize a production rollout.

## Decision principle

Start with the business decision, not the statistical test. The purpose of experimentation is to reduce uncertainty enough to choose an action responsibly.
