# OrbitMart Checkout Diagnostic Data Dictionary

The source grain is one date × country × platform × app version × payment method × acquisition channel aggregate. All times use the business reporting calendar in UTC.

| Field | Type | Definition | Analytical use |
|---|---|---|---|
| `date` | date | Business reporting date | Current, prior, and historical windows |
| `country` | category | Operational market: US, MX, BR, or CR | Pre-specified localization dimension |
| `platform` | category | Web, iOS, or Android | Pre-specified experience dimension |
| `app_version` | category | Web, iOS 12.1, Android 8.3, or Android 8.4 | Release-cohort diagnostic |
| `payment_method` | category | Card, Digital wallet, or Bank transfer | Payment-stage diagnostic |
| `acquisition_channel` | category | Organic, Paid search, Paid social, or Unknown | Traffic composition diagnostic |
| `checkout_starts` | integer | Sessions entering checkout | Primary KPI denominator |
| `payment_attempts` | integer | Checkouts submitting a payment | Attempt-rate numerator |
| `payment_approvals` | integer | Payment attempts approved | Approval-rate numerator |
| `orders_completed` | integer | Approved payments creating a completed order | Primary KPI numerator |
| `revenue_usd` | decimal | Synthetic completed-order revenue | Impact context and average order value |
| `checkout_support_contacts` | integer | Checkout-related contacts | Independent operational signal |

## Derived metrics

| Metric | Formula |
|---|---|
| Checkout completion rate | `orders_completed / checkout_starts` |
| Attempt rate | `payment_attempts / checkout_starts` |
| Approval rate | `payment_approvals / payment_attempts` |
| Post-approval completion rate | `orders_completed / payment_approvals` |
| Average order value | `revenue_usd / orders_completed` |
| Within effect | Current segment weight × segment rate change |
| Mix effect | Weight change × prior segment-rate difference from the overall prior rate |

## Data-quality controls

The synthetic raw data includes duplicate grains, missing acquisition channels, lowercase country values, negative checkout starts, and impossible funnel ordering. The reference workflow reports defects, labels missing channels as `Unknown`, normalizes country, removes duplicate grains, and quarantines impossible funnels.

## Statistical controls

Segment tests require at least 300 checkout starts in both periods. Two-proportion tests are adjusted using Benjamini–Hochberg within each tested dimension. A flagged decline must also exceed two percentage points. Statistical flags guide triage; they do not establish causality.
