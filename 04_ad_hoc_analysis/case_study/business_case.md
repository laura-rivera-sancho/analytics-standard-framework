# OrbitMart Checkout Completion Diagnostic Business Case

OrbitMart is a fictional e-commerce marketplace operating in the United States, Mexico, Brazil, and Costa Rica. On Monday morning, the commerce director reports that completed orders appear down despite normal traffic and asks Analytics for an explanation before the afternoon incident review.

All organizations, records, operational events, and monetary values in this case are synthetically generated for portfolio demonstration.

## Decision request

By 15:00, determine whether checkout completion for August 10–16 declined materially versus the matched prior week, identify the most important diagnostic branch, estimate the business impact, and recommend immediate mitigation or further validation.

## Analysis contract

| Item | Definition |
|---|---|
| Decision owner | Director of Commerce |
| KPI | Completed orders divided by checkout starts |
| Current period | 2026-08-10 through 2026-08-16 |
| Comparison | 2026-08-03 through 2026-08-09 |
| Materiality | At least 0.50 percentage points overall |
| Drill-down rule | Pre-specified operational dimensions; at least 300 starts per period |
| Statistical guardrail | Benjamini–Hochberg q-value below 0.05 plus at least 2 pp segment decline |
| Timebox | Four analyst hours |
| Stopping rule | Stable headline, isolated funnel stage, material segment, impact estimate, operational triangulation, and assigned next action |

## KPI tree

Checkout completion equals the product of:

1. payment attempts divided by checkout starts
2. payment approvals divided by payment attempts
3. completed orders divided by payment approvals

## Pre-specified hypotheses

| Hypothesis | Diagnostic evidence | Possible action |
|---|---|---|
| Traffic composition shifted | Channel or country mix effect | Adjust interpretation; no product rollback |
| Customers are abandoning before payment | Attempt rate falls | Inspect checkout experience and performance |
| Payments are being rejected | Approval rate falls by method, platform, or version | Escalate processor or release mitigation |
| Approved payments fail to become orders | Post-approval completion falls | Inspect order-creation and inventory services |
| The KPI movement is a data artifact | Freshness, duplicates, funnel violations, or definition change | Pause decision and repair measurement |

## Known operational context

Android 8.4 entered a 15% pilot in Mexico and Brazil during the comparison week and expanded to about 82% in the current week. A digital-wallet support alert was also opened during the current period. These are timeline facts, not proof of cause.

## Reference recommendation

Treat the decline as real and operationally material. Pause further Android 8.4 expansion for Mexico and Brazil, route or disable the affected digital-wallet flow if Operations confirms the error signature, and monitor approval recovery hourly. Preserve Android 8.3 and non-wallet traffic as comparisons. Do not claim the release alone caused the issue until logs or a controlled mitigation distinguish release and processor mechanisms.

## Limitations

- The case and data are synthetic.
- Week-over-week comparison does not by itself establish causality.
- The aggregate grain cannot expose request-level errors or customer retries.
- Android version and wallet usage overlap with country, limiting causal separation.
- The revenue gap uses prior-week average order value and excludes downstream margin effects.
