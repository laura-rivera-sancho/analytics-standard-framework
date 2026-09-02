# Marketing Experimentation Methodology

## Purpose

This methodology defines a reusable, decision-focused workflow for randomized marketing experiments. It covers a two-arm split test and a full `2 × 2 × 2` factorial test with a no-contact holdout. The workflow protects assignment integrity, consent, fixed outcome windows, multiplicity, contribution margin, and customer-experience guardrails before any rollout recommendation.

## 1. Write the experiment charter

Before generating assignments, record:

- decision, decision owner, and authorized actions
- target population and exclusions
- treatment and comparison conditions
- randomization unit and allocation probabilities
- primary estimand and outcome window
- baseline, practical minimum, power, and significance plan
- secondary, guardrail, and diagnostic metrics
- hypothesis families and multiplicity method
- duration, maturity date, stop rules, and review date
- consent, suppression, frequency-cap, and privacy requirements

The reference estimand is an intention-to-treat difference among eligible assigned customers. Delivery, opens, and clicks do not redefine the primary population.

## 2. Define the population before assignment

The reference population begins with At Risk and Needs Attention customers from the A6 lifecycle framework. Eligibility is evaluated before randomization.

The split test requires valid email consent. The factorial test includes an email-plus-SMS factor, so every factorial customer must be eligible for both channels. That restriction protects the experiment but limits generalization to dual-consented customers.

Pre-assignment exclusions include:

- invalid or unresolved customer identity
- missing lifecycle segment or value band
- absent required channel consent
- suppression or contact-frequency-cap conflict
- qualifying purchase inside the recent-purchase exclusion window
- assignment to another conflicting retention experiment

## 3. Plan power and minimum detectable effect

Use a two-sided significance level and prespecified power. Calculate the required sample from the baseline rate and the smallest absolute effect worth acting on. Add expected data loss only for exclusions that occur before assignment or for unavoidable immature windows; do not inflate and then remove customers based on delivery or engagement.

For the factorial test, document power separately for:

- pooled main effects
- active-cell comparisons with holdout
- prespecified two-way interactions
- exploratory three-way or segment interactions

The reference generator balances assignment exactly before defects. The final analysis will recalculate detectable effects from the validated sample rather than claiming the design supports every possible contrast.

## 4. Randomize and freeze assignment

Randomize at customer grain with a deterministic seed. Use stratification by lifecycle segment and value band when it improves precision or operational balance. Assignment must precede exposure and outcome measurement.

The split test uses equal allocation between the current reminder and lifecycle-informed message. The factorial test uses equal allocation across eight active cells and a no-contact holdout in the synthetic reference design. Production allocation could differ, but the planned probability must be recorded for sample-ratio validation.

## 5. Preserve an auditable event sequence

Required timestamps include assignment, first exposure, conversion when present, and the date the outcome window matures. Use event time for experiment logic and record extraction time separately.

Valid sequence:

`eligibility → assignment → exposure → outcome → outcome maturity → analysis`

A delivery failure is not a reason to remove a randomized customer from intention-to-treat analysis. An exposure before assignment or a conversion before assignment is a critical integrity defect and is quarantined.

## 6. Validate before reading effects

The validation gate reports:

- duplicate assignment identifiers
- duplicate customer assignment within an experiment
- missing identifiers, lifecycle segment, or value band
- invalid experiment, arm, factor, or holdout combinations
- missing required consent
- exposure or conversion before assignment
- conversion flags inconsistent with timestamps or value
- assignments whose 14-day outcome window has not matured
- observed assignment counts versus planned allocation

Raw, excluded, and analyzed row counts must reconcile. Critical defects block effect estimation until resolved or quarantined under a documented rule.

## 7. Check randomization integrity

Run a chi-square sample-ratio-mismatch test against planned arm probabilities using assigned counts before treatment-based filtering. Review allocation by assignment date and randomization stratum when the overall test fails.

