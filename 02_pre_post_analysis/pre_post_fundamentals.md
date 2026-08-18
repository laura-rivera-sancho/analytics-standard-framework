# Pre/Post Analysis Fundamentals

## What is pre/post analysis?

Pre/post analysis compares a population, process, product, or KPI **before** and **after** a defined intervention or business change.

It is commonly used when a randomized experiment is not possible because a change was launched to everyone, implemented operationally, required for compliance, or already happened before an experiment could be designed.

Examples:
- A new fraud-verification workflow launches globally.
- A support policy changes for all agents.
- A pricing or checkout flow is replaced for all customers.
- A new automation is introduced in an operational process.
- A system migration changes how work is handled.

The core question is usually:

> Did performance change after the intervention, and is the observed change large and credible enough to support a business decision?

## Pre/Post vs A/B testing

An A/B test compares contemporaneous randomized groups. A pre/post analysis compares different time periods.

That difference matters because time itself can introduce alternative explanations.

| A/B Testing | Pre/Post Analysis |
|---|---|
| Control and Treatment run at the same time | Before and After occur at different times |
| Randomization helps balance confounders | Confounders must be investigated explicitly |
| Stronger basis for causal inference | Usually weaker causal identification |
| Best when experimentation is feasible | Useful when no valid Control exists |

Pre/post analysis can provide strong decision support, but analysts should avoid automatically describing every before/after difference as caused by the intervention.

## Core terminology

### Intervention
The product, process, policy, system, or operational change being evaluated.

### Pre period
The observation window before the intervention.

### Post period
The observation window after the intervention.

### Baseline
The level and pattern of a KPI before the change. Baseline should include more than a single point whenever possible.

### Counterfactual
What would likely have happened after the intervention **if the intervention had not occurred**. This is the central challenge in causal analysis because the counterfactual is not directly observed.

### Confounder
A factor that changes around the same time as the intervention and may also affect the KPI.

Examples:
- seasonality
- traffic growth
- customer-mix changes
- a marketing campaign
- staffing changes
- another product release
- economic conditions
- channel or geography shifts

### Guardrail metric
A metric used to detect unintended harm while the primary KPI improves.

## Why choosing the time window matters

A weak pre/post analysis may compare one week before with one week after without checking whether those weeks are representative.

A stronger analysis asks:
- Is the period long enough to capture normal variability?
- Are weekdays and weekends represented consistently?
- Is there monthly or seasonal behavior?
- Was there a launch ramp-up period?
- Did holidays or major campaigns occur?
- Was the business stable before launch?

Using equal-length windows is often convenient, but equal length does not guarantee comparability.

## Common pre/post designs

### 1. Simple before/after comparison
Compares KPI averages or rates before and after a change.

Useful for quick directional analysis, but vulnerable to trend, seasonality, and confounding.

### 2. Segmented pre/post analysis
Repeats the comparison by meaningful segments such as device, market, tenure, product, channel, or customer type.

Useful for understanding whether the observed change is concentrated in specific populations.

### 3. Interrupted Time Series (ITS)
Uses repeated observations over time to estimate whether an intervention is associated with:
- an immediate **level change**, and/or
- a change in **trend** after launch.

ITS is often stronger than a two-period average comparison because it uses the pre-existing trajectory rather than treating the entire pre period as a single number.

### 4. Difference-in-Differences (DiD)
Used when there is a comparison population that was not exposed to the intervention, even if randomization was not possible.

It compares the change over time in the exposed population with the change over time in the comparison population.

A key assumption is **parallel trends**: without the intervention, the groups would have followed similar trends.

### 5. Matched or synthetic comparison approaches
When a natural Control does not exist, analysts may construct a more comparable benchmark using matching, weighting, synthetic controls, or other quasi-experimental methods.

These approaches require stronger assumptions and careful diagnostics.

## Absolute vs relative change

If a KPI moves from 60% to 66%:
- absolute change = **+6 percentage points**
- relative change = **+10%**

Both can be useful, but they answer different questions. Use percentage points for differences between rates and clearly label relative changes.

## Statistical significance vs business significance

A statistically significant difference is not automatically important to the business.

