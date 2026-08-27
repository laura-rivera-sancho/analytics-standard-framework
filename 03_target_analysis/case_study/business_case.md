# LuminaPay Instant Settlement Targeting Business Case

LuminaPay is a fictional payment platform serving small and midsize merchants in the United States, Mexico, Brazil, and Costa Rica. Instant Settlement is available to qualified merchants but has limited outreach capacity for the next campaign.

All people, organizations, data, and monetary assumptions in this case are synthetically generated for portfolio demonstration. They do not represent an employer or client.

## Decision

Which 6,000 eligible merchants should receive the first outreach wave for Instant Settlement on the 2026-08-01 population snapshot?

## Decision contract

| Item | Definition |
|---|---|
| Owner | Director of Merchant Growth |
| Unit | One merchant account, keyed by `merchant_id` |
| As-of date | 2026-08-01 |
| Capacity | 6,000 merchants |
| Action | One compliant education and enrollment sequence |
| Primary planning outcome | Instant Settlement adoption |
| Guardrails | Complaints, opt-outs, delivery failures, operational exceptions, and segment coverage |
| List expiry | Seven days after approval; suppressions rerun before send |

## Eligibility policy

A merchant must have an active account, verified KYC, at least three months of tenure, no existing Instant Settlement enrollment, no contact in the prior 30 days, low or medium risk, and at least $5,000 in monthly payment volume.

Rules are applied as hard gates. Missing hard-policy fields would be treated as not eligible and escalated; this synthetic dataset has complete gate fields after impossible records are quarantined.

## Prioritization policy

Eligible merchants receive auditable points for need, value, and fit. Country and industry do not award points. The campaign fills capacity in descending score order, then monthly volume, then merchant ID.

Priority tiers are High (6–9 points), Medium (4–5), and Standard (0–3).

## Planning assumptions

The case uses illustrative adoption rates of 18% for High, 10% for Medium, and 5% for Standard priority. Each adoption is assumed to contribute $40 per month. These rates are scenario inputs, not predictions or measured effects.

## Recommended decision

Approve a controlled 6,000-merchant first wave consisting of all 2,573 High-priority merchants and the top 3,427 Medium-priority merchants. Preserve a randomized holdout within priority bands, rerun suppressions, and evaluate incremental adoption before expanding toward 9,000.

## Key limitations

- The data and economic assumptions are synthetic.
- The point system encodes transparent business judgment, not optimized response probability.
- Tier adoption rates are illustrative and require experimental validation.
- Segment differences are descriptive and should not be interpreted causally.
- Actual activation requires privacy, compliance, channel, and regional review.
