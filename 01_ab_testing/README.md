# A/B Testing Standard Framework

This module defines a repeatable process for understanding, designing, validating, analyzing, and communicating controlled experiments.

## How to use this module

The module is organized in four layers:

1. **Fundamentals** — understand the concepts behind experimentation.
2. **Methodology** — follow the standard execution process.
3. **Practice** — apply the framework using the synthetic NovaPay case.
4. **Stakeholder communication** — convert analytical findings into a concise decision-focused readout.

Start here:

- `ab_testing_fundamentals.md` for what A/B testing is, when to use it, experiment types, statistical concepts, common failure modes, and interpretation principles.
- `methodology.md` for the analytical execution standard.
- `case_study/business_case.md` for the fictional NovaPay business scenario.
- `case_study/data_dictionary.md` for field definitions.
- `notebooks/guided_ab_test_analysis.ipynb` for the step-by-step worked analysis.
- `notebooks/challenge_ab_test_analysis.ipynb` for independent practice with TODO cells and no solutions.
- `templates/stakeholder_readout_deck.md` for the standard stakeholder presentation structure, slide-by-slide guidance, and communication rules.
- `src/generate_synthetic_data.py` to generate the reproducible synthetic dataset.
- `src/analyze_experiment.py` for the reference analysis workflow.

## Standard lifecycle

1. Frame the business decision.
2. Define the hypothesis.
3. Define the eligible population and unit of randomization.
4. Design Control and Treatment groups.
5. Define primary, secondary, and guardrail KPIs before reading outcomes.
6. Plan sample size, power, minimum detectable effect (MDE), and test duration.
7. Validate experiment implementation and data quality.
8. Select statistical methods based on metric type and design.
9. Quantify statistical significance, confidence intervals, and effect size.
10. Investigate segments, confounders, and experiment integrity.
11. Translate the result into business impact.
12. Recommend rollout, iteration, retest, or stop.
13. Communicate the decision using the standard stakeholder readout.

## Case study

The example in this module uses **NovaPay**, a fictional payments company testing a simplified digital checkout experience. All data are synthetic and generated solely for training and portfolio purposes.

## Running the notebooks

From the `01_ab_testing` directory:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/guided_ab_test_analysis.ipynb
```

or:

```bash
jupyter notebook notebooks/challenge_ab_test_analysis.ipynb
```

The guided notebook demonstrates the full workflow from raw data to recommendation. The challenge notebook gives the same business problem and synthetic data, but requires the analyst to build the data-quality checks, statistical analysis, segmentation, business-impact estimate, and executive recommendation independently.

## Important principle

Start with the business decision, not the statistical test. The purpose of experimentation is to reduce uncertainty and support a better decision.
