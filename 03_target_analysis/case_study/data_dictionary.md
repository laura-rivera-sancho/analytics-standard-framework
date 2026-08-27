# LuminaPay Target Analysis Data Dictionary

The synthetic source is a merchant-level snapshot as of 2026-08-01. All behavioral fields end on or before that date.

| Field | Type | Definition | Analytical use |
|---|---|---|---|
| `merchant_id` | string | Synthetic unique merchant key | Deduplication, ranking tie-break, activation key |
| `as_of_date` | date | Population snapshot date | Timing and list expiry control |
| `country` | category | Operational market: US, MX, BR, or CR | Coverage monitoring only; no score points |
| `industry` | category | Merchant operating category | Descriptive profiling only |
| `tenure_months` | integer | Completed months since activation | Eligibility: at least 3 |
| `account_status` | category | Active, Paused, or Closed | Eligibility: Active |
| `kyc_status` | category | Verified, Pending, or Expired | Eligibility: Verified |
| `risk_tier` | category | Low, Medium, or High operational risk | Eligibility excludes High; Low earns one fit point |
| `profitability_tier` | category | Synthetic unit-economics band | Medium or High earns one fit point |
| `monthly_payment_volume_usd` | decimal | Processed payment value in prior 30 days | Eligibility, value points, deterministic tie-break |
| `transaction_count_30d` | integer | Successful transactions in prior 30 days | Descriptive context |
| `avg_settlement_delay_hours` | decimal | Mean observed settlement delay in prior 90 days | Two need points at 36 hours or more |
| `payout_failure_rate_90d` | decimal | Failed payouts divided by payout attempts | One need point at 2% or more |
| `support_contacts_90d` | integer | Settlement-related support contacts | One need point at 2 or more |
| `mobile_app_active` | binary | At least one mobile-app session in prior 30 days | One fit point when active |
| `instant_settlement_enabled` | binary | Current product enrollment indicator | Eligibility requires 0 |
| `contacted_last_30d` | binary | Recent campaign-contact suppression | Eligibility requires 0 |

## Derived fields

| Field | Definition |
|---|---|
| `need_score` | 0–4 points for settlement friction |
| `value_score` | 0–2 points based on monthly payment volume |
| `fit_score` | 0–3 points for mobile readiness, sustainable economics, and low risk |
| `priority_score` | Sum of need, value, and fit scores |
| `priority_tier` | High, Medium, or Standard band |
| `priority_rank` | Deterministic ordering among all eligible merchants |
| `selected` | Whether rank is within campaign capacity |

## Data-quality defects

The raw generator deliberately adds duplicates, missing industries, lowercase country values, negative volume, and impossible tenure. The reference workflow reports these defects, normalizes casing, labels unknown industries, removes duplicate IDs, and quarantines impossible numeric records before eligibility.

## Governance notes

This portfolio example contains no personal data. A production implementation should minimize exported fields, restrict access, record policy approval, apply retention limits, and independently assess whether any field or proxy creates inappropriate differential treatment.
