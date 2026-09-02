# Target Analysis Fundamentals

Target analysis converts a business action into a governed population: who can be considered, who must be excluded, how large the opportunity is, and how limited capacity should be allocated. Its credibility depends less on algorithmic complexity than on definitions, denominators, traceability, and a safe activation handoff.

## The five populations

1. **Source population** — every record available at the as-of date.
2. **Valid population** — records remaining after quality controls and deduplication.
3. **Eligible population** — units meeting every policy and operational rule.
4. **Prioritized population** — eligible units ordered by documented decision criteria.
5. **Activated population** — units actually sent to the execution channel after final suppressions.

These populations should never be treated as interchangeable. Every percentage needs a named denominator, and every reduction needs a reason.

## Eligibility and priority answer different questions

Eligibility is a hard gate: may this merchant be contacted? Priority is an allocation rule: among eligible merchants, who should be contacted first? Mixing the two obscures exclusions and makes policy difficult to audit.

An eligibility rule should specify its rationale, source field, comparison, null behavior, effective date, owner, and expected volume impact. Priority criteria should be interpretable, monotonic where appropriate, and limited to information available at the decision time.

## Descriptive segments are not causal evidence

Segment profiles explain composition and operational coverage. A higher selection rate in a country or industry does not show that membership caused the score. Differences may reflect volume, settlement friction, or data coverage. Report observed composition, investigate unexpected disparities, and avoid causal language.

## Sizing requires scenarios

An addressable count is not an outcome. Translate selected merchants into a planning scenario with explicit adoption and value assumptions:

`annualized contribution = selected × expected adoption rate × monthly contribution per adopter × 12`

Show the assumptions alongside the estimate and vary the assumptions. Do not present scenario output as forecast accuracy or realized return.

## Transparent prioritization

The LuminaPay case assigns points across three dimensions:

| Dimension | Evidence | Maximum points |
|---|---|---:|
| Need | Long settlement delay, payout failures, support friction | 4 |
| Value | Monthly payment volume | 2 |
| Fit | Active mobile use, sustainable economics, low operational risk | 3 |

The score is intentionally simple. It can be inspected, challenged, and reproduced by business and operations partners. Ties are resolved by payment volume and merchant ID so the output is deterministic.

## Common failure modes

- changing denominators between funnel stages
- silently treating missing eligibility fields as eligible
- counting duplicate entities as additional opportunity
- scoring ineligible entities and excluding them only afterward
- using future information or campaign outcomes in the target definition
- optimizing a proxy without checking operational or customer harm
- using sensitive attributes directly or through careless proxies
- exporting excessive personal or operational data
- treating illustrative adoption assumptions as measured lift
- launching without suppressions, audit fields, ownership, or measurement

## Review questions

- Can each included and excluded merchant be explained from source fields?
- Does the funnel reconcile to one valid starting population?
- Are policy rules separated from capacity choices?
- Are segments used descriptively and checked for surprising disparities?
- Do sensitivity results show what changes the recommendation?
- Is the activation file minimal, versioned, time-stamped, and suppressible?
- Is a randomized holdout or another credible measurement plan defined?

## When to use another module

- Use [A/B Testing](../01_ab_testing/README.md) to estimate the causal effect of an intervention.
- Use [Pre/Post Analysis](../02_pre_post_analysis/README.md) to evaluate a change when randomization is unavailable.
- Use the [Machine Learning framework](https://github.com/laura-rivera-sancho/machine-learning-standard-framework) when the decision requires estimating a future individual-level outcome from historical data.
- Use Target Analysis when the immediate decision is population definition, sizing, description, and capacity allocation.
