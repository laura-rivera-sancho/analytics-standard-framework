# Case Study: NovaPay Simplified Checkout Experiment

> **Synthetic case study.** NovaPay is fictional and all data in this repository are generated for training and portfolio purposes.

## Business context

NovaPay is a digital payments platform. Product analytics show that a meaningful share of customers abandon checkout before completing payment. The current flow contains multiple confirmation screens and requires several interactions before payment completion.

The Product team proposes a simplified checkout flow intended to reduce friction while preserving payment quality and risk controls.

## Business decision

Should NovaPay replace the existing checkout journey with the simplified experience?

## Proposed experiences

### Control
Existing checkout journey:
1. Review transaction
2. Confirm payment method
3. Review final amount
4. Authenticate
5. Complete payment

### Treatment
Simplified checkout journey:
1. Review transaction
2. Confirm and authenticate
3. Complete payment

## Business hypothesis

Reducing checkout friction will improve successful checkout completion and shorten checkout time without materially increasing payment declines, support contacts, or fraud.

## Statistical hypotheses

### Primary outcome: checkout completion
- **H0:** checkout completion is equal between Control and Treatment.
- **H1:** checkout completion differs between Control and Treatment, with an expected positive Treatment effect.

## Experiment design

- **Unit of randomization:** customer
- **Allocation:** 50% Control / 50% Treatment
- **Planned experiment duration:** 14 days
- **Synthetic full population:** 40,000 customers
- **Control:** 20,000
- **Treatment:** 20,000

## Eligibility

Include:
- consumer customers eligible for the digital checkout flow
- customers entering checkout during the experiment window
- supported countries in the experiment configuration

Exclude:
- internal/test accounts
- unsupported payment journeys
- observations without valid experiment assignment
- duplicate experimental units after investigation

## KPIs

### Primary KPI
- `checkout_completed`: proportion of customers completing checkout

### Secondary KPIs
- `checkout_time_seconds`: time required to complete/exit the checkout flow
- `transaction_value_usd`: transaction value for behavioral and segment analysis

### Guardrail KPIs
- `payment_declined`
- `support_contact`
- `fraud_flag`

## Minimum business effect

Assume NovaPay considers an absolute improvement of **2 percentage points** in checkout completion commercially meaningful, provided guardrail metrics remain acceptable.

## Analytical questions

1. Did Treatment improve checkout completion?
2. How large is the improvement and what is the uncertainty around it?
3. Did checkout time improve?
4. Did payment declines, support contacts, or fraud deteriorate?
5. Is the effect consistent across device, country, and customer-tenure segments?
6. Are the experiment groups balanced and is assignment trustworthy?
7. Is the result both statistically significant and meaningful for the business?
8. Should NovaPay roll out, iterate, retest, or stop the new experience?

## Embedded learning features

The synthetic data intentionally include realistic analytical characteristics:
- a positive overall Treatment effect
- a stronger Treatment response on Mobile than Desktop
- right-skewed transaction values
- right-skewed checkout times
- small guardrail rates
- duplicate customer records in the sample file
- missing experiment assignments in the sample file
- inconsistent country casing in the sample file

The analyst is expected to identify and resolve data-quality issues before final inference.

## Expected executive story

A strong analysis should not stop at "p < 0.05." The final recommendation should combine:
- experiment validity
- effect magnitude
- confidence interval
- statistical evidence
- guardrail behavior
- segment patterns
- commercial relevance
- implementation recommendation
