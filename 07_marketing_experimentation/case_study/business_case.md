# Harbor & Pine Marketing Experimentation Business Case

## Scenario

Harbor & Pine is a fictional omnichannel home and lifestyle retailer. Its lifecycle analysis identified valuable At Risk and Needs Attention customers who may benefit from retention treatment. The growth team currently uses a general email reminder, but it does not know whether lifecycle-informed messaging improves outcomes or which combination of message, offer, and channel plan creates the strongest incremental business result.

The team wants an experimentation suite that teaches a reusable split-test workflow and then supports a controlled multivariate decision. All data will be deterministically generated; no real customer, employer, or campaign data will be used.

## Decision and owners

**Primary decision:** Which treatment, if any, should enter a staged retention rollout?

**Decision owner:** Vice President of Growth

**Analytical owner:** Experimentation Analytics

**Operational owners:** Customer Relationship Management, Marketing Operations, and Channel Operations

**Required reviewers:** Finance for contribution-margin assumptions and Privacy/Compliance for consent, suppression, and contact-policy controls

## Why experimentation is required

Customers who receive different campaigns may already differ in value, engagement, channel consent, or likelihood to return. Historical campaign comparisons therefore do not identify incremental impact. Random assignment creates a defensible counterfactual when assignment, exposure, outcome windows, and analysis rules are preserved.

The program will use intention-to-treat estimates: customers are analyzed according to randomized assignment even when delivery or engagement is imperfect. Exposure and delivery measures remain diagnostics rather than reasons to remove assigned customers selectively.

## Suite design

### Experiment 1 — Lifecycle-message split test

**Purpose:** Establish whether a lifecycle-informed email produces a practically meaningful improvement over the current general reminder.

**Arms:**

- Control: current general retention reminder
- Treatment: lifecycle-informed, benefit-led reminder with no additional discount

**Randomization unit:** customer

**Target population:** email-consented At Risk and Needs Attention customers who pass identity, suppression, frequency-cap, and recent-purchase exclusions

**Primary estimand:** intention-to-treat difference in 14-day completed-purchase rate between treatment and control

**Primary metric:** completed purchase within 14 days of assignment

**Secondary metrics:** recognized revenue per assigned customer, contribution margin per assigned customer, and click-through rate

**Guardrails:** unsubscribe rate, complaint rate, refund rate, and contact-policy violations

### Experiment 2 — Full-factorial multivariate test

**Purpose:** Estimate which factors and prespecified combinations improve purchase and contribution-margin outcomes while respecting channel and customer-experience constraints.

**Eligible population:** customers meeting the lifecycle criteria who are consented for both email and SMS. This restriction protects assignment integrity but limits generalization to dual-consented customers.

**Factors and levels:**

| Factor | Level 1 | Level 2 |
|---|---|---|
| Message framing | Benefit-led | Urgency-led |
| Offer | Free shipping | 10% discount |
| Channel plan | Email only | Coordinated email plus SMS |

The full factorial contains eight active treatment cells. A separate no-contact holdout provides an incremental baseline. The planned synthetic reference population contains 18,000 eligible customers: 2,000 per active cell and 2,000 in holdout before deliberate data-quality defects and documented exclusions.

**Primary estimands:**

- average main effect of each factor on 14-day completed-purchase rate
- incremental effect of each active cell versus no-contact holdout

**Prespecified interactions:**

- message framing × offer
- offer × channel plan

The three-way interaction and other subgroup findings are exploratory unless the power plan explicitly supports them.

## Metrics and business definitions

### Primary outcome

`converted_14d = 1` when an assigned customer completes at least one qualifying purchase from assignment time through the end of day 14. Assignment occurs before any campaign exposure.

### Business-value outcome

Contribution margin per assigned customer will subtract product cost, discount cost, shipping subsidy, messaging cost, and refund impact from recognized revenue. The exact assumptions will be versioned in the methodology and data dictionary.

### Guardrails

- unsubscribe or channel opt-out within 14 days
- complaint within 14 days
- refunded qualifying purchase within the defined return-observation window
- frequency-cap or consent-policy violation

A higher conversion rate cannot justify rollout when the prespecified guardrail or contribution-margin rule fails.

## Power and minimum detectable effect plan

Before reading outcomes, the workflow will:

1. declare the baseline conversion and business-relevant minimum detectable effect
2. choose two-sided significance, power, allocation, and expected attrition assumptions
3. calculate sample requirements for the two-arm split test
4. distinguish pooled main-effect power from lower-powered cell and interaction comparisons
5. record which interaction and segment analyses are confirmatory versus exploratory
6. avoid changing the sample or hypothesis family after observing results

The final synthetic design may be regenerated if the declared sample does not support its intended confirmatory estimands. Statistical significance alone will not replace the practical-effect or margin thresholds.

## Randomization and integrity controls

- assign at customer grain to prevent cross-treatment contamination
- use a fixed deterministic seed for reproducibility
- stratify by lifecycle segment and value band where appropriate
- freeze assignment before exposure
- preserve assignment records even when delivery fails
- exclude known consent and suppression violations before randomization
- test for duplicate assignments, missing arms, timestamp order, and sample-ratio mismatch
- report delivery and exposure separately from intention-to-treat outcomes

## Multiplicity strategy

The analysis will maintain a prespecified confirmatory family. Holm adjustment will control family-wise error for the limited rollout decisions. Benjamini–Hochberg false-discovery control may be used for clearly labeled exploratory families. Unadjusted post-hoc segment p-values will not be presented as discoveries.

## Decision rules

A treatment can be recommended for staged rollout only when:

- assignment and sample-ratio checks pass or any deviation is credibly resolved
- the primary intention-to-treat effect is statistically credible under the declared multiplicity plan
- the absolute effect meets the practical minimum
- incremental contribution margin is positive under the approved assumptions
- no critical consent, complaint, refund, or opt-out guardrail crosses its threshold
- the result is not dependent on an unsupported post-hoc subgroup
- the rollout includes monitoring, a rollback trigger, and an owner

If no treatment meets all gates, the valid decision is to retain the current policy, redesign the treatment, or collect more evidence—not to select the lowest p-value.

## Planned data-quality challenges

The synthetic generator will deliberately introduce a small, documented set of defects so validation behavior is inspectable:

- duplicate assignment identifiers
- assignments after a recorded outcome
- exposure timestamps before assignment
- consent-ineligible channel assignments
- missing lifecycle segments
- invalid treatment labels
- incomplete outcome observation windows

Critical defects will be quarantined or block analysis according to a declared rule. Cleaned counts must reconcile to raw, excluded, and analyzed populations.

## Acceptance criteria

A7 is complete only when it publishes:

- an interview-ready fundamentals guide and reusable methodology
- a versioned data dictionary and deterministic synthetic generator
- validated split-test and factorial datasets with compact tracked samples
- reusable power, integrity, effect-estimation, multiplicity, interaction, and business-value functions
- one guided notebook and no challenge notebook
- automated tests for critical statistical and governance logic
- deterministic expected results
- an executive preview, Markdown readout, and five-slide PowerPoint deck
- limitations, consent controls, monitoring, and staged-rollout guidance

## Out of scope

- real customer activation or external message delivery
- adaptive bandits or automated traffic reallocation
- personalized uplift modeling
- long-term customer lifetime value estimation
- unplanned repeated peeking or early stopping
- claims that synthetic effect sizes predict real campaign performance
