# Ad Hoc Analysis Methodology

This methodology supports urgent KPI diagnostics without turning the work into an unbounded exploratory exercise.

## 1. Intake and triage

Capture the stakeholder's wording, decision, deadline, business consequence, available actions, and required confidence. Clarify whether the request is diagnostic, causal, predictive, or merely descriptive.

Quality gate: the decision owner confirms what will change based on the answer.

## 2. Write the analysis contract

Define the unit, KPI formula, denominator, time zone, current and comparison periods, completeness window, materiality threshold, dimensions, exclusions, and stopping rule. Record known operational changes without assuming they caused the KPI movement.

Quality gate: a second analyst can reproduce the headline metric from the contract.

## 3. Build the KPI tree and hypothesis map

Express the headline KPI through its mechanical components. Map hypotheses to observable tests, required fields, and possible actions. Prioritize branches by explanatory power, business risk, and time cost.

Quality gate: each initial query tests a named hypothesis or validates the metric.

## 4. Validate the data

Check freshness, grain uniqueness, missingness, category consistency, funnel ordering, impossible values, and definition changes. Preserve the raw quality report. Quarantine invalid rows rather than allowing them to distort rates.

Quality gate: source-to-clean reconciliation is documented and the comparison periods are complete.

## 5. Confirm the headline

Calculate both periods from counts, not averages of subgroup rates. Report numerator, denominator, absolute change, relative change, and materiality. Compare matched weekdays and equal-length windows.

Quality gate: the movement survives definition, completeness, and denominator checks.

## 6. Diagnose the KPI tree

Compare attempt, approval, and post-approval completion rates. Start drill-downs at the stage with the largest credible movement. Keep stable branches in the record so reviewers can see what was ruled out.

Quality gate: the component rates multiply back to the headline KPI in each period.

## 7. Run bounded segment diagnostics

Use only pre-specified operational dimensions. Apply denominator thresholds, compute absolute rate changes, separate within-segment and mix effects, and control the false discovery rate within each dimension family. Track exploratory branches added after seeing the data.

Quality gate: segment contributions reconcile to the overall direction and all tested segments remain visible.

## 8. Triangulate and quantify impact

Estimate the outcome gap using the current denominator and the agreed baseline rate. Use a consistent value assumption. Check an independent operational signal such as support contacts, incident logs, latency, or error codes.

Quality gate: impact is labeled as an estimate and independent evidence supports the prioritized hypothesis.

## 9. Calibrate the conclusion

Organize output into facts, supported hypotheses, unknowns, and excluded explanations. Avoid claiming causation from timing or segment concentration alone. State what evidence would upgrade confidence.

Quality gate: language strength matches the design and evidence.

## 10. Recommend and hand off

Name the immediate mitigation, owner, deadline, rollback criterion, and customer or operational guardrails. Specify the follow-up measurement needed to confirm recovery and isolate cause.

Quality gate: stakeholders can act without reconstructing the analysis.

## 11. Stop and document

Stop when the agreed evidence threshold is met or the timebox expires. Save the intake, metric contract, source snapshot, code, results, tested dimensions, unresolved questions, and follow-up owner.

Quality gate: future analysis can distinguish what was known at decision time from what was learned later.
