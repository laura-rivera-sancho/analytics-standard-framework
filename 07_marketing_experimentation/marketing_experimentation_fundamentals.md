# Marketing Experimentation Fundamentals

Marketing experimentation uses controlled assignment to estimate what changes because of a message, offer, channel, or experience. The objective is not to find the smallest p-value. It is to make a better decision under uncertainty while protecting customers, economics, and measurement integrity.

## Start with the decision and estimand

An experiment should begin with:

- the decision and decision owner
- the eligible population
- the treatment and comparison conditions
- the randomization unit
- the outcome window
- the primary estimand
- the practical minimum worth acting on
- guardrails and stop rules
- the action authorized by each possible result

An **estimand** states the effect being estimated. For example: “the intention-to-treat difference in 14-day completed-purchase rate between customers assigned to lifecycle-informed email and customers assigned to the current reminder.”

Clear estimands prevent the analysis from shifting among delivered, opened, clicked, and assigned populations after results are visible.

## Why randomization matters

Random assignment makes treatment groups comparable in expectation on observed and unobserved pre-treatment characteristics. Outcome differences can then estimate causal effects when assignment is implemented correctly, interference is limited, and measurement is consistent.

Randomization does not automatically protect against:

- broken assignment or exposure logging
- treatment contamination
- selective exclusions after assignment
- incomplete outcome windows
- repeated peeking and optional stopping
- attrition that differs by treatment
- measurement changes during the test
- interference between customers

## Split tests and multivariate tests

### A/B or split test

A split test compares two randomized conditions, often control and one treatment. It is easy to communicate and usually provides more power per comparison than dividing the same population across many variants.

### A/B/n test

An A/B/n test compares several complete variants. It answers which bundled experience performs best but cannot cleanly attribute the result to individual components when each variant changes several things.

### Factorial multivariate test

A factorial design varies multiple **factors**, each with defined **levels**. A `2 × 2 × 2` design has three two-level factors and eight treatment cells.

Factorial designs can estimate:

- **main effects:** the average effect of changing one factor across the levels of the other factors
- **interaction effects:** whether the effect of one factor depends on another factor's level

A full factorial observes every combination. A fractional factorial uses only a structured subset to reduce sample requirements, but some effects become aliased and cannot be separated without assumptions.

## Main effects and interactions

Suppose a discount improves conversion when used with email only but reduces contribution margin when combined with email plus SMS. The offer and channel plan interact: the effect of the offer depends on channel plan.

When interaction is material, a main effect alone may hide the decision-relevant pattern. However, interaction estimates require more information and often have lower power. Prespecify a small number of plausible interactions tied to the business mechanism.

Avoid interpreting every cell difference as a separate independent discovery. Cell comparisons, main effects, and interactions belong to declared hypothesis families.

## Control and holdout choices

A current-policy control estimates improvement relative to what the business would otherwise do. A no-contact holdout estimates incremental effect relative to no campaign. Both can be useful, but they answer different questions.

In a factorial marketing test, all active cells may receive some campaign. A separate no-contact holdout is therefore needed when the decision requires evidence that campaigning is better than doing nothing. Customer harm, fairness, operational policy, and opportunity cost should inform holdout design.

## Randomization unit and interference

Choose the unit at which treatment can be kept independent:

- customer for direct messaging
- household when household members may share the treatment
- store, geography, or market when campaigns spill across individuals
- time block for operational policies that cannot alternate at user level

Randomizing customers while delivering a shared household offer can create interference. Cluster randomization may be more appropriate, but the effective sample size falls because units within a cluster are correlated.

## Eligibility, consent, and exclusions

Define eligibility before randomization. Typical rules include active identity, valid channel consent, suppression lists, contact-frequency caps, geographic eligibility, and absence of a recent purchase.

Post-assignment exclusions can break randomization. Remove a customer after assignment only under a prespecified rule unrelated to treatment outcome, and show the reconciliation from assigned to analyzed populations.

Consent is not a modeling feature to work around. A channel factor that includes SMS can be randomized only among customers eligible for SMS. Results then generalize to that eligible population, not automatically to email-only customers.

## Intention to treat and treatment on the treated

**Intention-to-treat analysis** compares customers according to assignment. It preserves the randomized comparison and estimates the effect of the policy as implemented, including imperfect delivery or engagement.

Comparing only customers who opened, clicked, or received the message usually reintroduces selection bias because engagement is affected by customer behavior and possibly treatment. Treatment-on-the-treated effects require additional assumptions or an appropriate instrumental-variable design; they should not replace the primary intention-to-treat result casually.

## Metrics hierarchy

### Primary metric

The single main outcome used for the principal decision. It should be sensitive to treatment, difficult to game, and measured consistently.

### Secondary metrics

