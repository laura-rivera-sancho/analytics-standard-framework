# NovaPay Expected Reference Results

These reference values are produced by `src/generate_synthetic_data.py` with `SEED = 42` and `N_CUSTOMERS = 40_000`, then analyzed on the clean reference population.

They exist so analysts can validate that their implementation is working. The recommended learning path is to analyze the raw/synthetic data first and use this file only afterward.

## Primary KPI: checkout completion

| Metric | Control | Treatment |
|---|---:|---:|
| Customers | 20,000 | 20,000 |
| Checkout completion rate | 72.64% | 75.95% |

- Absolute lift: **+3.31 percentage points**
- Relative lift: **~4.56%**
- Two-proportion z-test p-value: **< 0.001**
- Approximate 95% confidence interval for absolute lift: **+2.45 pp to +4.17 pp**

Interpretation: the synthetic Treatment effect exceeds the assumed +2 pp minimum business effect and is statistically distinguishable from zero.

## Checkout time

| Metric | Control | Treatment |
|---|---:|---:|
| Mean checkout time | ~89.35 sec | ~64.16 sec |

The distribution is intentionally right-skewed. A reference implementation should inspect mean, median, skewness, and outliers rather than relying on a single summary statistic.

The Treatment difference is large and statistically detectable in the generated population. The reference analysis provides both Welch's t-test and Mann-Whitney results as a robustness comparison.

## Guardrails

| KPI | Control | Treatment | Reference interpretation |
|---|---:|---:|---|
| Support contact rate | 5.655% | 4.570% | Lower under Treatment; statistically detectable |
| Payment decline rate | 5.495% | 5.180% | Small reduction; not statistically conclusive in this generated sample |
| Fraud rate | 0.355% | 0.350% | No meaningful difference in this generated sample |

## Segment pattern intentionally embedded

Treatment is designed to have a stronger checkout-completion effect for **Mobile** customers than for **Desktop** customers.

The correct interpretation is not automatically "roll out only to Mobile." Analysts should distinguish pre-specified segment analysis from post-hoc discovery and consider multiple-testing risk.

## Expected recommendation

A reasonable executive recommendation is to proceed toward rollout of the simplified checkout experience because:

1. the primary KPI improves by more than the assumed business threshold;
2. the effect is statistically credible;
3. checkout time materially improves;
4. support contacts improve;
5. there is no evidence of meaningful deterioration in payment declines or fraud;
6. post-launch monitoring should continue for guardrails and segment stability.

The exact wording of the recommendation should include assumptions, limitations, and any unresolved implementation questions.