Profile a small set of prespecified pre-treatment characteristics using standardized differences. Exact equality is not required; the purpose is to identify implementation defects and describe chance imbalance, not to search for variables that justify selective exclusions.

## 8. Estimate split-test effects

For each arm, report assigned customers, conversions, conversion rate, recognized revenue, contribution margin, and guardrail rates.

For the primary binary outcome, report:

- absolute difference in percentage points
- relative lift versus control
- two-sided confidence interval
- p-value under the prespecified test
- practical-threshold comparison

The primary conclusion uses intention to treat. Delivery and click diagnostics are secondary mechanism evidence.

## 9. Estimate factorial effects

Encode the active factorial levels transparently and estimate:

- average main effects for message, offer, and channel plan
- message × offer interaction
- offer × channel-plan interaction
- each active cell versus no-contact holdout

Use a model appropriate to the outcome and report effects on an interpretable scale. For binary conversion, a linear probability model can communicate percentage-point contrasts while robust standard errors protect inference; a logistic model can serve as a sensitivity analysis. Cell summaries must reconcile to modeled assignments.

Do not interpret a pooled main effect without checking prespecified interactions. A material interaction means the factor's effect depends on another factor's level.

## 10. Control multiple comparisons

Define families before outcome review:

- one primary split-test effect
- three factorial main effects and two prespecified interactions
- eight active-cell versus holdout contrasts
- critical guardrails
- exploratory segment interactions

Use Holm adjustment for limited confirmatory rollout families. Use Benjamini–Hochberg only for clearly labeled exploratory families. Report raw and adjusted p-values together with effect sizes; adjustment does not replace business judgment.

## 11. Calculate contribution margin

For each assigned customer:

`contribution margin = recognized revenue − product cost − discount cost − shipping subsidy − messaging cost − refund impact`

The reference data store each component separately so assumptions can be inspected. Estimate incremental margin per assigned customer and projected rollout margin using the same eligible-population denominator as the treatment effect.

Positive conversion lift with negative incremental margin fails the business-value gate.

## 12. Review guardrails

Evaluate unsubscribe, complaint, SMS opt-out, refund, consent-violation, and contact-policy outcomes. Use absolute rates and differences, not only significance tests. A rare but severe policy violation can block rollout even when statistical uncertainty is high.

Guardrail thresholds and severity are defined before the decision meeting. Critical consent or suppression failures are operational defects, not acceptable tradeoffs for lift.

## 13. Handle segment analysis carefully

Prespecify lifecycle segment and value band as the primary heterogeneity candidates. Test treatment-by-segment interactions directly. “Significant in one group and not significant in another” does not establish different effects.

Post-hoc segments are exploratory, require adequate sample and multiplicity control, and generate hypotheses for a new experiment rather than immediate targeting rules.

## 14. Make the decision

A staged rollout requires:

- valid assignment, timestamps, consent, and mature windows
- a primary effect that meets statistical and practical criteria
- positive incremental contribution margin
- no critical guardrail breach
- no dependence on an unsupported post-hoc subgroup
- named monitoring owner, review date, and rollback trigger

Otherwise recommend the current policy, a redesigned treatment, or more evidence. Selecting whichever cell has the largest observed rate is not a valid fallback.

## 15. Monitor and preserve learning

Archive the experiment charter, assignment table, code version, data-quality report, estimands, effect table, adjusted comparisons, and decision. A rollout should retain the same metric definitions and monitor data quality, conversion, margin, unsubscribe, complaint, refund, and opt-out signals.

Future experiments should reference prior results without treating them as guaranteed priors in a changed population or season.

## Reference implementation boundary

The portfolio uses synthetic customer-level records and local Python. It demonstrates design and analytical controls rather than campaign delivery, identity resolution, or production experimentation infrastructure. A production system would add authenticated assignment services, immutable exposure logs, channel integrations, durable storage, access enforcement, orchestration, alert delivery, and a registered experiment catalog.
