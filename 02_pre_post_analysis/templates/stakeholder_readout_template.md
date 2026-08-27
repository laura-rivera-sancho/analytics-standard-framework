# Pre/Post Analysis Stakeholder Readout — Standard Guide

This template standardizes how Pre/Post analysis results are communicated when a randomized Control group is not available.

The purpose is to help stakeholders understand:

1. what changed after the intervention
2. how credible the evidence is
3. which alternative explanations were evaluated
4. whether guardrails remain acceptable
5. what action should be taken next

## Recommended deck length

Use **9–11 slides** for a standard stakeholder readout. Add technical appendices only when needed.

---

## Slide 1 — Executive Summary

**Purpose:** Lead with the decision.

Include:
- Business question
- Intervention / change evaluated
- Primary KPI movement
- Strength of evidence
- Guardrail summary
- Business impact
- Recommendation

**Standard wording pattern:**

> After the launch of **[intervention]**, **[primary KPI]** changed from **[Pre value]** to **[Post value]**, a **[X percentage-point / X%]** movement. After accounting for **[trend / ramp / seasonality / mix / campaign]**, the evidence suggests **[high / moderate / low]** confidence that the intervention contributed to the change. Guardrails showed **[no material deterioration / specific concern]**. We recommend **[continue / continue with monitoring / iterate / validate further / rollback]**.

---

## Slide 2 — Business Question & Intervention

**Purpose:** Reconnect the analysis to the business decision.

Include:
- What changed
- Launch date
- Why the change matters
- Population affected
- Decision the analysis supports
- Why no randomized Control exists

Avoid starting with statistics. Start with the business problem.

---

## Slide 3 — Measurement Framework

**Purpose:** Show what success and risk mean.

Include:

| KPI Type | Metric | Direction | Why it matters |
|---|---|---|---|
| Primary | [Primary KPI] | Higher/lower | Direct success measure |
| Secondary | [Secondary KPI] | Higher/lower | Explains mechanism |
| Guardrail | [Guardrail KPI] | Stable/better | Detects unintended harm |

Clearly distinguish:
- primary KPI
- secondary/explanatory metrics
- guardrail metrics

---

## Slide 4 — Analysis Design

**Purpose:** Explain how impact was estimated without a Control group.

Include:
- Pre period
- Launch date
- Post period
- Ramp/stabilization period
- Analytical unit
- Inclusion/exclusion rules
- Key limitations

Recommended wording:

> Because the intervention launched to all eligible traffic, this is an observational Pre/Post design. The analysis compares performance before and after launch, then evaluates whether the movement is consistent with the intervention after reviewing trend, seasonality, traffic mix, ramp behavior, and concurrent events.

---

## Slide 5 — Data Quality & Analytical Population

**Purpose:** Establish trust before discussing results.

Include only decision-relevant checks:
- record counts before/after cleaning
- duplicate IDs removed
- missing critical fields
- derived Pre/Post fields
- invalid or anomalous values
- final analytical population

Example table:

| Check | Status | Comment |
|---|---|---|
| Duplicate IDs | Corrected | X duplicates removed |
| Missing critical fields | Corrected / noted | X records affected |
| Date coverage | Pass | Full Pre/Post window present |
| Intervention flags | Re-derived | Based on transaction date |
| Anomalous durations | Corrected for duration analysis | X values excluded from duration metrics |

---

## Slide 6 — Simple Pre/Post Results

**Purpose:** Present what changed descriptively.

Include:
- Pre value
- Post value
- absolute change
- relative change where useful
- confidence interval or p-value when appropriate

Important note:

> This slide describes observed movement. It does not by itself establish causality.

Visual options:
- two-bar chart
- KPI callout table
- small multiples for primary + guardrails

---

## Slide 7 — Trend, Ramp, and Seasonality

**Purpose:** Show whether the movement is consistent with the intervention timing.

Include:
- daily/weekly trend line
- launch annotation
- ramp period annotation
- campaign/concurrent event annotation
- weekday/weekend or seasonal notes

Questions to answer:
- Was the KPI already improving before launch?
- Was there an immediate shift at launch?
- Did performance stabilize after ramp?
- Did a campaign or event overlap with Post?
- Is the Post movement broader than normal variation?

