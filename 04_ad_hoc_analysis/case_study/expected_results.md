# OrbitMart Ad Hoc Diagnostic Expected Results

These deterministic results use seed 505 and the repository reference workflow. Material differences indicate a changed generator, metric definition, comparison window, or dependency.

## Data-quality reconciliation

| Check | Reference result |
|---|---:|
| Raw rows | 4,806 |
| Duplicate grain rows | 19 |
| Missing acquisition channels | 25 |
| Lowercase country values | 12 |
| Negative checkout starts | 6 |
| Invalid funnel sequences | 12 |

## Headline comparison

| Metric | Prior week | Current week | Change |
|---|---:|---:|---:|
| Checkout starts | 25,941 | 26,173 | +0.9% |
| Completed orders | 22,588 | 22,536 | −0.2% |
| Checkout completion | 87.07% | 86.10% | **−0.97 pp** |
| Payment approval | 91.55% | 90.59% | **−0.96 pp** |
| Revenue | $1.382M | $1.376M | −$6.0K observed |
| Checkout support contacts | 197 | 290 | **+47.2%** |

## KPI-tree conclusion

Attempt rate changes by −0.05 pp and post-approval completion changes by −0.01 pp. Payment approval changes by −0.96 pp and explains the diagnostic direction. The component rates multiply back to the headline completion rate in both periods.

## Segment evidence

| Dimension | Most important segment | Prior | Current | Change | Within effect |
|---|---|---:|---:|---:|---:|
| Platform | Android | 86.64% | 84.28% | −2.35 pp | −0.86 pp |
| App version | Android 8.4 | 87.10% | 79.86% | **−7.24 pp** | **−1.04 pp** |
| Payment method | Digital wallet | 88.78% | 86.36% | **−2.41 pp** | **−0.80 pp** |
| Country | Mexico | 87.11% | 85.57% | −1.54 pp | −0.40 pp |

Android 8.4 and digital wallet meet the materiality and false-discovery-rate criteria. Traffic-mix effects are small relative to within-segment deterioration. Acquisition channels decline broadly but do not localize the mechanism.

## Business impact

Applying the prior-week completion rate to the current 26,173 checkout starts yields 22,790 expected orders. The observed 22,536 implies an estimated gap of **254 orders**. At the prior average order value of $61.16, the estimated revenue gap is **$15.5K**.

This counterfactual is a planning estimate, not a causal loss calculation.

## Evidence-calibrated conclusion

- **Fact:** checkout completion declined materially while starts increased.
- **Diagnostic evidence:** payment approval is the only materially changing KPI-tree stage.
- **Supported hypothesis:** the issue concentrates in Android 8.4 digital-wallet traffic, especially in Mexico and Brazil, and support demand increased.
- **Unknown:** whether the release, wallet processor, or their interaction caused the decline.
- **Action:** pause expansion, inspect logs and incident signatures, apply a reversible mitigation, and monitor recovery against unaffected cohorts.
