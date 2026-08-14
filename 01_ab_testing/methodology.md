# A/B Testing Methodology

## Purpose

Use this framework when the business can expose comparable populations to different experiences and wants to estimate the causal effect of a change.

## 1. Frame the business decision

Document the decision the experiment is intended to support. Examples: launch a new feature, change a process, simplify a customer journey, modify a message, or change a pricing/offer experience.

Required questions:
- What decision will be made from the result?
- Why does the change matter to the business?
- What customer or operational problem is being addressed?
- What is the expected direction of impact?

## 2. Define hypotheses

State the hypotheses before reading experiment outcomes.

- **Null hypothesis (H0):** the Treatment does not produce a meaningful difference from Control for the primary KPI.
- **Alternative hypothesis (H1):** the Treatment changes the primary KPI in the expected direction.

Also define the **Minimum Detectable Effect (MDE)** or smallest effect the business considers worth detecting.

## 3. Define population and randomization

Specify:
- unit of randomization (customer, account, session, transaction, merchant, etc.)
- eligibility rules
- exclusions
- treatment allocation ratio
- exposure rules
- contamination risks

Random assignment is preferred because it reduces systematic differences between groups. After assignment, validate group balance on key pre-treatment characteristics.

## 4. Define metrics before reading results

### Primary KPI
Directly answers the main hypothesis and should be limited to a small number of pre-specified outcomes.

### Secondary KPIs
Help explain the mechanism or downstream business effect.

### Guardrail KPIs
Detect unintended harm. Examples: fraud, complaints, latency, support contacts, cancellation, or operational cost.

Avoid selecting success metrics after observing outcomes.

## 5. Plan sample size and duration

Plan using:
- baseline performance
- MDE
- significance level (commonly alpha = 0.05)
- desired power (commonly 80% or higher)
- expected traffic
- expected business-cycle variation

Run the test long enough to achieve the planned sample and cover a representative business cycle. Avoid stopping solely because a p-value temporarily crosses a significance threshold.

## 6. Validate experiment health

Before outcome analysis, check:
- assignment counts and sample-ratio mismatch
- duplicate units
- missing experiment assignment
- exposure contamination
- event/tracking completeness
- unexpected implementation changes
- severe guardrail deterioration

If randomization or tracking is materially compromised, pause causal interpretation and investigate.

## 7. Validate analytical data

Perform reproducible quality checks for:
- schema and data types
- duplicate IDs
- missing critical fields
- impossible values
- inconsistent categories
- date range
- metric construction
- one unit appearing in multiple groups

Document exclusions and the final analytical population.

## 8. Select the statistical method

The statistical test depends on metric type and experiment design.

### Binary/proportion outcome
Examples: conversion, activation, DSAT flag, support-contact rate.

Typical method: two-proportion z-test or equivalent regression approach.

### Continuous outcome
Examples: AHT, checkout duration, transaction amount.

Typical method: two-sample t-test/Welch t-test when appropriate. Inspect skewness, outliers, and variance. For heavily skewed outcomes, consider robust summaries, transformations, bootstrap confidence intervals, or non-parametric validation.

### Categorical outcome
Examples: reason category, channel mix.

Typical method: chi-square or a model appropriate to the design.

Do not select a test simply because it is familiar; match the method to the outcome and assumptions.

## 9. Quantify the effect

Report more than the p-value:
- Control and Treatment values
- absolute lift
- relative lift
- 95% confidence interval
- p-value or equivalent evidence measure
- effect size where useful

Statistical significance and business significance are different. A tiny effect can be statistically significant with very large samples while being commercially irrelevant.

## 10. Diagnose and segment

Investigate:
- pre-specified segments
- heterogeneous treatment effects
- operational anomalies
- concurrent campaigns or releases
- seasonality
- channel/device/country differences

Treat post-hoc segment discoveries as exploratory unless validated independently. Multiple comparisons increase false-positive risk.

## 11. Translate into business impact

Estimate the practical consequence of the effect. Depending on the case this may include:
- incremental conversions
- additional active customers
- revenue/volume opportunity
- avoided costs
- customer-experience improvement
- risk impact

Quantify uncertainty where possible.

## 12. Make the recommendation

Choose one of four outcomes:
- **Roll out:** evidence is statistically credible, commercially meaningful, and guardrails are acceptable.
- **Iterate:** direction is promising but design/experience can be improved.
- **Retest/extend:** evidence is inconclusive or a new hypothesis should be validated.
- **Stop/rollback:** treatment causes harm or fails to create enough value.

## Executive communication standard

Lead with:
1. business question
2. result and magnitude
3. confidence/evidence
4. guardrail impact
5. business implication
6. recommendation

Technical statistics belong in supporting detail or an appendix unless the audience requests them.