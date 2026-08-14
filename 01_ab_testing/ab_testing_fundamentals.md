# A/B Testing Fundamentals

## What A/B testing is

A/B testing is a controlled experimentation method used to estimate the causal impact of a change by comparing outcomes between groups exposed to different experiences.

A typical A/B test has:

- **Control:** the current or baseline experience.
- **Treatment:** the new experience being tested.
- **Random assignment:** eligible units are assigned to groups so they are comparable in expectation.
- **Pre-defined metrics:** success and guardrail metrics are chosen before reviewing results.
- **Statistical inference:** observed differences are evaluated to determine whether they are likely to reflect a real treatment effect rather than random variation.

The objective is not simply to prove that one version is better. The objective is to reduce uncertainty around a business decision.

## When to use A/B testing

A/B testing is appropriate when:

- the business can expose comparable populations to different experiences;
- the treatment can be clearly defined;
- the outcome can be measured reliably;
- the experiment can run long enough to obtain adequate sample size;
- the groups can remain sufficiently isolated from one another;
- there is a real decision that will be made from the result.

Typical use cases include:

- checkout or conversion-flow changes;
- onboarding changes;
- pricing or offer presentation;
- messaging and communications;
- product-feature launches;
- customer-support process changes;
- fraud or risk interventions;
- recommendation algorithms;
- retention or engagement initiatives.

## When not to use A/B testing

A randomized A/B test may not be practical or appropriate when:

- there is insufficient traffic or sample size;
- the treatment cannot be isolated between groups;
- the change affects an entire system at once;
- strong network effects cause users in one group to influence another;
- legal, ethical, operational, or risk constraints prevent random assignment;
- the expected effect takes too long to observe;
- the experiment could expose customers or the business to unacceptable harm.

Alternatives may include pre/post analysis, matched-control designs, difference-in-differences, interrupted time series, geo experiments, switchback designs, or observational modeling.

## Core experiment structure

### Business question

Start with the decision the experiment is intended to support.

Example:

> Should we roll out a simplified checkout experience?

### Hypothesis

A hypothesis states what effect is expected and on which outcome.

- **Null hypothesis (H0):** there is no true treatment effect on the primary KPI.
- **Alternative hypothesis (H1):** the treatment changes the primary KPI.

For a directional business hypothesis, the expected direction should be documented before the test.

### Unit of randomization

The unit assigned to Control or Treatment may be:

- customer;
- account;
- session;
- transaction;
- merchant;
- store;
- geographic market;
- time block.

The correct unit depends on how the treatment is delivered and where contamination could occur.

## Why randomization matters

Randomization helps distribute both observed and unobserved characteristics across groups so that, in expectation, the treatment is the main systematic difference between them.

This strengthens causal interpretation.

Randomization does not eliminate the need for quality checks. Analysts should still verify:

- allocation counts;
- sample-ratio mismatch;
- exposure integrity;
- duplicate experimental units;
- important pre-treatment balance;
- tracking quality.

## Common types of controlled experiments

| Type | Description | Typical use |
|---|---|---|
| **A/B test** | One Control and one Treatment | Compare a new experience with the current one |
| **A/B/n test** | One Control and multiple Treatments | Compare several variants at once |
| **Multivariate test** | Multiple components are varied jointly | Understand combinations of page or product elements |
| **Holdout test** | A persistent Control group is intentionally not exposed to a change | Measure longer-term incremental impact |
| **Switchback experiment** | Treatment alternates over time for the same market/system | Marketplace, operations, delivery, or system-level interventions |
| **Geo experiment** | Geographic regions receive different treatments | Marketing, pricing, media, or policy changes where user-level randomization is difficult |
| **Cluster-randomized experiment** | Groups such as stores, teams, or merchants are randomized | Reduce contamination when treatment occurs at group level |

## A/B versus multivariate testing

An A/B test compares complete experiences or treatments.

A multivariate test evaluates combinations of several components simultaneously, such as headline, image, and call-to-action.

Multivariate tests generally require more traffic because the sample is distributed across more combinations.

## One-tailed versus two-tailed tests

### Two-tailed

Tests whether Treatment is different from Control in either direction.

Use when both improvement and deterioration are important and no valid directional restriction should be imposed.

### One-tailed

Tests for an effect in one pre-specified direction.

A one-tailed test should not be chosen after seeing the result. In many business settings, two-tailed tests are safer because an unexpected negative effect also matters.

