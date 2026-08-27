# Ad Hoc Analysis Fundamentals

Ad hoc analysis is not unstructured analysis. It is a disciplined response to an urgent, ambiguous question whose decision, scope, and evidence needs are not yet standardized. The analyst's job is to make the problem smaller, protect the metric definition, test the highest-value explanations, and stop with a clear decision handoff.

## Begin with a decision contract

Before opening a notebook, capture:

- the decision and decision owner
- the deadline and analysis timebox
- the primary KPI, numerator, denominator, and time zone
- the comparison period and why it is comparable
- the minimum material change worth action
- known launches, incidents, campaigns, and data changes
- allowed actions and required approvers
- the stopping rule and unresolved-question log

A question such as “Why is conversion down?” becomes: “By 15:00, determine whether checkout completion for August 10–16 declined materially versus August 3–9, identify the funnel stage and operational segment contributing most, and recommend mitigation or further validation.”

## Use a KPI tree before slicing

OrbitMart checkout completion can be expressed as:

`orders / checkout starts = attempt rate × approval rate × post-approval completion rate`

This identity limits the first diagnostic branch. If approval rate moves while the other two remain stable, drilling into payment-related dimensions is higher value than exploring every available attribute.

## Separate rate and mix

An overall KPI can change because:

- performance changed within one or more segments
- the population mix shifted toward historically different segments
- both occurred

The reference workflow reports both within-segment and mix effects. A segment with a large rate drop but tiny current share may not explain much of the overall movement; a high-volume segment with a modest decline may matter more.

## Control exploratory risk

Every additional slice increases the chance of finding noise. Use pre-specified dimensions tied to the KPI tree, require minimum denominators, report all tested segments, adjust p-values across each family of comparisons, and combine statistical evidence with a practical threshold.

The reference marks a decline only when it is at least two percentage points, has at least 300 checkout starts in each period, and has a Benjamini–Hochberg q-value below 0.05.

## Use an evidence ladder

1. **Fact:** directly observed and definition-stable, such as the 0.97 pp completion decline.
2. **Diagnostic evidence:** localization or decomposition, such as payment approval driving the KPI-tree movement.
3. **Supported hypothesis:** consistent with multiple signals, such as Android 8.4 wallet traffic being the affected interaction.
4. **Causal conclusion:** requires an incident mechanism, experiment, rollback response, or other credible design.
5. **Speculation:** plausible but unsupported; document it without presenting it as a finding.

## Timeboxing and stopping rules

Stop when the decision can be made, the agreed timebox expires, data quality invalidates the result, or the next question requires a different owner or method. A useful stopping rule is: confirm the headline, isolate one material stage, identify a decision-relevant segment, quantify impact, triangulate one independent operational signal, and define the next validation.

## Common failure modes

- changing metric definitions mid-analysis
- comparing incomplete or seasonally mismatched periods
- exploring every dimension without a hypothesis map
- reporting small segments or unadjusted significance as discoveries
- confusing composition shifts with within-segment deterioration
- treating correlation or release timing as proof of causation
- estimating impact with an inconsistent denominator or value basis
- hiding inconclusive branches and unresolved data issues
- continuing analysis after the decision is already supported
- delivering charts without an owner, action, or follow-up test

## Review questions

- Is the primary question answerable within the timebox?
- Are KPI definitions and comparison periods stable and explicit?
- Did the KPI tree constrain the first diagnostic branches?
- Are sample-size, multiple-comparison, and materiality controls visible?
- Can the headline change be reconciled to segment contributions?
- Are facts, hypotheses, causal claims, and unknowns labeled correctly?
- Does the output name an action, owner, deadline, and measurement plan?
