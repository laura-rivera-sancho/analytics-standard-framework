# Expected Customer Value Results

## Reference population

Seed `606` generates 25,343 raw order rows for 3,000 customers. Validation identifies 30 duplicate order IDs, 25 rows with missing acquisition channel, 15 nonpositive-revenue rows, and at least 12 future-dated rows. After deduplication and quarantine, 25,286 transactions remain.

## Current RFM profile

| Segment | Customers | Customer share | Trailing-year value | Value share |
|---|---:|---:|---:|---:|
| Champions | 694 | 23.1% | $1,232,660.75 | 55.5% |
| Loyal Customers | 535 | 17.8% | $393,526.46 | 17.7% |
| At Risk | 503 | 16.8% | $376,992.02 | 17.0% |
| Hibernating | 698 | 23.3% | $113,337.94 | 5.1% |
| New or Potential | 338 | 11.3% | $64,204.74 | 2.9% |
| Needs Attention | 232 | 7.7% | $40,229.91 | 1.8% |

The 3,000-customer population represents $2,220,951.82 in trailing-year recognized revenue. Value is concentrated: Champions contribute over half of value while representing less than one quarter of customers.

## Lifecycle movement

From 2026-05-31 to 2026-08-31, 1,356 customers remain stable, 969 improve, and 675 decline. The largest transitions include Hibernating remaining Hibernating, Champions remaining Champions, Loyal Customers moving to Champions, and Loyal Customers moving to At Risk.

Movement is a descriptive prioritization signal. Relative quintile boundaries and customer behavior both influence the result, so migration is not interpreted as campaign impact.

## Recommended first wave

Select 500 consented At Risk or Needs Attention customers using the declared priority score. The reference file contains 398 At Risk and 102 Needs Attention customers representing $323,176.80 in trailing-year value.

Reserve a randomized holdout within priority bands. Measure incremental repeat purchase and recognized revenue alongside unsubscribe, complaint, delivery, offer-cost, and segment-coverage guardrails.
