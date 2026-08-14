# A/B Testing Fundamentals — Beginner-Friendly Guide

This page explains A/B testing in simple language. It is written for people who may be new to experimentation, statistics, or analytics.

The goal is not to memorize formulas. The goal is to understand the logic well enough to make better business decisions.

---

## 1. What is A/B testing?

A/B testing is a way to compare **two versions of something** to see which one performs better.

For example, imagine a company wants to simplify its checkout process.

- **Version A — Control:** the current checkout experience
- **Version B — Treatment:** the new simplified checkout experience

Customers are randomly assigned to one of the two versions.

Then we compare the results.

Example:

- Control checkout completion: **72%**
- Treatment checkout completion: **75%**

The main question becomes:

> Did the new checkout actually improve completion, or could this difference have happened by chance?

That is what A/B testing helps us answer.

---

## 2. Why do companies use A/B tests?

A/B testing helps businesses test ideas before making a large change for everyone.

Instead of saying:

> “We think this new feature is better.”

we can say:

> “We tested it with comparable groups and measured the result.”

Typical uses include:

- website or app changes
- checkout improvements
- onboarding flows
- email or message changes
- pricing or offer presentation
- product features
- customer-support changes
- fraud or risk rules
- recommendation systems
- retention or engagement initiatives

The main goal is to **reduce uncertainty before making a decision**.

---

## 3. The basic structure of an A/B test

A simple A/B test usually has four parts.

### Control

The current experience.

Example:

> Existing checkout flow

### Treatment

The new experience being tested.

Example:

> Simplified checkout flow

### Random assignment

Eligible users are randomly placed into Control or Treatment.

This is important because it helps make the groups similar before the test starts.

### Metrics

We decide in advance what success means.

Example:

- Primary KPI: checkout completion
- Secondary KPI: checkout time
- Guardrail KPI: fraud rate

---

## 4. Why does randomization matter?

Imagine we gave the new checkout only to younger customers and the old checkout only to older customers.

If the new checkout performs better, we would not know whether the improvement came from:

- the checkout change, or
- the difference between the customer groups.

Randomization helps avoid this problem.

It spreads different types of customers across both groups so the main planned difference is the experience they receive.

Randomization does not guarantee a perfect experiment, so we still check:

- group sizes
- duplicate users
- missing assignments
- whether users accidentally saw both versions
- whether important customer characteristics look reasonably balanced
- whether tracking worked correctly

---

## 5. What is a hypothesis?

A hypothesis is simply a statement we want to test.

Example:

> The simplified checkout will increase checkout completion.

In statistics, we usually write two versions.

### Null hypothesis — H0

Assume there is **no real difference** between Control and Treatment.

### Alternative hypothesis — H1

Assume there **is a real difference**.

You do not need to think of these as complicated statistical ideas.

A simple way to remember them is:

- **H0:** nothing really changed
- **H1:** the Treatment changed the result

---

## 6. What should we measure?

A good experiment normally uses three types of metrics.

### Primary KPI

The most important metric.

It answers the main business question.

Examples:

- conversion rate
- activation rate
- retention rate
- completion rate
- average handling time

### Secondary KPIs

These help explain what else happened.

Example:

If checkout completion improves, we may also check whether checkout time decreased.

### Guardrail KPIs

These help make sure the Treatment does not create a new problem.

Examples:

- fraud rate
- complaints
- payment declines
- cancellations
- support contacts
- system latency
- operational cost

A Treatment should not be considered successful just because the primary KPI improves if an important guardrail becomes much worse.

---

## 7. What is a baseline?

The baseline is the current level of performance before we expect any Treatment effect.

Example:

Current checkout completion = **72%**

That 72% is our baseline.

The baseline helps us estimate:

- how much improvement would matter
- how many users we need in the test
- what business impact a lift could create

---

## 8. What is lift?

Lift means the difference between Treatment and Control.

Example:

- Control = 60%
- Treatment = 63%

### Absolute lift

63% - 60% = **+3 percentage points**

### Relative lift

3 / 60 = **+5% relative improvement**

These are not the same thing.

A move from 60% to 63% is:

- **+3 percentage points** absolute
- **+5%** relative

---

## 9. What is business significance?

A result may be statistically real but still too small to matter.

Example:

Suppose a Treatment increases conversion from:

