# Target Analysis Methodology

This workflow is designed for repeatable targeting decisions in which policy eligibility, opportunity size, and limited operational capacity must be reconciled.

## 1. Frame the decision

Write a short decision contract before querying data: action and owner; unit and unique key; as-of date; channel, capacity, and launch date; hard exclusions; intended outcome; guardrails; and review cadence.

Quality gate: a reviewer can state exactly what the list authorizes and what it does not.

## 2. Validate the source population

Check key uniqueness, row counts, field coverage, valid ranges, category normalization, refresh time, and joins. Quarantine impossible records rather than silently imputing hard eligibility fields. Preserve a quality report before cleaning.

Quality gate: the valid population reconciles to the source population through duplicates, quarantines, and retained records.

## 3. Build the eligibility funnel

Apply hard rules sequentially to a common starting population. The order is for audit readability; final eligibility is the logical intersection of all rules. Record remaining and newly excluded counts at every stage.

Quality gate: recomputing all rules simultaneously produces the same final eligible population.

## 4. Profile the eligible population

Describe eligible counts, volume, friction, and coverage by operationally meaningful segments. Include an `Unknown` category rather than dropping missing descriptive dimensions. Compare selection rates later to detect unexpected concentration.

Quality gate: all segment totals reconcile to the eligible population.

## 5. Prioritize transparently

Define decision dimensions before thresholds. In this case, need covers settlement delay, support demand, and payout failures; value covers payment volume; and fit covers mobile readiness, sustainable economics, and low risk.

Document every threshold and point. Apply criteria only after eligibility. Use a deterministic tie-breaker and retain component scores in the activation audit table.

Quality gate: any merchant's score can be recomputed from the exported rules and source snapshot.

## 6. Apply capacity and size opportunity

Select the highest priorities up to capacity. Estimate expected adopters and contribution using tier-level assumptions. Separate known counts from assumed rates and values. Compare at least three capacity scenarios.

Quality gate: the recommendation remains sensible under plausible alternative assumptions, or its dependency is explicitly escalated.

## 7. Review safeguards

Inspect selection rates by operational segments, unknown-data rates, risk mix, and recent-contact suppressions. Geography and industry are monitoring variables here, not scoring inputs. Escalate unexplained disparities and policy exceptions.

Quality gate: decision owner, compliance, operations, and analytics approve the versioned rule set.

## 8. Prepare the activation handoff

Export the minimum fields required for execution plus audit fields: entity key, as-of date, eligibility version, priority rank, score components, tier, and suppression status. Re-run time-sensitive suppressions immediately before send. Set an expiration date.

Quality gate: operations can execute, suppress, reconcile, and roll back the list without an analyst reconstructing it manually.

## 9. Measure impact

Reserve a randomized holdout within actionable priority bands where feasible. Track delivery, contact, adoption, incremental adoption, complaints, opt-outs, operational capacity, and realized contribution. Reconcile activated versus selected records.

Quality gate: the measurement design distinguishes response from incremental impact.

## 10. Govern and refresh

Version source snapshot, code, thresholds, assumptions, approvals, and output checksum. Monitor input drift, funnel movement, segment coverage, and outcome performance. Do not refresh automatically when a policy owner has not approved rule changes.