Additional outcomes that explain mechanism or business value. They support interpretation but should not silently replace a failed primary outcome.

### Guardrails

Outcomes that protect customers, operations, risk, or long-term economics. Examples include unsubscribes, complaints, refunds, margin, frequency-cap violations, and deliverability.

### Diagnostic metrics

Delivery, open, and click measures help explain the treatment path. They are often intermediate outcomes and should not be confused with the final business objective.

## Denominators and outcome windows

Define every metric's numerator, denominator, clock, and time zone. For intention-to-treat conversion, the denominator is assigned eligible customers, not message opens or successful deliveries.

Use the same fixed follow-up window for every assigned customer. Ending the experiment on a calendar date can leave later assignments with less observation time. Either wait for the final cohort to mature or exclude immature assignments under a rule declared before outcome analysis.

## Effect size

For a binary outcome:

- **absolute effect:** treatment rate minus control rate, usually expressed in percentage points
- **relative lift:** absolute effect divided by control rate

Absolute effects connect directly to incremental outcomes and capacity. Relative lift provides context but can appear large when the baseline is small. Report the effect estimate, confidence interval, sample sizes, and baseline—not only a p-value.

Business impact should use an internally consistent denominator:

`incremental outcomes = eligible rollout population × absolute effect`

Then incorporate revenue, variable cost, offer subsidy, message cost, refunds, and uncertainty to estimate incremental contribution margin.

## Confidence intervals and hypothesis tests

A confidence interval describes the range of effect sizes compatible with the data and method under repeated sampling assumptions. A p-value measures how surprising the observed result would be under a specified null model. It is not the probability that the hypothesis is true and does not measure business value.

Large samples can make trivial effects statistically significant. Small samples can leave valuable effects uncertain. Use statistical evidence together with a prespecified practical threshold and risk tolerance.

## Power and minimum detectable effect

Power is the probability of detecting a specified effect when it is truly present under the design assumptions. The minimum detectable effect is the smallest effect the planned sample can detect at the chosen significance and power.

Sample planning depends on:

- baseline rate or variance
- practical minimum effect
- significance level and sidedness
- desired power
- allocation ratio
- number of arms or factors
- multiplicity plan
- clustering or repeated measures
- expected ineligibility, attrition, and incomplete windows

Power should be planned before outcomes are observed. “Observed power” calculated after the test adds little beyond the confidence interval.

Factorial main effects pool multiple cells and can be more precisely estimated than individual cell contrasts. Interaction effects and pairwise cell comparisons usually require more sample. State which estimands the design is actually powered to support.

## Sample-ratio mismatch

Sample-ratio mismatch occurs when observed assignment counts differ implausibly from planned allocation. It can signal broken randomization, logging loss, eligibility applied after assignment, bot filtering, or pipeline errors.

The check should use assigned counts and the planned probabilities. A failed check is a validity alarm, not a metric to “adjust away.” Investigate by time, platform, source, and assignment path before interpreting treatment effects.

## Covariate balance and stratification

Randomized groups will not match exactly by chance. Balance tables are useful diagnostics, but testing many baseline differences and excluding imbalanced variables can create new bias.

Stratified randomization can improve balance for a small set of high-value predictors such as lifecycle segment or value band. The analysis should reflect the randomization design. Prespecified regression adjustment or variance-reduction methods can improve precision without changing the estimand.

## Variance reduction

Pre-treatment covariates correlated with the outcome can reduce uncertainty. Common approaches include regression adjustment and CUPED-style use of a pre-period measure.

Controls must be measured before treatment and selected without looking at post-treatment outcomes. Variance reduction does not rescue a broken experiment, change the business meaning of the effect, or justify unsupported subgroup searches.

## Multiple comparisons

Testing many hypotheses increases the chance of at least one false positive.

- **Family-wise error rate** controls the probability of any false rejection in a family. Holm's method is a flexible step-down procedure for a limited confirmatory family.
- **False discovery rate** controls the expected share of false discoveries among rejected hypotheses. Benjamini–Hochberg is useful for clearly labeled exploratory families.

Define families according to the decision. Primary effects, guardrails, interactions, and exploratory segments may require different handling. Do not place every metric into one arbitrary family or leave the family undefined until results are known.

## Sequential testing and peeking

Repeatedly checking a fixed-horizon p-value and stopping when it becomes significant inflates false positives. Options include:

- wait for the planned sample and mature outcome window
- use prespecified group-sequential boundaries
- use an always-valid sequential method
- stop only for operational or safety rules that are separate from efficacy claims

Dashboards can monitor data quality and critical harm signals without authorizing unplanned efficacy decisions.

## Segment and heterogeneous-effect analysis

Prespecified segment analysis can answer whether treatment effects differ across lifecycle group, value band, or another credible moderator. The relevant evidence is an interaction test, not “significant in one segment and not significant in another.”

