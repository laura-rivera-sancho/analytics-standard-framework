# Harbor & Pine Customer Lifecycle Business Case

## Context

Harbor & Pine is a fictional omnichannel retailer. Growth leadership sees uneven repeat-purchase behavior but lacks a consistent customer-value view. CRM teams currently use separate recency lists and spend thresholds, creating overlapping messages and inconsistent treatment.

## Decision

Approve a first retention wave of at most 500 consented customers, and define differentiated lifecycle treatment for the broader customer base.

## Audience and owners

- Growth leadership owns the capacity decision.
- CRM owns message and offer execution.
- Customer Analytics owns segmentation and measurement.
- Analytics Engineering owns the governed upstream data products.

## Analytical contract

- Customer grain: one row per customer at each snapshot date.
- Current cutoff: 2026-08-31.
- Comparison cutoff: 2026-05-31.
- RFM window: trailing 365 days.
- Monetary measure: recognized revenue from valid positive-value orders.
- Activation capacity: 500 customers.
- Eligibility: marketing consent plus At Risk or Needs Attention status.

## Success criteria

- Customer and value totals reconcile across segments.
- RFM rules and activation ranking are reproducible and auditable.
- Lifecycle movement is measured at customer level.
- The selected audience stays within capacity and contains only consented customers.
- A randomized holdout is specified before launch.

## Guardrails

Track unsubscribe and complaint rates, offer cost, delivery failures, contact frequency, country and acquisition-channel coverage, and operational capacity. No non-consented customer may enter the activation file.

## Evidence boundary

The data, company, customer identifiers, results, and recommendations are synthetically generated. RFM is descriptive and the activation plan is a test design—not a forecast of incremental impact.
