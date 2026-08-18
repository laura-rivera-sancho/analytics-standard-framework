# Pre/Post Challenge Scoring Rubric

This rubric can be used to review the FinFlow challenge notebook or any Pre/Post impact analysis where a randomized Control group is not available.

Total suggested score: **100 points**.

## 1. Business framing — 10 points

| Criteria | Points |
|---|---:|
| Clearly states the business decision being supported | 3 |
| Defines expected success and risk signals | 3 |
| Explains why this is not an A/B test | 2 |
| Identifies key causal risks before analyzing outcomes | 2 |

Strong answer: Frames the decision as whether to continue, iterate, or validate the automated workflow, not merely whether Post metrics are higher.

## 2. Data quality and analytical population — 15 points

| Criteria | Points |
|---|---:|
| Produces and interprets a raw data-quality report | 3 |
| Handles duplicate transaction IDs appropriately | 2 |
| Standardizes categorical values and identifies missing fields | 2 |
| Identifies invalid/anomalous verification durations | 2 |
| Re-derives Pre/Post, ramp, and campaign flags from transaction date | 3 |
| Documents final analytical population and exclusions | 3 |

Strong answer: Does not blindly trust raw intervention flags when launch date is known.

## 3. Simple Pre/Post KPI comparison — 10 points

| Criteria | Points |
|---|---:|
| Reports primary, secondary, and guardrail metrics for Pre and Post | 3 |
| Calculates absolute and relative changes correctly | 2 |
| Uses appropriate statistical comparison for rate metrics | 2 |
| Separates observed movement from causal interpretation | 3 |

Strong answer: Says what changed, while clearly stating that simple Pre/Post comparison alone does not prove causality.

## 4. Ramp and stable-post analysis — 10 points

| Criteria | Points |
|---|---:|
| Identifies the 7-day launch ramp period | 2 |
| Compares full Post and stable Post periods | 3 |
| Explains why excluding ramp can be useful but must be disclosed | 3 |
| Interprets whether performance stabilized after launch | 2 |

Strong answer: Reports ramp as a meaningful implementation period rather than silently removing it.

## 5. Trend, seasonality, and concurrent events — 10 points

| Criteria | Points |
|---|---:|
| Aggregates and visualizes daily KPI trend | 2 |
| Marks launch, ramp, and campaign periods | 2 |
| Evaluates pre-existing baseline trend | 2 |
| Evaluates weekday/weekend seasonality or volume patterns | 2 |
| Discusses how campaign timing could affect interpretation | 2 |

Strong answer: Uses time-series visualization to assess whether the post-launch movement aligns with intervention timing.

## 6. Confounders and mix shift — 10 points

| Criteria | Points |
|---|---:|
| Compares Pre/Post traffic mix by country | 2 |
| Compares device mix | 2 |
| Compares customer tenure mix | 2 |
| Compares risk-tier mix | 2 |
| Explains how mix shifts could bias simple Pre/Post results | 2 |

Strong answer: Identifies that changes in customer or risk composition can move outcomes even if the workflow has no true effect.

## 7. Secondary metrics and guardrails — 10 points

| Criteria | Points |
|---|---:|
| Analyzes verification time using mean and median | 2 |
| Recognizes right-skew in duration metrics | 2 |
| Reviews manual review as a mechanism metric | 2 |
| Reviews payment decline and support contact guardrails | 2 |
| Treats rare fraud outcomes cautiously using event counts | 2 |

Strong answer: Does not overreact to relative changes in rare events without reviewing absolute counts.

## 8. Interrupted Time Series analysis — 15 points

| Criteria | Points |
|---|---:|
| Fits or interprets a basic ITS model | 3 |
| Fits or interprets an adjusted ITS model | 3 |
| Correctly interprets baseline trend | 2 |
| Correctly interprets immediate post-launch level change | 2 |
| Correctly interprets post-launch slope change | 2 |
| Includes ramp, campaign, weekday, and mix covariates where appropriate | 2 |
| States limitations of ITS vs randomized experimentation | 1 |

Strong answer: Uses ITS to strengthen the evidence, but does not claim it creates randomized causality.

## 9. Business impact and recommendation — 10 points

| Criteria | Points |
|---|---:|
| Translates KPI movement into estimated business impact | 2 |
| States assumptions transparently | 2 |
| Provides a causal-confidence rating | 2 |
| Gives a clear recommendation category | 2 |
| Includes next steps and monitoring plan | 2 |

Strong answer: Ends with a decision-ready recommendation, not a list of statistics.

## Suggested score interpretation

| Score | Interpretation |
|---|---|
| 90–100 | Strong portfolio-level analysis; ready for stakeholder or interview discussion |
| 75–89 | Good analysis with minor gaps in interpretation or communication |
| 60–74 | Technically developing; needs stronger causal reasoning and/or communication |
| Below 60 | Incomplete Pre/Post framework; likely over-relies on simple before/after movement |

## Reviewer notes

A strong Pre/Post analysis should demonstrate humility around causality. The best answer is not necessarily the one with the most complex model. The best answer is the one that clearly explains what changed, how credible the evidence is, what could still be confounding the result, and what the business should do next.