## Primary, secondary, and guardrail metrics

### Primary KPI

The main outcome used to evaluate the hypothesis.

Examples:

- conversion rate;
- activation rate;
- retention rate;
- average order value;
- processing time.

### Secondary KPIs

Help explain mechanism or downstream impact.

### Guardrail KPIs

Protect against unintended harm.

Examples:

- fraud rate;
- complaint rate;
- support contacts;
- latency;
- cancellation;
- payment declines;
- operational cost.

A successful experiment should not be defined only by improvement in the primary KPI if important guardrails deteriorate materially.

## Baseline

The baseline is the expected performance of the current experience before treatment effects are considered.

Baseline values are used in:

- sample-size planning;
- MDE definition;
- business-impact estimation;
- interpretation of relative lift.

## Minimum Detectable Effect (MDE)

The MDE is the smallest treatment effect the experiment is designed to detect with the chosen significance level and statistical power.

It should be connected to business value.

A test designed to detect an extremely small effect may require a very large sample even if that effect would not matter commercially.

## Statistical power

Statistical power is the probability of detecting a true effect of the planned size when that effect actually exists.

A common planning target is 80% or higher.

Low-powered experiments have a higher risk of missing real effects.

## Significance level (alpha)

Alpha represents the acceptable probability of a Type I error under the testing framework.

A common threshold is:

`alpha = 0.05`

The threshold should be chosen before reviewing experiment outcomes.

## P-value

A p-value measures how compatible the observed result is with the null hypothesis under the statistical model.

A p-value below the pre-defined alpha provides evidence against the null hypothesis.

It does **not** mean:

- there is a 95% probability that the Treatment works;
- there is only a 5% probability that the null hypothesis is true;
- the result is automatically important for the business.

## Confidence interval

A confidence interval provides a range of plausible treatment-effect values under repeated-sampling interpretation.

It helps answer two questions:

1. How uncertain is the estimated effect?
2. Is the range large enough to be meaningful for the business?

Confidence intervals are often more informative than a p-value alone.

## Effect size

Effect size measures the magnitude of the treatment difference.

Common business forms include:

- absolute percentage-point lift;
- relative percentage lift;
- mean difference;
- standardized effect size;
- incremental revenue or cost savings.

Example:

Control conversion = 60%  
Treatment conversion = 63%

- absolute lift = **+3 percentage points**;
- relative lift = **+5%**.

## Statistical significance versus business significance

A result can be statistically significant but commercially irrelevant.

With a very large sample, even a tiny difference may produce a small p-value.

A good decision considers:

- effect size;
- confidence interval;
- implementation cost;
- risk;
- operational impact;
- customer impact;
- strategic relevance.

## Type I and Type II errors

### Type I error — false positive

Conclude that Treatment has an effect when no real effect exists.

Business consequence: roll out an ineffective or harmful change.

### Type II error — false negative

Fail to detect an effect that actually exists.

Business consequence: reject or abandon a valuable improvement.

## Sample Ratio Mismatch (SRM)

SRM occurs when the observed experiment allocation differs materially from the intended allocation beyond what random variation would reasonably explain.

Example:

Expected: 50% Control / 50% Treatment  
Observed: 38% Control / 62% Treatment

Possible causes:

- broken randomization;
- tracking failures;
- filtering differences;
- eligibility logic errors;
- treatment-specific dropouts;
- extraction problems.

SRM is an experiment-health issue and should be investigated before treatment effects are trusted.

## Sample size

Sample size depends on:

- baseline metric;
- MDE;
- alpha;
- desired power;
- allocation ratio;
- metric variance;
- expected traffic.

Do not choose sample size based only on how many observations happen to be available.

## Experiment duration

Run the experiment long enough to:

- achieve the planned sample;
- cover representative business cycles;
- avoid unusual calendar periods dominating the result;
- observe delayed outcomes where relevant.

Longer is not always better. Excessively long tests can increase exposure cost and the chance of contamination or concurrent changes.

## Peeking and early stopping

Repeatedly checking the p-value and stopping the experiment as soon as it crosses 0.05 can inflate false-positive risk under standard fixed-horizon testing.

Use a pre-defined stopping rule or a sequential-testing method if continuous monitoring is required.

## Multiple testing

Testing many metrics, variants, or segments increases the probability of observing at least one apparently significant result by chance.

Options include:

