# Customer Value & Lifecycle Methodology

## 1. Frame the decision

Declare the audience, action, capacity, analysis date, lookback window, customer grain, value measure, and guardrails before calculating segments. RFM is appropriate for treatment design when purchase history is the relevant behavior; it is not a substitute for incremental-response modeling.

Quality gate: a reviewer can state what action the analysis authorizes and what it does not.

## 2. Validate the analytical input

Check order-key uniqueness, customer identifiers, timestamps, recognized revenue, customer creation dates, acquisition dimensions, and consent. Quarantine nonpositive revenue, future orders, unparseable dates, and transactions before customer creation. Preserve a defect report.

Quality gate: source rows reconcile through duplicates, invalid transactions, and retained clean records.

## 3. Establish a point-in-time snapshot

Fix an `as_of_date` and use only information available by that date. Calculate frequency and monetary value over the trailing 365 days; calculate recency from the latest known order. Keep the cutoff explicit so repeated runs are comparable and future information cannot leak backward.

Quality gate: one row exists per eligible customer and every feature respects the cutoff.

## 4. Score RFM dimensions

Rank recency, frequency, and monetary value into five population-relative bands. Higher scores always mean more favorable behavior. Use deterministic tie handling, retain the underlying measures, and reserve the lowest frequency and monetary scores for customers without lookback activity.

Quality gate: every score is between one and five and can be recomputed from the snapshot.

## 5. Assign interpretable segments

Map score combinations into Champions, Loyal Customers, New or Potential, At Risk, Hibernating, and Needs Attention. Segment rules must remain simple enough for a stakeholder to audit and stable enough to compare across snapshots.

Quality gate: segment counts and value reconcile to the customer snapshot.

## 6. Profile value and contactability

For each segment, report customer count and share, average recency, frequency, customer value, total value, value share, and consented customers. Avoid equating high historical value with future incremental opportunity.

Quality gate: customer and value shares each sum to 100%.

## 7. Measure lifecycle migration

Recreate the same segmentation at a prior cutoff and compare customer-level assignments. Label movements as improved, declined, or stable using an explicit ordinal interpretation. Show transition counts and value, while acknowledging that score thresholds shift with the population.

Quality gate: every current customer appears once in the migration table.

## 8. Prioritize a controlled action

Restrict candidates to consented At Risk and Needs Attention customers. Rank transparently using monetary, frequency, and disengagement evidence; use customer ID as a deterministic tie-breaker. Apply capacity only after eligibility.

Quality gate: the selected audience contains only eligible customers, never exceeds capacity, and includes all scoring components.

## 9. Measure and govern

Randomize a holdout within comparable priority bands. Track delivery, conversion, incremental recognized revenue, unsubscribe and complaint rates, offer cost, and segment coverage. Version the cutoff, rules, capacity, consent snapshot, code, and output checksum.

Quality gate: rollout decisions use incremental evidence and guardrails rather than raw response alone.
