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
- `case_study/data_dictionary.md` for the planned synthetic dataset.

Guided and challenge notebooks, reusable code, and stakeholder templates will be added next.

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

## Case study

The first case uses **FinFlow**, a fictional payments company that introduced an automated transaction-verification workflow to reduce manual review time while maintaining payment quality and fraud controls.

Because the workflow was launched to all eligible traffic at once, there is no randomized Control group. The analyst must compare outcomes before and after launch while accounting for trend, seasonality, traffic mix, and other concurrent changes.

All data and results in this module are synthetic and created solely for training and portfolio purposes.

## Important principle

A pre/post difference is not automatically a causal effect. The analyst's job is to determine whether the observed change is consistent with the intervention while explicitly evaluating alternative explanations.