- pre-specifying a limited set of hypotheses;
- defining a single primary KPI;
- adjusting for multiple comparisons when appropriate;
- treating post-hoc segment findings as exploratory;
- validating promising findings in a follow-up experiment.

## Segmentation and heterogeneous treatment effects

The average experiment result may hide important differences across groups.

Common segments:

- country;
- device;
- customer tenure;
- acquisition channel;
- merchant type;
- customer risk level;
- product type.

Segment analysis should distinguish between:

- **pre-specified segments:** defined before the test;
- **post-hoc segments:** discovered after seeing results.

Post-hoc findings should generally be treated as new hypotheses rather than final causal conclusions.

## Contamination and interference

### Contamination

A unit assigned to Control is exposed to the Treatment, or vice versa.

### Interference

One experimental unit's treatment affects another unit's outcome.

Examples:

- customers sharing referral codes;
- marketplace participants influencing each other;
- store-level operational changes affecting nearby stores;
- team-level treatments where employees interact across groups.

If interference is expected, individual-level randomization may not be appropriate.

## Novelty effect

Users may respond differently simply because an experience is new.

A short-lived improvement may disappear once users adapt.

Longer observation windows or post-rollout monitoring may be needed for durable behavior changes.

## Carryover effect

Past treatment exposure can affect later outcomes.

This is especially important in crossover or switchback experiments.

A washout period may be needed between conditions.

## Common statistical methods by metric type

| Metric type | Example | Common approach |
|---|---|---|
| **Binary / proportion** | conversion, activation, fraud flag | two-proportion z-test, logistic regression |
| **Continuous** | AHT, checkout time, spend | Welch/two-sample t-test when appropriate, regression, robust or non-parametric methods |
| **Count** | purchases, contacts, claims | Poisson/negative-binomial models or suitable count methods |
| **Categorical** | reason category, channel distribution | chi-square or multinomial methods |
| **Time-to-event** | time to churn, time to activation | survival-analysis methods |

The test should match the metric, randomization structure, assumptions, and decision context.

## Continuous metrics and normality

A common misconception is that every raw observation must be perfectly normally distributed before a t-test can be used.

In practice, analysts should inspect:

- skewness;
- outliers;
- sample size;
- variance;
- whether the mean is the business quantity of interest.

For strongly skewed metrics such as transaction value or handling time, consider reporting both mean and median and validating conclusions with robust, transformed, bootstrap, or non-parametric approaches when appropriate.

## Confounding variables

Randomization is designed to reduce confounding, but analysts should still look for operational or implementation problems.

Potential confounders include:

- simultaneous campaigns;
- system outages;
- pricing changes;
- seasonality;
- channel mix changes;
- geographic events;
- policy changes;
- changes in staffing or operations.

For a properly randomized and implemented experiment, these factors should not systematically affect one group more than another. If they do, investigate before making a causal claim.

## Causal interpretation

A valid randomized experiment provides stronger causal evidence than a simple before/after comparison because exposure is assigned rather than merely observed.

Causal confidence weakens when there is:

- broken randomization;
- non-compliance;
- contamination;
- severe attrition;
- missing tracking;
- post-treatment filtering;
- major implementation differences between groups.

## Common experiment failure modes

1. No clear business decision.
2. Primary KPI selected after seeing results.
3. Inadequate sample size.
4. Broken randomization or SRM.
5. Missing or inconsistent tracking.
6. Treatment contamination.
7. Stopping too early because p < 0.05.
8. Ignoring guardrails.
9. Over-interpreting post-hoc segments.
10. Reporting only p-values without effect size or confidence intervals.
11. Confusing statistical significance with business value.
12. Ignoring implementation cost or operational risk.

## Recommended interpretation framework

A strong experiment readout answers:

1. **What decision were we testing?**
2. **Was the experiment valid?**
3. **What happened to the primary KPI?**
4. **How large was the effect?**
5. **How uncertain is the estimate?**
6. **What happened to guardrails?**
7. **Were there important segment differences?**
8. **What is the business impact?**
9. **What should the business do next?**

## Relationship to the rest of this module

Use this document for conceptual understanding.

Then use:

- `methodology.md` for the standard execution process;
- `case_study/business_case.md` for the NovaPay scenario;
- `notebooks/guided_ab_test_analysis.ipynb` for a worked example;
- `notebooks/challenge_ab_test_analysis.ipynb` for independent practice.

The guiding principle remains:

> **Start with the business decision, validate the experiment, quantify both statistical and business impact, and end with a clear recommendation.**
