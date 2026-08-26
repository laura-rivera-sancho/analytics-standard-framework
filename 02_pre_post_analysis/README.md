# Pre/Post Analysis Standard Framework

This module defines a repeatable process for estimating the impact of a business, product, or operational change when a randomized Control group is not available.

## How to use this module

The module follows the same portfolio structure as the A/B testing section:

1. **Fundamentals** — understand what pre/post analysis is, when to use it, and its limitations.
2. **Methodology** — follow a standard execution process from business question to recommendation.
3. **Practice** — apply the framework using a synthetic case study.
4. **Stakeholder communication** — translate results into a decision-focused readout.

Start here:

- `pre_post_fundamentals.md` for core concepts and terminology.
- `methodology.md` for the analytical execution standard.
- `case_study/business_case.md` for the fictional FinFlow scenario.
- `case_study/data_dictionary.md` for the synthetic dataset definition.
- `data/raw/finflow_verification_pre_post_sample.csv` for a compact inspectable synthetic sample with deliberate data-quality defects.
- `notebooks/guided_pre_post_analysis.ipynb` for the step-by-step worked analysis from raw Pre/Post comparison through adjusted Interrupted Time Series and recommendation.
- `notebooks/challenge_pre_post_analysis.ipynb` for the independent practice version with TODO cells and no worked answers.
- `templates/stakeholder_readout_template.md` for the standard stakeholder presentation structure and communication rules.
- `templates/challenge_answer_key.md` for the expected analytical narrative and interpretation.
- `templates/challenge_scoring_rubric.md` for a 100-point review rubric.
- `templates/create_stakeholder_readout_pptx.js` to generate a reusable PowerPoint stakeholder readout template.
- `src/generate_synthetic_data.py` to generate reproducible raw and clean FinFlow datasets.
- `src/analyze_pre_post.py` for the reference analysis, including simple Pre/Post comparisons and an adjusted interrupted-time-series model.
- `requirements.txt` for the Python environment.

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
