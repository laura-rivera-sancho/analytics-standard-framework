# Analytics Standard Framework Roadmap

This roadmap distinguishes completed portfolio evidence from planned work and defines a consistent completion standard for every analytical module.

## Status definitions

| Status | Meaning |
|---|---|
| **Planned** | Scope and intended deliverables are documented, but implementation has not started. |
| **In progress** | At least one substantive deliverable exists, but the module does not yet meet the completion standard. |
| **Complete** | The module meets every completion criterion below and is ready for portfolio review. |

Repository-wide improvements such as CI, dependency locking, and licensing are tracked separately. They affect the repository's maturity but do not change whether an individual learning module is analytically complete.

## Module completion standard

A module is marked **Complete** only when it includes:

1. a module README with purpose, navigation, lifecycle, and run instructions
2. a fundamentals guide
3. an end-to-end methodology
4. a synthetic business case and data dictionary
5. a deterministic data generator and compact inspectable sample, when data are required
6. reusable reference analysis code
7. a guided notebook
8. an independent challenge notebook
9. deterministic expected results or an answer key
10. a stakeholder communication template
11. explicit assumptions, limitations, and synthetic-data disclosure
12. successful syntax, link, artifact, and end-to-end workflow validation

A scoring rubric and generated presentation template are encouraged enhancements. Automated repository tests will be introduced as a cross-module quality layer rather than duplicated as a completion requirement.

## Current portfolio status

| Order | Module | Status | Evidence |
|---:|---|---|---|
| 01 | [A/B Testing](01_ab_testing/README.md) | Complete | NovaPay randomized checkout experiment |
| 02 | [Pre/Post Analysis](02_pre_post_analysis/README.md) | Complete | FinFlow observational workflow evaluation |
| 03 | [Target Analysis](03_target_analysis/README.md) | Planned | Scope and deliverable plan documented |
| 04 | [Predictive Analytics](04_predictive_analytics/README.md) | Complete | PayWave capacity-constrained inactivity model |
| 05 | [Ad Hoc Analysis](05_ad_hoc_analysis/README.md) | Planned | Scope and deliverable plan documented |

## Planned Module 03 — Target Analysis

The module will focus on defensible target-population definition, segmentation, eligibility logic, opportunity sizing, prioritization, and activation handoff.

Planned portfolio evidence:

- fundamentals and methodology
- synthetic business case and data dictionary
- population funnel and eligibility rules
- segment sizing and profiling
- prioritization framework with sensitivity analysis
- guided and challenge notebooks
- reference results and stakeholder readout

See the [module plan](03_target_analysis/README.md).

## Planned Module 05 — Ad Hoc Analysis

The module will focus on turning ambiguous stakeholder questions into structured, time-bounded diagnostic analysis without sacrificing data quality or decision clarity.

Planned portfolio evidence:

- intake and problem-framing standard
- KPI tree and hypothesis map
- synthetic diagnostic case
- reproducible exploratory and root-cause workflow
- guided and challenge notebooks
- concise analytical memo or stakeholder readout
- follow-up measurement plan

See the [module plan](05_ad_hoc_analysis/README.md).

## Repository-quality sequence

Repository-wide improvements are tracked separately from analytical module status:

- [x] Centralize the Python environment and pin direct dependencies.
- [x] Add analytical tests, repository-integrity checks, linting, formatting, and GitHub Actions.
- [x] Add licensing, citation metadata, contributor guidance, and contribution templates.
- [x] Standardize finished visible reports, executive previews, and PowerPoint readouts across completed modules.
- [x] Complete the final recruiter-experience, navigation, and accessibility review.
