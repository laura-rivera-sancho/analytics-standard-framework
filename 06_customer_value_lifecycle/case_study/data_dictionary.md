# Customer Value Data Dictionary

## Source grain

One row represents one fictional completed order associated with one customer. Customer attributes repeat across the customer's orders to keep the compact portfolio input independently inspectable.

| Field | Type | Definition | Analytical treatment |
|---|---|---|---|
| `customer_id` | string | Stable fictional customer identifier | Customer grain and deterministic tie-breaker |
| `customer_created_at` | date | Date the customer relationship began | Eligibility at each snapshot |
| `acquisition_channel` | category | Original acquisition source | Profile-only dimension; missing becomes `unknown` |
| `country_code` | category | Fictional customer market | Normalized to uppercase; not used in priority scoring |
| `marketing_consent` | boolean | Whether lifecycle marketing is permitted | Hard activation eligibility rule |
| `order_id` | string | Stable fictional order identifier | Deduplication key |
| `order_timestamp` | date | Date the order occurred | Recency, frequency window, and future-order validation |
| `recognized_revenue` | decimal | Positive completed-order value after discounts | Monetary value; nonpositive rows are quarantined |

## Derived customer measures

| Measure | Definition |
|---|---|
| Recency | Days from snapshot cutoff to most recent valid order |
| Frequency | Distinct valid orders in the trailing 365 days |
| Monetary value | Recognized revenue in the trailing 365 days |
| R/F/M score | Population-relative rank from 1 to 5; higher is more favorable |
| RFM segment | Interpretable rule-based combination of R/F/M scores |
| Movement | Improved, declined, or stable relative to the prior snapshot |
| Priority score | 45% monetary score + 35% frequency score + 20% disengagement evidence |

## Deliberate source defects

The generator adds duplicate order IDs, missing acquisition channels, nonpositive revenue, and future-dated orders. They exist to demonstrate validation and quarantine before business interpretation.