- 60.00% to 60.05%

With a very large sample, that tiny difference could be statistically significant.

But the business may decide the gain is not worth the cost of implementing the change.

So we always ask two questions:

1. Is the effect statistically credible?
2. Is the effect large enough to matter to the business?

---

## 10. What is the Minimum Detectable Effect — MDE?

The **Minimum Detectable Effect**, or MDE, is the smallest improvement we want the experiment to be able to detect.

Example:

The business may say:

> We only care about the new checkout if it improves completion by at least 2 percentage points.

Then **+2 percentage points** is the business-relevant target.

The smaller the effect we want to detect, the more data we usually need.

---

## 11. What is sample size?

Sample size means how many users or observations are included in the experiment.

Too little data can make it hard to tell whether a difference is real.

Sample-size planning normally depends on:

- the current baseline
- the MDE
- the amount of variation in the metric
- the significance level
- the desired statistical power
- the Control/Treatment split

The important idea is simple:

> Do not stop the test just because we already have “a lot of data.” We need enough data for the question we are trying to answer.

---

## 12. What is statistical power?

Statistical power tells us how likely the experiment is to detect a real effect of the size we planned for.

A common target is **80% power**.

In simple terms:

> If a meaningful effect really exists, do we have enough data to have a good chance of finding it?

Low power increases the chance that we miss a real improvement.

---

## 13. What is alpha?

Alpha is the threshold we choose for deciding how much false-positive risk we are willing to accept.

A common value is:

`alpha = 0.05`

This is connected to the p-value we see later.

The important point is that alpha should be chosen **before** we look at the results.

---

## 14. What is a p-value?

A p-value helps us judge whether the difference we observed could reasonably happen if there were actually no Treatment effect.

A common rule is:

- p-value < 0.05 → evidence against “no difference”
- p-value >= 0.05 → not enough evidence to reject “no difference”

But a p-value does **not** tell us whether the result is important to the business.

It also does **not** mean:

- there is a 95% chance the Treatment works
- there is only a 5% chance the null hypothesis is true

Think of the p-value as one piece of evidence, not the whole decision.

---

## 15. What is a confidence interval?

A confidence interval gives us a reasonable range for the size of the Treatment effect.

Example:

Estimated lift = **+3.2 percentage points**

95% confidence interval = **+1.8 to +4.6 percentage points**

This tells us the result is not just one exact number.

There is uncertainty around the estimate.

Confidence intervals are useful because they help us ask:

- Could the true effect be close to zero?
- Could the true effect be large enough to matter?
- How precise is our estimate?

---

## 16. Statistical significance vs business significance

These are different.

### Statistical significance

Asks:

> Is the observed difference likely to be more than random variation?

### Business significance

Asks:

> Is the difference large enough to matter?

A good recommendation should consider both.

---

## 17. Type I and Type II errors

These sound technical, but the ideas are simple.

### Type I error — false positive

We conclude the Treatment works when it actually does not.

Business example:

> We roll out a feature that does not really improve performance.

### Type II error — false negative

We fail to detect a real improvement.

Business example:

> We reject a good feature because the test did not have enough data.

---

## 18. What is Sample Ratio Mismatch — SRM?

Suppose we planned a 50/50 experiment.

Expected:

- 50% Control
- 50% Treatment

But we observe:

- 38% Control
- 62% Treatment

That may be a warning sign.

This is called **Sample Ratio Mismatch**, or SRM.

Possible causes include:

- broken assignment logic
- tracking problems
- filtering mistakes
- eligibility errors
- Treatment-specific dropouts
- data-extraction issues

SRM does not automatically mean the experiment is unusable, but it should be investigated before we trust the results.

---

## 19. How long should an experiment run?

A test should run long enough to:

- reach the planned sample size
- cover normal business patterns
- include relevant weekdays/weekends if needed
- capture delayed outcomes

A test should not stop simply because the p-value looks good on one day.

---

## 20. What is peeking?

Peeking means checking the result repeatedly and stopping as soon as it becomes statistically significant.

Example:

Day 3: p = 0.12  
Day 4: p = 0.08  
Day 5: p = 0.04 → stop the test immediately

With normal fixed-horizon testing, this can increase the risk of false positives.

Better practice:

- define the sample size and stopping rule in advance, or
- use a statistical method designed for continuous monitoring

