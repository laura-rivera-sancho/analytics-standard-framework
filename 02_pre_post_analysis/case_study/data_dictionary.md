# FinFlow Synthetic Data Dictionary

The planned synthetic dataset is transaction-level so the case can support simple pre/post comparisons, daily time-series analysis, interrupted time series, and segment analysis.

| Field | Type | Description |
|---|---|---|
| `transaction_id` | string | Synthetic unique transaction identifier. Raw training data will intentionally include a small number of duplicates. |
| `customer_id` | string | Synthetic customer identifier. Customers may have more than one transaction. |
| `transaction_date` | date | Date of the eligible transaction. Coverage: 2026-02-01 through 2026-05-31. |
| `period` | string | `Pre` before 2026-04-01 and `Post` on/after 2026-04-01. Derived during analysis rather than trusted blindly from raw data. |
| `days_from_launch` | integer | Calendar-day distance from the intervention date. Negative before launch, 0 on launch date, positive afterward. |
| `post_flag` | integer | 1 for post-launch transactions, otherwise 0. |
| `ramp_flag` | integer | 1 for the first 7 days after launch to support launch-stabilization analysis. |
| `campaign_flag` | integer | 1 during the short post-launch marketing campaign period. |
| `country` | category | Synthetic market: US, MX, CR, or BR. Raw training data may contain inconsistent casing. |
| `device_type` | category | `Mobile` or `Desktop`. |
| `customer_tenure` | category | `New` or `Existing`. |
| `risk_tier` | category | `Low`, `Medium`, or `High` transaction/customer risk grouping. |
| `transaction_value_usd` | float | Synthetic transaction amount in USD; intentionally right-skewed. |
| `verification_completed` | binary | 1 if the verification flow completed successfully. Primary KPI numerator. |
| `verification_time_seconds` | float | Time required to complete/exit verification. Intentionally right-skewed and includes a few anomalous raw values. |
| `manual_review` | binary | 1 if the transaction required manual risk review. |
| `payment_declined` | binary | 1 if the payment was declined. Guardrail KPI. |
| `support_contact` | binary | 1 if a related support contact occurred within the defined follow-up window. Guardrail KPI. |
| `fraud_confirmed` | binary | 1 if confirmed fraudulent activity was identified. Rare-event guardrail. |

## KPI definitions

### Verification completion rate
`SUM(verification_completed) / COUNT(eligible transactions)`

Primary KPI. Higher is better.

### Verification time
Analyze both mean and median `verification_time_seconds` because the distribution is expected to be right-skewed. Lower is better.

### Manual review rate
`SUM(manual_review) / COUNT(eligible transactions)`

Lower is generally better provided fraud/payment-quality guardrails remain acceptable.

### Payment decline rate
`SUM(payment_declined) / COUNT(eligible transactions)`

Guardrail. Interpretation depends on fraud/risk performance; lower is not automatically better if controls become too permissive.

### Support contact rate
`SUM(support_contact) / COUNT(eligible transactions)`

Lower is better.

### Fraud-confirmed rate
`SUM(fraud_confirmed) / COUNT(eligible transactions)`

Rare-event guardrail. Lower is better, but event counts and confidence intervals must accompany percentage changes.

## Planned synthetic data behavior

The generator will intentionally encode:
- a mild pre-existing improvement trend in verification completion
- day-of-week variation in transaction volume and processing behavior
- a seven-day launch ramp
- a post-launch reduction in manual review and verification time
- a positive but not perfectly uniform completion effect
- a modest post-period traffic-mix change
- a temporary marketing campaign that increases volume and new-customer share
- stable-to-slightly-noisy fraud behavior due to rarity
- a small number of raw data-quality defects

These characteristics are training features. They are intended to require diagnostic work before the analyst reaches a recommendation.

## Data-quality checks expected

Before analysis, validate at minimum:
- duplicate `transaction_id`
- missing intervention-critical fields
- unexpected category values/casing
- invalid binary values
- negative or implausibly high verification durations
- transaction-date coverage
- consistency of derived pre/post flags with the launch date
- missingness by period
- sudden unexplained volume discontinuities

## Important modeling note

`period`, `post_flag`, `days_from_launch`, and `ramp_flag` should be reproducibly derived from `transaction_date` in the analytical workflow. Raw flags should not be accepted without validation.