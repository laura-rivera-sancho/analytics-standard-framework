# Target Analysis — Quality and Acceptance Checklist

Use this checklist to determine whether a targeting analysis is ready for activation review.

| Review area | Acceptance evidence |
|---|---|
| Decision framing | Action, owner, unit, as-of date, capacity, intended outcome, and guardrails are explicit |
| Data quality | Defects are measured, treatment is justified, and source-to-clean counts reconcile |
| Eligibility | Hard rules are auditable, ordered, separated from priority logic, and reconcile to a stable denominator |
| Prioritization | Need, value, and fit logic is interpretable; missing values and tie-breaking are deterministic |
| Opportunity sizing | Counts are separated from planning assumptions and alternative capacity scenarios are correct |
| Coverage and sensitivity | Selection patterns are reviewed descriptively and material tradeoffs are visible |
| Activation governance | Suppressions, minimization, versioning, approvals, expiry, ownership, and allowed uses are documented |
| Measurement | A holdout or other credible design is specified before incremental impact is claimed |
| Communication | Recommendation, limitations, owners, and next decision are concise and prominent |

## Readiness assessment

- **Ready for controlled activation:** analytical evidence, governance controls, and measurement design are complete.
- **Ready with conditions:** the audience is defensible, but named approvals or operational controls remain open.
- **Not ready:** population, assumptions, governance, or handoff cannot yet support action.