Post-hoc segments are hypothesis-generating. Report all tested segments, apply appropriate multiplicity controls, require adequate sample, and validate promising patterns in a new experiment.

## Common threats to validity

- assignment after exposure or outcome
- duplicate or changing assignments
- cross-arm contamination
- missing or unequal outcome windows
- selective delivery-based analysis
- novelty and learning effects
- seasonality or concurrent campaigns
- spillovers between customers
- instrumentation changes during the test
- differential attrition
- unplanned peeking
- choosing the winning metric after viewing results
- stopping when budget, not the declared sample, happens to run out

## Full experiment workflow

1. Frame the decision, estimand, and authorized actions.
2. Define population, consent, unit, treatment, control, metrics, and guardrails.
3. Set baseline, practical minimum, power, sample, duration, and multiplicity plan.
4. Create and freeze deterministic assignment before exposure.
5. Validate assignment, consent, timestamps, duplication, and sample ratio.
6. Wait for complete outcome windows.
7. Estimate intention-to-treat effects and confidence intervals.
8. Apply multiplicity controls to the declared families.
9. Evaluate interactions, business value, and guardrails.
10. Recommend rollout, iteration, more evidence, or no change.
11. Monitor the staged decision and retain a rollback trigger.

## Common failure modes

- changing the primary metric after seeing results
- reporting only relative lift
- using opens as the denominator for purchase conversion
- selecting the best of many variants without multiplicity control
- interpreting a main effect while ignoring a strong interaction
- declaring segments different because only one has a low p-value
- treating statistical significance as positive economics
- excluding delivery failures from the primary analysis
- ignoring consent or contact-pressure constraints
- generalizing beyond the randomized eligible population
- recommending broad rollout without a staged monitor and stop rule

## How to explain the A7 design in an interview

Use a concise structure:

1. **Problem:** A lifecycle analysis identified a governed retention audience, but historical campaign performance could not identify incremental impact.
2. **Design:** Start with a two-arm message test, then use a full `2 × 2 × 2` factorial design for message, offer, and channel plan plus a no-contact holdout.
3. **Integrity:** Randomize at customer grain, freeze assignment before exposure, use intention to treat, check sample ratio and timestamps, and preserve complete 14-day windows.
4. **Inference:** Report absolute effects and confidence intervals, prespecify interactions, and control multiplicity according to decision families.
5. **Decision:** Require practical lift, positive contribution margin, and acceptable consent, opt-out, complaint, and refund guardrails before staged rollout.

## Practice interview questions

### When would you use a factorial test instead of an A/B/n test?

Use a factorial test when the business needs to learn the contribution of individual components and plausible interactions. Use A/B/n when the bundled experiences are the decision units or when operational constraints prevent independent factor variation.

### Why include a no-contact holdout?

Comparisons among active treatments identify which treatment performs better, but not whether campaigning creates incremental value relative to no campaign. A holdout provides that baseline when it is ethical and operationally acceptable.

### What is sample-ratio mismatch?

It is an implausible difference between planned and observed assignment counts. It can indicate broken randomization, logging loss, or post-assignment filtering, so I investigate it before interpreting outcomes.

### Why use intention to treat?

It preserves the randomized comparison and estimates the effect of the assignment policy under real delivery and engagement behavior. Conditioning on opens or clicks selects on post-treatment behavior and can bias the result.

### How do you handle many variants and metrics?

I define confirmatory hypothesis families before the test, keep one primary decision metric, use Holm or another family-wise procedure for rollout claims, and use false-discovery control for clearly labeled exploratory analysis.

### What if conversion improves but margin declines?

The treatment fails the business-value gate. A discount can buy conversions that destroy contribution margin. I would retain or redesign the treatment rather than recommend it from conversion alone.

### How do you compare segment effects?

I test the treatment-by-segment interaction. A significant result in one segment and a nonsignificant result in another does not itself prove the effects differ.

### How would you monitor a rollout?

Use a staged allocation with fixed owners, data-quality checks, the same outcome and guardrail definitions, predefined rollback thresholds, and a scheduled decision review. I would not continuously reinterpret ordinary fixed-horizon p-values.

## Review checklist

- Is the decision and primary estimand explicit?
- Are eligibility, consent, randomization unit, and assignment timing governed?
- Is the sample powered for the effects and interactions being claimed?
- Are primary, secondary, guardrail, and diagnostic metrics separated?
- Do denominators and outcome windows match the intention-to-treat design?
- Did sample ratio, duplication, timestamps, and observation maturity pass validation?
- Are absolute effects, uncertainty, multiplicity, and practical thresholds visible?
- Are interaction and segment claims supported by direct tests?
- Does the recommendation include contribution margin, customer risk, monitoring, and rollback?
