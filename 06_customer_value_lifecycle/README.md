# Customer Value & Lifecycle Analytics

> **Status: In review.** This module turns governed customer and order data into reproducible RFM segments, lifecycle movement, and a controlled retention action plan.

**Portfolio shortcut:** Review the [Finished stakeholder readout](reports/stakeholder_readout.md) for the value concentration, migration risks, and recommended 500-customer activation.

## Business question

Harbor & Pine needs to decide how lifecycle treatment should differ across its customer base and where a limited retention team should focus first. The analysis must identify high-value customers, distinguish recent promise from disengagement, measure quarter-over-quarter segment movement, and produce an auditable audience without treating descriptive segments as causal predictions.

The reference analysis finds that **Champions represent 23.1% of customers but 55.5% of trailing-year value**. Another **503 At Risk customers hold $377.0K in value**. A consent-filtered, capacity-constrained first wave selects **500 At Risk or Needs Attention customers representing $323.2K in trailing-year value**.

## What this module demonstrates

- explicit analysis dates, lookback windows, customer grain, and value definitions
- validation and quarantine of duplicate, future, and nonpositive transactions
- deterministic recency, frequency, and monetary scoring
- interpretable segment rules and reconciled segment profiles
- quarter-over-quarter lifecycle migration without causal overclaiming
- transparent, consent-aware prioritization under a 500-customer capacity limit
- activation guidance with a randomized holdout and outcome measurement plan
- a direct analytical consumer of the portfolio's governed customer data architecture

## Navigate the module

| Resource | Purpose |
|---|---|
| [Fundamentals](customer_value_lifecycle_fundamentals.md) | Core RFM, lifecycle, prioritization, governance, and interpretation concepts |
| [Methodology](methodology.md) | Reusable customer-value workflow and analytical quality gates |
| [Business case](case_study/business_case.md) | Decision, audience, constraints, and success criteria |
| [Data dictionary](case_study/data_dictionary.md) | Transaction grain, fields, derived measures, and exclusions |
| [Expected results](case_study/expected_results.md) | Deterministic findings and interpretation boundary |
| [Guided notebook](notebooks/guided_customer_value_lifecycle.ipynb) | Worked RFM, profile, migration, and activation analysis |
| [Reference analysis](src/analyze_customer_value.py) | Reusable quality, RFM, migration, and prioritization functions |
| [Synthetic generator](src/generate_synthetic_data.py) | Deterministic customer-order history with deliberate defects |
| [Stakeholder readout](reports/stakeholder_readout.md) | Executive recommendation and portfolio artifacts |

## Run locally

From the repository root:

```bash
python 06_customer_value_lifecycle/src/generate_synthetic_data.py
python 06_customer_value_lifecycle/src/analyze_customer_value.py
pytest tests/test_customer_value_lifecycle.py
```

The full dataset and processed activation files are reproducible from seed `606` and intentionally ignored. A compact 3,000-row sample remains tracked for inspection.

## Decision boundary

RFM describes observed purchase behavior; it does not estimate incremental response or customer lifetime value. The selected audience authorizes only a controlled retention test. A randomized holdout is required before interpreting response differences as campaign impact, and non-consented customers remain excluded from activation.

## Data-platform relationship

The analytical contracts mirror the governed `customer_360` and `rfm_segments` products in the [Data Architecture Standard Framework](https://github.com/laura-rivera-sancho/data-architecture-standard-framework). This repository remains independently reproducible through synthetic inputs while demonstrating how the two portfolio pillars connect.
