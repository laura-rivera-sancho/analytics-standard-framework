# A/B Testing Stakeholder Readout Deck — Standard Guide

This template standardizes how A/B test results are communicated to business and technical stakeholders. The goal is to keep the presentation decision-focused, concise, and consistent across experiments.

## Recommended deck length

Use **8–10 slides** for a standard stakeholder readout. Add technical appendices only when needed.

---

## Slide 1 — Executive Summary

**Purpose:** Give stakeholders the answer first.

Include:
- Business question
- Experiment / feature tested
- Primary KPI result
- Statistical conclusion
- Business impact
- Recommendation

**Standard wording pattern:**

> The Treatment increased/decreased **[primary KPI]** by **[X percentage points / X%]** versus Control. The effect was **[statistically significant / not statistically significant]** and **[met / did not meet]** the predefined business threshold. Guardrail metrics showed **[no material deterioration / specific concern]**. We recommend **[roll out / iterate / extend / stop]**.

**Visual:** One KPI callout card plus recommendation banner.

---

## Slide 2 — Business Question & Hypothesis

**Purpose:** Reconnect the analysis to the decision being made.

Include:
- Business problem
- Customer or operational pain point
- Treatment description
- Control description
- H0 / H1 in business language
- Decision the experiment is intended to support

Avoid starting with methodology or statistics.

---

## Slide 3 — Experiment Design

**Purpose:** Show that the comparison is credible.

Include:
- Experiment dates
- Eligible population
- Unit of randomization
- Control / Treatment allocation
- Final analytical sample size
- Primary KPI
- Secondary KPI(s)
- Guardrails

Optional:
- MDE
- Power target
- Predefined duration

**Visual:** Simple Control vs Treatment flow diagram.

---

## Slide 4 — Data Quality & Experiment Health

**Purpose:** Establish trust in the result before discussing outcomes.

Include only the checks that matter to the conclusion:
- Sample Ratio Mismatch (SRM)
- Duplicates / exclusions
- Missing treatment assignment
- Cross-group contamination
- Tracking completeness
- Baseline balance
- Major implementation issues

**Standard status format:**

| Check | Status | Comment |
|---|---|---|
| Assignment ratio | Pass / Investigate | Expected 50/50; observed X/X |
| Duplicate units | Pass / Corrected | X duplicates removed |
| Missing assignment | Pass / Corrected | X records excluded |
| Baseline balance | Pass / Investigate | No material imbalance |

Do not overwhelm stakeholders with every QA check. Detailed validation belongs in the appendix.

---

## Slide 5 — Primary KPI Result

**Purpose:** Present the most important experiment result clearly.

Include:
- Control value
- Treatment value
- Absolute lift
- Relative lift when useful
- 95% confidence interval
- p-value or significance conclusion
- Business threshold / MDE comparison

**Preferred interpretation:**

> Treatment improved checkout completion from **71.8% to 75.1%**, a **+3.3 pp** absolute lift. The confidence interval excludes zero, providing evidence that the effect is unlikely to be explained by random variation alone. The observed lift also exceeds the predefined **+2.0 pp** business threshold.

**Visual:** Two-bar comparison or lift callout with confidence interval.

Do not make the p-value the headline.

---

## Slide 6 — Secondary & Guardrail Metrics

**Purpose:** Show whether the Treatment creates trade-offs.

Include a compact table:

| Metric | Control | Treatment | Change | Interpretation |
|---|---:|---:|---:|---|
| Primary KPI | X | X | X | Positive / Neutral / Negative |
| Secondary KPI | X | X | X | ... |
| Guardrail 1 | X | X | X | ... |
| Guardrail 2 | X | X | X | ... |

Separate statistically credible changes from directional/noisy movement.

For rare metrics such as fraud, show event counts if they materially affect interpretation.

---

## Slide 7 — Segment Insights

**Purpose:** Explain where the effect is strongest or weakest.

Include only business-relevant segments, such as:
- Device
- Market / country
- Customer tenure
- Product tier
- Acquisition channel

For each segment, show Control, Treatment, and lift.

Clearly label:
- **Pre-specified segment:** planned before the experiment
- **Post-hoc segment:** exploratory; requires validation before strong causal claims

Avoid presenting many slices simply because they are available.

---

## Slide 8 — Business Impact

**Purpose:** Translate statistical results into an operational or financial outcome.

Possible translations:
- Incremental conversions
- Additional active customers
- Revenue / payment volume
- Cost avoidance
- Reduced support demand
- Reduced handling time
- Improved retention / activation

**Example formula:**

`Annual eligible volume × observed absolute lift = estimated incremental outcomes`

State assumptions explicitly.

If the estimate is uncertain, provide a range rather than false precision.

---

## Slide 9 — Recommendation

**Purpose:** Make the decision explicit.

Choose one of four standard recommendation categories:

### Roll out
Use when the effect is statistically credible, commercially meaningful, and guardrails are acceptable.

### Iterate
Use when direction is promising but the experience should be improved before broader deployment.

### Retest / Extend
Use when evidence is inconclusive, sample size is insufficient, or a new hypothesis requires validation.

### Stop / Roll back
Use when the treatment causes harm or fails to create sufficient value.

Include:
- Recommendation
- Why
- Risks / caveats
- Required monitoring

---

## Slide 10 — Next Steps

Include concrete ownership and timing:
- Rollout plan
- Follow-up experiment
- Monitoring window
- Guardrail thresholds
- Segment-specific validation
- Technical fixes
- Decision owner

Avoid generic next steps such as “continue monitoring” without defining what will be monitored and for how long.

---

# Optional Appendix Slides

Use only when needed.

## Appendix A — Statistical Method

Include:
- Test selected and why
- Alpha
- Confidence level
- Sample size
- Assumptions
- Sensitivity checks

## Appendix B — Sample Size / Power

Include:
- Baseline rate
- MDE
- Alpha
- Power
- Required sample
- Actual sample

## Appendix C — Data Quality Details

Include:
- Exclusion counts
- Duplicate handling
- Missingness
- Metric definitions
- Assignment / exposure rules

## Appendix D — Full Segment Table

Provide supporting segment detail without cluttering the main narrative.

---

# Presentation Standards

## Lead with decisions
The first slide should answer: **What happened, does it matter, and what should we do?**

## Use percentage points correctly
If conversion increases from 70% to 73%:
- Absolute lift = **+3 percentage points**
- Relative lift = **+4.3%**

Do not use the terms interchangeably.

## Separate evidence from interpretation
Example:
- **Evidence:** Treatment increased completion by +3.2 pp; 95% CI +1.9 to +4.5 pp.
- **Interpretation:** The change is both statistically credible and large enough to justify rollout.

## Show uncertainty
Confidence intervals are preferred over presenting a single estimate with no context.

## Avoid causal overstatement
If randomization, exposure, or tracking is compromised, qualify causal language.

## Keep technical detail proportional to the audience
Executives need decision implications. Analysts may require test details. Keep deep methodology in the appendix unless it changes the decision.

---

# Standard Stakeholder Storyline

Every A/B testing readout should answer these questions in order:

1. What decision are we making?
2. What did we test?
3. Can we trust the experiment?
4. What happened to the primary KPI?
5. Did anything else get worse?
6. Where was the effect strongest or weakest?
7. What does the effect mean for the business?
8. What should we do next?

This storyline should remain consistent even if the underlying metrics or industry change.