---

## 21. What is multiple testing?

Imagine we test:

- 20 metrics
- 10 countries
- 5 customer types
- 4 devices

Eventually, something may look significant just by chance.

This is the multiple-testing problem.

Ways to reduce the risk include:

- define the main hypothesis before the experiment
- keep one clear primary KPI
- limit unnecessary comparisons
- treat unexpected segment findings as exploratory
- validate interesting findings in a future experiment

---

## 22. What is segmentation?

Segmentation means checking whether different groups reacted differently to the Treatment.

Examples:

- Mobile vs Desktop
- New vs Existing customers
- Country
- Product type
- Acquisition channel

Example:

Overall Treatment lift = **+3 pp**

But:

- Mobile = **+5 pp**
- Desktop = **+1 pp**

That may be useful for the business.

However, there is an important difference.

### Pre-specified segment

We planned to analyze it before seeing results.

### Post-hoc segment

We discovered it after seeing results.

Post-hoc findings can be useful, but they should usually be treated as a new hypothesis to test rather than a final conclusion.

---

## 23. What is contamination?

Contamination happens when users do not stay in the group they were assigned to.

Example:

A customer assigned to Control somehow sees the Treatment experience.

If this happens often, the groups become less different and the result becomes harder to interpret.

---

## 24. What is interference?

Interference happens when one person's Treatment affects another person's outcome.

Example:

In a marketplace, changing the experience for sellers may also affect buyers.

Or employees in a Treatment team may share a new process with employees in a Control team.

In those cases, randomizing individual people may not be the best design.

---

## 25. What is a novelty effect?

Sometimes people react strongly to something simply because it is new.

Example:

A redesigned app screen gets high engagement during the first week, but the effect disappears after users get used to it.

This is called a novelty effect.

For important behavior changes, longer observation or post-launch monitoring may be useful.

---

## 26. What is a carryover effect?

A carryover effect happens when a previous Treatment continues to affect behavior later.

This matters in experiments where the same users or systems switch between Control and Treatment over time.

Example:

A delivery team uses a new routing method in the morning and returns to the old method in the afternoon, but the morning changes continue to influence afternoon operations.

Sometimes a **washout period** is needed before switching conditions.

---

## 27. Common types of experiments

| Experiment type | Simple explanation | Example |
|---|---|---|
| **A/B test** | Compare one current version with one new version | Old checkout vs new checkout |
| **A/B/n test** | Compare Control with several new versions | Current page vs three new designs |
| **Multivariate test** | Test several elements and combinations at the same time | Headline + image + button combinations |
| **Holdout test** | Keep one group unchanged for a longer period | Measure the long-term impact of a loyalty program |
| **Switchback test** | Alternate Control and Treatment over time | New delivery policy on/off by time block |
| **Geo experiment** | Use different geographic areas as groups | Marketing campaign in selected cities |
| **Cluster-randomized test** | Randomize groups instead of individuals | Randomize stores, teams, or merchants |

---

## 28. A/B test vs multivariate test

### A/B test

Compares complete versions.

Example:

- Version A: current landing page
- Version B: redesigned landing page

### Multivariate test

Tests combinations of several page elements.

Example:

- headline A or B
- image A or B
- button A or B

Because there are more combinations, multivariate tests usually need more traffic.

---

## 29. One-tailed vs two-tailed tests

### Two-tailed test

Checks whether Treatment is different from Control in either direction.

Treatment could be better or worse.

### One-tailed test

Checks only one pre-defined direction.

Example:

> We are only testing whether Treatment increases conversion.

The direction must be chosen before seeing the results.

In many business situations, a two-tailed test is safer because unexpected harm also matters.

---

## 30. Which statistical test should we use?

The correct test depends on the type of metric.

| Metric type | Example | Common method |
|---|---|---|
| **Binary / rate** | conversion, activation, fraud flag | two-proportion z-test, logistic regression |
| **Continuous** | checkout time, AHT, transaction value | Welch/two-sample t-test, regression, robust methods |
| **Count** | number of purchases or contacts | Poisson or negative-binomial models |
| **Categorical** | channel or reason category | chi-square or categorical models |
| **Time-to-event** | time to churn or time to activation | survival analysis |

You do not need to memorize all of these at first.

The key idea is:

> Match the statistical method to the kind of metric you are analyzing.

