# FinFlow Automated Verification — Pre/Post Case Study

## Company

**FinFlow** is a fictional digital-payments company.

## Business context

FinFlow historically relied on a partially manual verification workflow for a subset of transactions that required additional risk checks before completion.

The existing process created operational friction:
- customers waited while verification was completed
- some transactions were abandoned during review
- operations teams handled a high volume of manual cases
- support teams received contacts related to transaction status

Product and Risk launched an **automated transaction-verification workflow** for all eligible traffic.

The new workflow uses predefined verification logic to automatically clear lower-risk cases while continuing to route higher-risk cases for manual review.

## Intervention

**Launch date:** 2026-04-01

**Rollout:** 100% of eligible traffic at launch. There is no randomized Control group.

Because everyone received the new workflow, FinFlow must evaluate impact using a pre/post design.

## Business question

> Did the automated verification workflow reduce transaction-processing friction and manual review demand without increasing payment declines, fraud risk, or support demand?

## Expected mechanism

If the automation works as intended:

1. fewer eligible transactions should require manual review
2. verification time should decline
3. transaction completion should improve
4. support contacts related to transaction status may decline
5. fraud and payment-quality guardrails should remain stable

## KPI framework

### Primary KPI
**Verification completion rate**

Proportion of eligible transactions that successfully complete the verification flow.

### Secondary KPIs
- Average verification time
- Median verification time
- Manual review rate
- Daily completed transaction count

### Guardrail KPIs
- Payment decline rate
- Fraud-confirmed rate
- Support contact rate

## Analytical unit

The synthetic dataset will be generated at the **transaction level**, with transaction date and customer/context attributes that allow daily aggregation and segment analysis.

This supports both:
- simple Pre vs Post comparisons
- time-series / interrupted-time-series analysis

## Analysis windows

Planned data coverage:
- **Pre period:** 2026-02-01 through 2026-03-31
- **Launch date:** 2026-04-01
- **Post period:** 2026-04-01 through 2026-05-31

The first 7 post-launch days should also be inspected separately as a potential ramp/stabilization period.

## Intentional analytical challenges

The synthetic data will contain realistic complications so the case requires judgment rather than a simple Before minus After calculation.

### 1. Existing baseline trend
Verification performance will show a small pre-launch trend, forcing the analyst to distinguish continuation of baseline improvement from intervention-related change.

### 2. Day-of-week seasonality
Transaction volume and some operational KPIs will vary by weekday/weekend.

### 3. Launch ramp
The first several post-launch days will have weaker performance than the later stable post period.

### 4. Traffic-mix shift
The post period will contain a modest shift in country/device/customer-risk composition.

### 5. Concurrent marketing event
A short campaign during the post period will temporarily increase transaction volume and new-customer mix.

### 6. Right-skewed verification time
Verification duration will include long-tail cases, making mean and median interpretation different.

### 7. Rare fraud outcome
Fraud will be intentionally low-frequency, requiring cautious interpretation of relative percentage changes.

### 8. Data-quality issues
The raw training dataset will contain a small number of duplicate transaction IDs, inconsistent category casing, missing fields, and anomalous duration values.

## Expected analytical tasks

The analyst should:

1. validate raw data quality
2. define the final analytical population
3. inspect KPI trends over time
4. compare population mix before and after launch
5. identify launch/ramp and concurrent-event periods
6. calculate unadjusted pre/post KPI changes
7. evaluate statistical uncertainty
8. perform an interrupted-time-series analysis for the primary KPI
9. compare stable-post results with full-post results
10. analyze relevant customer and operational segments
11. assess guardrails
12. estimate business impact
13. rate the strength of causal evidence
14. provide a stakeholder recommendation

## Decision framework

### Continue / Scale
Use when the workflow produces meaningful operational/customer improvement, time-series evidence supports the change, and guardrails remain acceptable.

### Continue with monitoring
Use when the result is positive but causal confidence is moderate or a guardrail requires additional observation.

### Iterate
Use when benefit is concentrated in certain segments or the launch experience creates avoidable friction.

### Validate further
Use when trend, seasonality, mix changes, or concurrent events make the result difficult to interpret confidently.

### Roll back / Stop
Use if payment quality or fraud deteriorates materially or the automation does not generate sufficient value.

## Portfolio objective

This case is designed to demonstrate that the analyst understands the difference between:

> **Performance changed after launch**

and

> **The launch caused the performance change**.

A strong analysis quantifies the observed change while being explicit about the evidence required for causal interpretation.

## Disclaimer

FinFlow, its workflow, customers, transactions, data, and results are entirely fictional and synthetic. The case is designed for education and portfolio demonstration only.