# Harbor & Pine Marketing Experimentation Expected Results

These deterministic reference results use synthetic generator seed `707`, validation as of `2026-10-31`, and the analysis rules in `src/analyze_marketing_experiments.py`. They allow reviewers to confirm that the implementation, notebook, and stakeholder narrative reconcile.

## Population and integrity

- Raw assignments: **26,020**
- Quarantined rows: **78**
- Valid intention-to-treat assignments: **25,942**
- Split-test population: **7,989**
- Factorial population: **17,953**

The quarantine contains 58 distinct source-row defects plus 20 duplicated records. Both experiments pass the `p ≥ 0.01` sample-ratio gate:

| Experiment | Valid assignments | Arms | SRM p-value | Decision |
|---|---:|---:|---:|---|
| Lifecycle-message split test | 7,989 | 2 | 0.955 | Pass |
| Factorial multivariate test | 17,953 | 9 | ~1.000 | Pass |

## Power and sensitivity

| Estimand | Planned practical effect | Required per group | Validated groups | Detectable effect from validated sample |
|---|---:|---:|---:|---:|
| Split treatment versus control | +1.50 pp | 5,848 | 3,992 / 3,997 | 1.83 pp |
| Factorial pooled main effect | +1.20 pp | 8,105 | 7,977 / 7,980 | 1.21 pp |
| Active cell versus holdout | +2.50 pp | 1,891 | 1,992 / 1,996 | 2.43 pp |

The split test is underpowered for its original +1.50 pp planning target after validation. Its confidence interval remains the correct description of what the realized sample supports.

## Split-test result

| Metric | Current reminder | Lifecycle message | Effect | 95% CI | p-value |
|---|---:|---:|---:|---:|---:|
| 14-day conversion | 8.27% | 9.71% | **+1.44 pp** | +0.19 to +2.69 pp | 0.024 |
| Revenue per assigned customer | $8.34 | $9.97 | +$1.63 | −$0.03 to +$3.28 | 0.054 |
| Contribution margin per assigned customer | $4.12 | $4.74 | +$0.63 | −$0.28 to +$1.53 | 0.177 |
| Unsubscribe rate | 0.88% | 0.73% | −0.15 pp | −0.54 to +0.24 pp | 0.448 |
| Complaint rate | 0.15% | 0.15% | ~0.00 pp | −0.17 to +0.17 pp | 0.998 |
| Refund rate | 0.43% | 0.68% | +0.25 pp | −0.07 to +0.57 pp | 0.132 |

Interpretation: the treatment has a statistically credible positive conversion effect, but the observed +1.44 pp effect is slightly below the predeclared +1.50 pp practical threshold. Revenue and margin estimates are positive but uncertain. The result supports continued testing, not automatic rollout.

## Factorial main effects and interactions

Holm adjustment is applied across the three main effects and two prespecified interactions.

| Effect | Estimate | 95% CI | Raw p-value | Holm p-value | Interpretation |
|---|---:|---:|---:|---:|---|
| Benefit-led versus urgency-led message | −0.17 pp | −1.06 to +0.72 pp | 0.714 | 1.000 | No supported main effect |
| 10% discount versus free shipping | **+1.37 pp** | +0.47 to +2.26 pp | 0.0027 | **0.013** | Credible positive main effect |
| Email plus SMS versus email only | +0.35 pp | −0.54 to +1.24 pp | 0.440 | 1.000 | No supported main effect |
| Message × offer | −0.58 pp | −2.37 to +1.20 pp | 0.521 | 1.000 | No supported interaction |
| Offer × channel | −1.28 pp | −3.06 to +0.50 pp | 0.159 | 0.638 | No supported interaction |

The discount factor improves conversion on average relative to free shipping. The synthetic sample does not support a general claim that benefit framing or additional SMS improves conversion.

## Active cells versus no-contact holdout

Holdout conversion is **7.77%**. Only one active cell remains statistically credible after Holm adjustment across eight comparisons:

| Cell | Conversion | Absolute effect | 95% CI | Holm p-value | Incremental margin/customer | Margin 95% CI |
|---|---:|---:|---:|---:|---:|---:|
| Urgency + 10% discount + email only | **10.43%** | **+2.67 pp** | +0.88 to +4.45 pp | **0.027** | +$0.16 | −$1.02 to +$1.33 |
| Benefit + 10% discount + email plus SMS | 9.68% | +1.92 pp | +0.17 to +3.67 pp | 0.223 | +$0.51 | −$0.67 to +$1.69 |
| Urgency + 10% discount + email plus SMS | 9.53% | +1.76 pp | +0.02 to +3.51 pp | 0.285 | +$0.30 | −$0.86 to +$1.46 |
| Benefit + 10% discount + email only | 9.36% | +1.59 pp | −0.14 to +3.33 pp | 0.359 | +$0.33 | −$0.80 to +$1.46 |

Unadjusted intervals for other cells are shown for transparency, but they do not authorize separate discoveries after the declared family-wise correction.

## Guardrails

Every validated arm remains below the declared absolute thresholds for unsubscribe, complaint, SMS opt-out, and refund rates. For the leading urgency + 10% discount + email-only cell:

- unsubscribe: **0.45%** versus 1.50% threshold
- complaint: **0.05%** versus 0.50% threshold
- SMS opt-out: **0.00%** because the arm is email only
- refund: **0.95%** versus 9.00% threshold

Passing a threshold does not prove no harm. Rates and confidence intervals should continue to be monitored during any staged decision.

## Reference recommendation

Advance **urgency-led message + 10% discount + email only** to a controlled margin-validation stage while retaining a no-contact holdout. Do not authorize broad rollout yet.

Rationale:

1. assignment integrity and sample ratio pass;
2. the cell produces a +2.67 pp conversion effect versus holdout;
3. the effect remains credible after Holm adjustment;
4. all declared absolute guardrails pass;
5. mean incremental contribution margin is positive but its interval includes material downside;
6. email plus SMS has no supported main effect, so the added contact pressure is not justified;
7. the next stage should prioritize better margin precision and validate the result in a fresh cohort.

## Evidence boundary

All organizations, customers, assignments, outcomes, effects, and costs are synthetically generated. The reference result demonstrates analytical practice; it does not predict real campaign performance. Contribution-margin assumptions require Finance approval in a production setting, and channel consent must be revalidated at activation time.
