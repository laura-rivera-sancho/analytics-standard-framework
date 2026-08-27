# LuminaPay Target Analysis Expected Results

These deterministic results use seed 314 and the repository's reference code. Small formatting differences are acceptable; material count differences indicate a changed generator, rule, or dependency.

## Data-quality reconciliation

| Check | Reference result |
|---|---:|
| Raw rows | 60,030 |
| Duplicate merchant IDs | 30 |
| Missing industries | 240 |
| Lowercase country values | 20 |
| Negative-volume rows | 20 |
| Invalid-tenure rows | 20 |
| Clean merchant population | 59,960 |

## Eligibility funnel

| Stage | Remaining | Share of clean population |
|---|---:|---:|
| Total merchant population | 59,960 | 100.0% |
| Active account | 54,610 | 91.1% |
| Verified KYC | 49,163 | 82.0% |
| At least 3 months tenure | 49,032 | 81.8% |
| Not already enabled | 38,005 | 63.4% |
| No contact in prior 30 days | 34,174 | 57.0% |
| Low or medium risk | 30,678 | 51.2% |
| At least $5k monthly volume | 25,805 | 43.0% |

## Capacity recommendation

At 6,000 contacts, all 2,573 High-priority merchants and 3,427 of 7,593 Medium-priority merchants are selected. Standard-priority merchants are not required to fill capacity.

| Capacity | Expected adopters | Expected adoption | Annualized contribution | Average score | High-priority share |
|---:|---:|---:|---:|---:|---:|
| 3,000 | 506 | 16.9% | $242.8K | 6.26 | 85.8% |
| 6,000 | 806 | 13.4% | $386.8K | 5.54 | 42.9% |
| 9,000 | 1,106 | 12.3% | $530.8K | 5.03 | 28.6% |

The 6,000-contact wave balances reach and average priority. Expanding to 9,000 increases illustrative total contribution but lowers average score and expected response rate.

## Segment review

Country selection rates range from 20.9% to 29.5%. Brazil's higher rate reflects the synthetic generator's greater settlement friction; country does not award score points. Industry selection rates are tightly grouped around 21.8%–23.6%, while `Unknown` is 19.8%. These are descriptive checks, not evidence of fairness or causality.

## Interpretation

Approve the 6,000-merchant list only as a controlled first wave. The expected-adopter and contribution figures are scenarios. Preserve a randomized holdout within actionable bands to estimate incremental adoption and update assumptions with observed evidence.