A useful analysis asks both:
1. Is the observed change larger than expected random variation?
2. Is the magnitude large enough to matter operationally or financially?

Always report effect size and uncertainty, not only a p-value.

## Confidence intervals

A confidence interval communicates a range of plausible values for the estimated change under the analytical assumptions.

Narrow intervals indicate greater precision. Wide intervals signal that the data may not support a precise conclusion.

## Statistical tests commonly used

The correct method depends on the metric and design.

### Binary or rate outcomes
Examples: conversion, fraud rate, support contact rate.

Possible methods:
- two-proportion test for a simple independent pre/post comparison
- logistic regression
- segmented regression for time series

### Continuous outcomes
Examples: handling time, checkout duration, transaction value.

Possible methods:
- Welch t-test for independent period comparisons
- Mann–Whitney or robust methods for skewed outcomes
- regression with time/intervention terms
- bootstrap confidence intervals

### Count outcomes
Examples: daily contacts, incidents, completed transactions.

Possible methods:
- Poisson or negative-binomial regression
- time-series regression

The statistical test should match the data-generating process, not simply the analyst's preferred technique.

## Trend and seasonality

One of the biggest risks in pre/post analysis is attributing an existing trend to the intervention.

Example: if completion rate was already improving by 0.3 percentage points each week before launch, a higher post-period average may partly reflect continuation of that trend.

Similarly, weekly, monthly, holiday, or seasonal patterns can distort simple averages.

Plot the KPI over time before drawing conclusions.

## Regression to the mean

If a business launches an intervention immediately after an unusually bad KPI period, some improvement may have occurred naturally even without the intervention.

This is called **regression to the mean** and is a common reason that naive before/after analyses overstate impact.

## Concurrent changes

Document anything else that changed around launch:
- campaigns
- pricing
- staffing
- routing rules
- outages
- policy updates
- tracking changes
- product releases

If a concurrent event could plausibly explain the KPI movement, the final conclusion should acknowledge that limitation.

## Composition or mix shift

A KPI can change because the underlying population changed.

Example: the post period may contain more existing customers and fewer new customers. If existing customers naturally convert at a higher rate, the aggregate KPI may improve even if the intervention has no effect.

Compare important pre/post population characteristics before interpreting outcomes.

## Novelty, adoption, and ramp effects

The first days after launch may not represent steady-state performance.

Reasons include:
- user learning
- employee adaptation
- incomplete rollout
- technical stabilization
- temporary curiosity or novelty

Consider showing launch/ramp separately from the stable post period when appropriate.

## Autocorrelation

Time-based observations are often correlated with nearby observations. Yesterday's performance may resemble today's performance.

This violates the independence assumption behind some simple tests. Interrupted-time-series or time-series regression methods can explicitly account for temporal structure.

## When not to make a causal claim

Use cautious language when:
- there is no credible comparison group
- the pre trend is unstable
- major concurrent changes occurred
- tracking changed at launch
- the population composition shifted materially
- seasonality is not addressed
- the time window is too short

Prefer wording such as:

> Performance improved after launch, and the timing is consistent with a positive intervention effect; however, because there was no randomized Control, the estimate should be interpreted as an observed post-launch association rather than definitive causal proof.

## Common failure modes

- Comparing arbitrary short windows
- Ignoring baseline trend
- Ignoring seasonality
- Ignoring launch ramp-up
- Using different KPI definitions before and after
- Ignoring population-mix shifts
- Failing to identify concurrent changes
- Calling correlation causation
- Reporting only averages and no time-series view
- Reporting only p-values and no effect size
- Running many segment comparisons and highlighting only positive ones
- Treating statistical significance as automatic business value

## Decision rule

A strong pre/post conclusion considers four dimensions together:

1. **Magnitude** — how large is the observed change?
2. **Uncertainty** — how precise is the estimate?
3. **Credibility** — do trends, data quality, mix, and confounders support the interpretation?
4. **Business value** — is the change large enough to influence the decision?

## Key principle

Pre/post analysis is not simply **Before minus After**.

The analytical work is determining whether the observed difference represents a credible intervention-related change rather than normal variation, trend, seasonality, mix shift, or another event.