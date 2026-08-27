# Pre/Post Analysis Standard Framework

This module defines a repeatable process for estimating the impact of a business, product, or operational change when a randomized Control group is not available.

**Portfolio shortcut:** Review the [finished FinFlow stakeholder readout](reports/stakeholder_readout.md)
or [download the five-slide PowerPoint deck](reports/stakeholder_readout.pptx).

## How to use this module

The module follows the same portfolio structure as the A/B testing section:

1. **Fundamentals** — understand what pre/post analysis is, when to use it, and its limitations.
2. **Methodology** — follow a standard execution process from business question to recommendation.
3. **Practice** — apply the framework using a synthetic case study.
4. **Stakeholder communication** — translate results into a decision-focused readout.

Start here:

- [Finished stakeholder readout](reports/stakeholder_readout.md) for the FinFlow decision memo, executive preview, and PowerPoint deck.
- [Guided analysis notebook](notebooks/guided_pre_post_analysis.ipynb) for the worked analysis through adjusted interrupted time series and recommendation.
- [Challenge notebook](notebooks/challenge_pre_post_analysis.ipynb) for independent practice with TODO cells and no worked answers.
- [Pre/Post fundamentals](pre_post_fundamentals.md) and [analytical methodology](methodology.md) for concepts and execution standards.
- [FinFlow business case](case_study/business_case.md), [data dictionary](case_study/data_dictionary.md), and [inspectable synthetic sample](data/raw/finflow_verification_pre_post_sample.csv).
- [Expected analytical narrative](templates/challenge_answer_key.md) and [100-point scoring rubric](templates/challenge_scoring_rubric.md) for self-review.
- [Stakeholder presentation guide](templates/stakeholder_readout_template.md) and [reusable PowerPoint generator](templates/create_stakeholder_readout_pptx.js).
- [Synthetic-data generator](src/generate_synthetic_data.py) and [reference analysis](src/analyze_pre_post.py) for the reproducible workflow.

## Standard lifecycle

1. Frame the business decision.
2. Define the intervention or change.
3. Define the pre and post periods.
4. Define the population and inclusion/exclusion rules.
5. Define primary, secondary, and guardrail KPIs.
6. Validate data quality and metric consistency across periods.
7. Inspect baseline trends, seasonality, and structural differences.
8. Identify concurrent changes and likely confounders.
9. Select the appropriate comparison method.
10. Quantify absolute and relative change with uncertainty.
11. Segment results to explain heterogeneous impact.
12. Separate observed association from causal claims.
13. Translate findings into business impact.
14. Recommend rollout continuation, iteration, rollback, or further validation.
15. Communicate findings using the standard stakeholder readout.

## Case study

The case uses **FinFlow**, a fictional payments company that introduced an automated transaction-verification workflow to reduce manual review time while maintaining payment quality and fraud controls.

Because the workflow was launched to all eligible traffic at once, there is no randomized Control group. The analyst must compare outcomes before and after launch while accounting for trend, seasonality, traffic mix, and other concurrent changes.

The generated dataset intentionally includes a mild baseline trend, day-of-week seasonality, a seven-day launch ramp, post-period mix shifts, a short marketing campaign, right-skewed verification time, rare fraud events, and a small number of raw data-quality defects.

All data and results in this module are synthetic and created solely for training and portfolio purposes.

## Running the reference workflow

From the `02_pre_post_analysis` directory:

```bash
pip install -r requirements.txt
python src/generate_synthetic_data.py
python src/analyze_pre_post.py
```

To open the guided analysis:

```bash
jupyter notebook notebooks/guided_pre_post_analysis.ipynb
```

To open the challenge version:

```bash
jupyter notebook notebooks/challenge_pre_post_analysis.ipynb
```

To generate the stakeholder PowerPoint template:

```bash
cd templates
npm install
npm run build:pptx
```

The guided notebook generates the synthetic raw dataset in memory and walks through data-quality validation, re-derivation of intervention timing, simple Pre/Post inference, full vs stable Post comparison, daily trend analysis, traffic-mix checks, continuous and guardrail metrics, basic and adjusted Interrupted Time Series, a model-based counterfactual, segment analysis, business impact, causal-confidence assessment, and stakeholder recommendation.

The full raw and clean reference datasets are generated locally and excluded from Git. The compact 1,000-row sample remains tracked so reviewers can inspect the schema and intentional defects without running the generator first.

## Important principle

A pre/post difference is not automatically a causal effect. The analyst's job is to determine whether the observed change is consistent with the intervention while explicitly evaluating alternative explanations.
