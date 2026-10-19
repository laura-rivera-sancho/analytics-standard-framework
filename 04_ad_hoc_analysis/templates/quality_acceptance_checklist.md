# KPI Diagnostic — Quality and Acceptance Checklist

Use this checklist to determine whether a time-bounded KPI diagnostic can support an operational decision.

| Review area | Acceptance evidence |
|---|---|
| Decision and metric contract | Owner, action, deadline, KPI, periods, materiality threshold, and stopping rule are explicit |
| Data validation | Grain, missingness, categories, funnel logic, and source-to-output reconciliation are documented |
| KPI-tree diagnosis | Component identities reconcile and the failing stage is isolated |
| Segment analysis | Dimensions are bounded in advance; denominators, minimum samples, multiplicity, and rate/mix effects are controlled |
| Impact and triangulation | Baseline-based impact is correct and independent operational evidence is considered |
| Interpretation | Observed facts, supported hypotheses, causal limits, and unknowns are separated |
| Recommendation and handoff | Action, owner, reversibility, guardrails, and follow-up measurement are defined |
| Reproducibility | Code, inputs, parameters, and reported outputs can be independently checked |
| Communication | The readout is concise, decision-first, and explicit about remaining uncertainty |

## Readiness assessment

- **Ready for decision-owner review:** evidence supports a bounded action and the remaining uncertainty is visible.
- **Ready with conditions:** immediate direction is useful, but named operational validation is required before escalation.
- **Not ready:** metric, population, diagnostic, or interpretation gaps could materially change the action.