---

## 31. Do the data need to be perfectly normal?

No.

This is a common misunderstanding.

For continuous metrics such as checkout time or transaction value, analysts should look at:

- skewness
- outliers
- sample size
- variance
- mean and median

With large samples, some statistical tests are fairly robust even when raw data are not perfectly normal.

For very skewed data, it may also be useful to use:

- median
- transformations
- bootstrap methods
- robust methods
- non-parametric tests

The goal is not to force every dataset to look normal. The goal is to choose a method that fits the metric and the business question.

---

## 32. What are confounding variables?

A confounding variable is something else that could affect the result.

Examples:

- a marketing campaign starts during the experiment
- a system outage affects one group more than the other
- pricing changes
- holiday traffic
- staffing changes
- a new policy launches at the same time

Randomization helps reduce confounding, but operational problems can still happen.

Always ask:

> Was anything else happening that could explain the result?

---

## 33. Why is A/B testing stronger than a simple before/after comparison?

Suppose conversion improves after a new feature launches.

A before/after comparison might show:

Before = 70%  
After = 74%

But many other things could have changed at the same time:

- seasonality
- customer mix
- marketing activity
- pricing
- traffic volume

In a well-run randomized A/B test, Control and Treatment run at the same time.

That makes it easier to isolate the effect of the Treatment itself.

This is why randomized experiments can provide stronger causal evidence.

---

## 34. When should we NOT use an A/B test?

A standard A/B test may not be practical when:

- there are too few users
- everyone must receive the change at the same time
- users strongly influence each other
- random assignment would create legal or ethical problems
- the change could create unacceptable risk
- the result takes too long to observe
- the Treatment cannot be isolated

Other methods may work better, such as:

- pre/post analysis
- matched Control groups
- difference-in-differences
- interrupted time series
- geo experiments
- switchback experiments

---

## 35. Common A/B testing mistakes

Watch for these problems:

1. No clear business question
2. Choosing the primary KPI after seeing the results
3. Too little data
4. Broken randomization
5. Sample Ratio Mismatch
6. Missing or inconsistent tracking
7. Customers appearing in both groups
8. Stopping the test too early
9. Looking at too many metrics or segments
10. Ignoring guardrails
11. Reporting only the p-value
12. Confusing statistical significance with business value
13. Ignoring implementation cost or risk

---

## 36. A simple decision framework

At the end of an A/B test, answer these questions in order:

1. **What business decision were we testing?**
2. **Was the experiment set up correctly?**
3. **What happened to the primary KPI?**
4. **How large was the difference?**
5. **How confident are we in that difference?**
6. **Did any guardrail metric get worse?**
7. **Did important customer groups react differently?**
8. **What does the result mean for the business?**
9. **What should we do next?**

---

## 37. Quick glossary

| Term | Simple meaning |
|---|---|
| **Control** | Current experience |
| **Treatment** | New experience being tested |
| **Randomization** | Randomly assigning users to groups |
| **Primary KPI** | Main success metric |
| **Guardrail** | Metric that protects against unintended harm |
| **Baseline** | Current level of performance |
| **Lift** | Difference between Treatment and Control |
| **MDE** | Smallest effect the experiment is designed to detect |
| **Power** | Ability to detect a real effect |
| **Alpha** | Pre-defined false-positive risk threshold |
| **P-value** | Evidence used to judge whether a difference may be due to random variation |
| **Confidence interval** | Range showing uncertainty around the estimated effect |
| **SRM** | Warning that the observed group split differs unexpectedly from the planned split |
| **Segmentation** | Checking results for different customer or business groups |
| **Contamination** | A user is exposed to the wrong experiment experience |
| **Confounder** | Another factor that may influence the result |

---

## 38. How this page connects to the rest of the module

Use this page when you want to understand the concepts in plain language.

Then move to:

- `methodology.md` — the step-by-step analytical process
- `case_study/business_case.md` — the NovaPay business scenario
- `notebooks/guided_ab_test_analysis.ipynb` — a worked example
- `notebooks/challenge_ab_test_analysis.ipynb` — independent practice
- `templates/stakeholder_readout_deck.md` — how to present results to stakeholders

The main principle to remember is:

> **Start with the business question, make sure the experiment is trustworthy, measure the impact, check for harm, and end with a clear recommendation.**