---

## Slide 8 — Confounders & Mix Shift

**Purpose:** Show alternative explanations that were tested.

Include changes in:
- customer tenure mix
- device mix
- country/market mix
- risk tier / customer risk mix
- volume mix
- campaigns or operational changes

Example wording:

> Post-period traffic had a higher share of new customers and high-risk transactions. Because these groups historically have different verification outcomes, the analysis includes mix diagnostics and an adjusted Interrupted Time Series model.

---

## Slide 9 — Interrupted Time Series / Adjusted Evidence

**Purpose:** Move from simple Pre/Post comparison to stronger observational evidence.

Include:
- baseline trend
- immediate level change
- post-launch slope change
- ramp effect
- campaign adjustment
- key covariates

Translate coefficients into business language:

> The adjusted ITS model estimates an immediate lift of approximately **X percentage points** at launch, after accounting for baseline trend, weekday patterns, ramp, campaign timing, and daily traffic mix.

Keep technical detail in the appendix if stakeholders are not technical.

---

## Slide 10 — Guardrails & Trade-Offs

**Purpose:** Confirm whether improvement created unintended harm.

Include:

| Guardrail | Pre | Post | Change | Interpretation |
|---|---:|---:|---:|---|
| Payment decline rate | X | X | X | Stable / concern |
| Support contact rate | X | X | X | Improved / stable |
| Fraud-confirmed rate | X | X | X | Interpret with event counts |

For rare events, always include event counts and avoid overreacting to large relative changes from small bases.

---

## Slide 11 — Recommendation & Next Steps

**Purpose:** Make the decision path explicit.

Choose one:

### Continue / Scale
Use when results are positive, causal evidence is reasonably credible, and guardrails are acceptable.

### Continue with Monitoring
Use when results are positive but causal confidence is moderate or a guardrail requires more observation.

### Iterate
Use when results are promising but concentrated in certain segments or ramp issues should be corrected.

### Validate Further
Use when trend, mix shifts, or concurrent events materially weaken causal interpretation.

### Roll Back / Stop
Use when guardrails deteriorate or business benefit is insufficient.

Include:
- recommendation
- reason
- caveats
- owner
- monitoring window
- metrics to monitor
- trigger thresholds if available

---

## Optional Appendix Slides

### Appendix A — Methodology

Include:
- Pre/Post design rationale
- metric definitions
- statistical methods
- ITS formula
- assumptions
- limitations

### Appendix B — Full Data Quality Details

Include:
- exclusion counts
- missingness
- duplicate handling
- anomalous values
- date coverage
- derived field logic

### Appendix C — Full Segment Tables

Use this for detailed country/device/customer-tenure/risk-tier results.

### Appendix D — Model Output

Include detailed model coefficients for technical reviewers.

---

## Communication Standards

### Do not overstate causality
Avoid saying:

> The launch caused a X% improvement.

Prefer:

> Results are consistent with the launch contributing to improvement, after accounting for trend, ramp, mix, and campaign timing.

Use stronger causal language only when the design supports it.

### Separate observed movement from adjusted evidence
A strong readout distinguishes:

- simple Pre/Post movement
- stable Post movement
- adjusted ITS estimate
- causal-confidence rating

### Use percentage points correctly
If a rate moves from 80% to 84%:

- Absolute change = **+4 percentage points**
- Relative change = **+5%**

Do not use them interchangeably.

### Explain rare events carefully
For low-frequency metrics such as fraud, show event counts and confidence intervals. A large relative change may represent only a few cases.

### End with a decision
Every Pre/Post readout should end with one clear recommendation and a monitoring plan.

---

## Standard Storyline

Every Pre/Post stakeholder readout should answer these questions in order:

1. What decision are we trying to make?
2. What changed and when?
3. What does success mean?
4. Can we trust the data?
5. What changed after launch?
6. Was the change already happening before launch?
7. Could traffic mix or concurrent events explain the result?
8. What does the adjusted evidence suggest?
9. Did any guardrails deteriorate?
10. What is the business impact?
11. What should we do next?
