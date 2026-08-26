# Target Analysis Standard Framework

> **Status: Planned.** This page documents the intended scope and completion criteria. Analysis code, data, and results have not been added yet.

This module will define a repeatable process for identifying, sizing, describing, and prioritizing a target population for a specific business action.

## Intended business questions

The framework will support questions such as:

- Which customers, merchants, products, or locations are eligible for an initiative?
- How large is the realistically addressable opportunity?
- Which segments contribute most to the opportunity or risk?
- How should a limited budget or operational capacity be prioritized?
- What measurement plan is required after activation?

## Planned analytical lifecycle

1. Define the business action and decision owner.
2. Define the unit of analysis and as-of date.
3. Translate policy and business rules into reproducible eligibility criteria.
4. Build the population funnel from total population to addressable target.
5. Validate data coverage, exclusions, overlaps, and denominator consistency.
6. Size the opportunity using transparent assumptions.
7. Profile meaningful segments without confusing description with causation.
8. Define prioritization tiers under capacity or budget constraints.
9. Test sensitivity to thresholds, missing data, and uncertain assumptions.
10. Produce an activation-ready target definition and measurement handoff.

## Planned portfolio deliverables

- `target_analysis_fundamentals.md`
- `methodology.md`
- `case_study/business_case.md`
- `case_study/data_dictionary.md`
- `case_study/expected_results.md`
- compact synthetic sample data
- deterministic data generator
- reusable target-sizing and segmentation analysis
- guided notebook
- independent challenge notebook
- stakeholder readout template

## Boundaries with other modules

- Use [A/B Testing](../01_ab_testing/README.md) when the primary question is whether an intervention caused an outcome.
- Use [Pre/Post Analysis](../02_pre_post_analysis/README.md) when evaluating a change without randomized control.
- Use [Predictive Analytics](../04_predictive_analytics/README.md) when estimating a future individual-level outcome from historical data.
- Use Target Analysis when the immediate need is to define, size, profile, and prioritize an actionable population.

## Completion rule

This module will remain **Planned** until substantive implementation begins and will not be marked **Complete** until it satisfies the repository-wide [module completion standard](../ROADMAP.md#module-completion-standard).
