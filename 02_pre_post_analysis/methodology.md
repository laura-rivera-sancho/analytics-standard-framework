# Pre/Post Analysis Methodology

## Purpose

Use this framework when a business change has been implemented and a randomized Control group is unavailable or not valid. The objective is to estimate how performance changed after the intervention while explicitly testing alternative explanations.

## 1. Frame the business decision

Document:
- What changed?
- Why was it changed?
- What decision will the analysis support?
- What outcome was expected to improve?
- What unintended outcomes must not deteriorate?

The business question should be decision-oriented, for example:

> Did the new verification workflow reduce processing time enough to justify keeping it while maintaining payment quality and fraud controls?

## 2. Define the intervention precisely

Record:
- launch date and time
- rollout scope
- eligible population
- rollout method: immediate, phased, or ramped
- implementation changes during the post period
- known incidents or outages

If adoption was gradual, a single binary pre/post flag may be insufficient.

## 3. Define the analytical population

Specify:
- unit of analysis
- eligibility rules
- exclusions
- geographic/product/channel scope
- whether repeated customers or transactions are allowed
- how partial exposure is handled

Use the same population definition across periods whenever possible.

## 4. Define the pre and post windows

Choose windows based on business behavior rather than convenience.

Check:
- sufficient baseline length
- comparable weekdays/weekends
- holidays
- seasonality
- marketing cycles
- launch ramp-up
- operational stabilization

When useful, define:
- **Pre baseline**
- **Launch/ramp period**
- **Stable post period**

Document why the selected windows are appropriate.

## 5. Define KPIs before interpreting outcomes

### Primary KPI
The main metric tied to the intervention objective.

### Secondary KPIs
Metrics that explain mechanism or supporting value.

### Guardrail KPIs
Metrics that detect unintended harm.

For each KPI document:
- formula
- numerator/denominator when applicable
- grain
- exclusions
- desired direction
- business-relevant threshold when available

Verify that KPI definitions and tracking logic did not change at launch.

## 6. Validate data quality

Check:
- schema and data types
- duplicates
- missing critical fields
- impossible values
- category consistency
- period coverage
- metric construction
- logging/tracking changes
- sudden volume discontinuities

Quantify exclusions and produce a final analytical population.

## 7. Inspect the time series before comparing averages

Plot each major KPI over time and annotate the intervention date.

Look for:
- pre-existing trend
- level shifts
- post-launch trend changes
- weekly cycles
- outliers
- volatility changes
- launch ramp
- outages or special events

Never rely only on a two-row Pre vs Post table when time-series data are available.

## 8. Check population and traffic mix

Compare important characteristics across periods, such as:
- geography
- device
- customer tenure
- product
- channel
- transaction size
- customer risk tier
- traffic source

A material mix shift can move the aggregate KPI without an intervention effect.

## 9. Build a confounder register

Document events that may affect interpretation.

Recommended table:

| Potential confounder | Timing | KPI potentially affected | Evidence | Analytical action |
|---|---|---|---|---|
| Marketing campaign | Post week 2 | Volume / completion | Campaign calendar | Segment or control for period |
| Staffing change | Launch week | Processing time | Ops notes | Treat ramp separately |

Classify each confounder as:
- unlikely to matter
- possible influence
- material limitation

## 10. Select the comparison method

### Simple pre/post comparison
Use when the baseline is stable, windows are comparable, and confounding risk is low.

Report:
- Pre value
- Post value
- absolute change
- relative change
- confidence interval
- statistical evidence where appropriate

### Interrupted Time Series
Prefer when repeated observations are available and trend matters.

A basic segmented model may estimate:

`Outcome_t = β0 + β1(Time_t) + β2(Post_t) + β3(TimeAfter_t) + error_t`

Interpretation:
- `β1`: baseline trend
- `β2`: immediate level change after intervention
- `β3`: change in trend after intervention

Consider autocorrelation, seasonality, and robust errors.

### Difference-in-Differences
Use when a credible non-randomized comparison group exists.

Core idea:

`Impact = (Treatment_Post - Treatment_Pre) - (Comparison_Post - Comparison_Pre)`

Validate the parallel-trends assumption before relying on the estimate.

### Regression / adjusted analysis
Use covariates to account for meaningful observed changes in mix or context. Adjustment improves comparability but does not eliminate unmeasured confounding.

## 11. Quantify the effect

Report:
- baseline value
- post value
- absolute change
- relative change
- confidence interval
- effect size or modeled intervention coefficient
- p-value when relevant

For percentage KPIs, distinguish **percentage-point** change from **relative-percent** change.

## 12. Evaluate robustness

Useful sensitivity checks include:
- alternative pre/post windows
- excluding launch/ramp days
- excluding known outage dates
- weekday-only comparison
- controlling for seasonality
- adjusted vs unadjusted estimates
- median vs mean for skewed metrics
- segment consistency

If the conclusion changes substantially across reasonable specifications, report that instability.

## 13. Segment the impact

Analyze only business-relevant segments.

For each segment show:
- Pre KPI
- Post KPI
- absolute change
- sample/volume
- uncertainty when feasible

Avoid treating every post-hoc segment difference as a confirmed causal effect.

## 14. Translate into business impact

Possible measures:
- hours saved
- incremental completed transactions
- additional customers served
- avoided support contacts
- cost reduction
- reduced manual reviews
- revenue or payment-volume opportunity
- risk/fraud cost

Show assumptions and preferably a plausible range.

## 15. Rate causal confidence

Before writing the recommendation, explicitly assess causal confidence.

### Higher confidence
- stable pre trend
- consistent KPI definitions
- sufficient pre/post duration
- no major concurrent changes
- stable population mix
- time-series or comparison-group evidence supports the result

### Moderate confidence
- some limitations exist but do not obviously explain the full effect

### Low confidence
- major concurrent changes, tracking issues, unstable baseline, short windows, or severe mix shifts

This prevents a statistically significant pre/post difference from being presented as stronger evidence than the design supports.

## 16. Make the recommendation

Standard recommendation categories:

### Continue / Scale
Observed improvement is meaningful, credible, and guardrails are acceptable.

### Continue with monitoring
Positive result, but uncertainty or confounding requires post-launch monitoring.

### Iterate
Direction is promising but implementation or segment performance suggests changes are needed.

### Validate further
Evidence is inconclusive; use a longer post period, stronger quasi-experimental design, or future controlled experiment.

### Roll back / Stop
Performance deteriorated materially or guardrail harm outweighs benefit.

## Executive communication standard

Lead with:
1. business question
2. what changed and when
3. primary result and magnitude
4. strength of evidence / causal-confidence level
5. guardrail impact
6. important confounders or limitations
7. business implication
8. recommendation and monitoring plan

Use cautious causal language unless the design supports stronger inference.