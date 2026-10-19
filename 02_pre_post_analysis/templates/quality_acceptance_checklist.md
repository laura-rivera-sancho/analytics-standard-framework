# Launch Impact Assessment — Quality and Acceptance Checklist

Use this checklist to review a pre/post impact assessment when a randomized Control group is unavailable. The package is decision-ready only when every required area is addressed or an exception is documented and accepted by the decision owner.

## Required evidence

| Review area | Acceptance evidence |
|---|---|
| Business framing | Decision, owner, action options, success measures, risk signals, and causal risks are explicit |
| Analytical population | Raw-to-clean counts reconcile; duplicates, categories, missing fields, durations, and exclusions are documented |
| Timing | Intervention, pre, ramp, post, stable-post, and concurrent-event periods are derived from dates and reviewed |
| KPI comparison | Primary, secondary, and guardrail measures are reported consistently with absolute and relative changes |
| Trend and seasonality | Daily trends, baseline movement, weekday patterns, volume, and intervention alignment are inspected |
| Mix and confounding | Important country, device, tenure, risk, and campaign shifts are quantified and interpreted |
| Secondary outcomes | Skewed duration measures, mechanism metrics, guardrails, and rare-event counts receive appropriate treatment |
| Adjusted analysis | Interrupted-time-series specification, covariates, immediate level change, slope change, and limitations are documented |
| Business impact | Assumptions, scenario math, uncertainty, and the difference between observed and causal impact are explicit |
| Recommendation | Continue, iterate, rollback, or validate further is tied to an owner, monitoring plan, and next decision |

## Readiness assessment

- **Ready for decision-owner review:** all critical evidence is present, results reconcile, causal confidence is calibrated, and the recommendation is actionable.
- **Ready with conditions:** the direction is useful, but named data, design, governance, or monitoring gaps must be resolved before action.
- **Not ready:** population, timing, metric, confounding, or reconciliation problems could materially change the conclusion.

## Reviewer notes

A strong impact assessment demonstrates humility around causality. Model complexity is not the goal; the review should make clear what changed, how credible the evidence is, what could still explain the result, and which action is justified now.
