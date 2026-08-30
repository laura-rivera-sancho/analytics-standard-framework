# Data & AI Portfolio Roadmap

This roadmap reframes the repository as the foundation of a broader professional portfolio spanning five complementary areas: **Analytics**, **Machine Learning**, **Large Language Models**, **AI Agentic Frameworks**, and **Data Warehousing, Data Marts & Data Modeling**.

The current Analytics Standard Framework is the completed first portfolio pillar. The remaining pillars are staged tracks that will be scoped and delivered as evidence-based case studies rather than collections of disconnected demos.

## Portfolio north star

Each pillar should demonstrate an end-to-end business capability: frame a decision, design the technical approach, implement a reproducible solution, evaluate it honestly, and communicate the outcome to both technical and non-technical audiences.

| Pillar | Portfolio outcome | Current status |
|---|---|---|
| 1. Analytics | Decision-ready analysis across experimentation, change measurement, targeting, prediction, and rapid diagnostics | **Complete** |
| 2. Machine Learning | Production-minded predictive systems with baselines, validation, explainability, deployment thinking, and monitoring | **Planned** |
| 3. Large Language Models | Evaluated LLM applications using retrieval, structured generation, safety controls, and measurable quality | **Planned** |
| 4. AI Agentic Frameworks | Reliable tool-using workflows with orchestration, state, human oversight, observability, and evaluation | **Planned** |
| 5. Data Warehousing, Data Marts & Data Modeling | Governed analytical data products using dimensional models, tested transformations, lineage, and semantic definitions | **Planned** |

## Status definitions

| Status | Meaning |
|---|---|
| **Backlog** | A portfolio opportunity has been captured but not yet scoped. |
| **Planned** | The business case, intended evidence, and acceptance criteria are documented. |
| **In progress** | Implementation has started, but the track does not yet meet its evidence standard. |
| **In review** | The work is complete and undergoing technical, narrative, and recruiter-experience review. |
| **Complete** | The work meets its evidence standard and is ready for portfolio review. |

## Shared portfolio evidence standard

A portfolio case study is marked **Complete** only when it includes, where applicable:

1. a clear business problem, decision, audience, and success criteria
2. documented assumptions, constraints, risks, and ethical considerations
3. an inspectable data source or deterministic synthetic-data generator
4. a reproducible implementation with pinned dependencies
5. a justified baseline and fit-for-purpose evaluation
6. tests for critical logic, data quality, and expected behavior
7. operational considerations such as cost, latency, monitoring, failure modes, and rollback
8. architecture, data-flow, or lifecycle documentation
9. a concise stakeholder readout with findings, limitations, and recommended action
10. a recruiter-friendly README, navigation path, and representative output preview

Pillar-specific criteria extend this standard; they do not replace it.

## Pillar 1 — Analytics

**Objective:** Demonstrate structured decision support across the main analytical workflows used in product, operations, marketing, and strategy teams.

| Module | Status | Portfolio evidence |
|---|---|---|
| [A/B Testing](01_ab_testing/README.md) | Complete | NovaPay randomized checkout experiment |
| [Pre/Post Analysis](02_pre_post_analysis/README.md) | Complete | FinFlow observational workflow evaluation |
| [Target Analysis](03_target_analysis/README.md) | Complete | LuminaPay merchant targeting and activation handoff |
| [Predictive Analytics](04_predictive_analytics/README.md) | Complete | PayWave capacity-constrained inactivity model |
| [Ad Hoc Analysis](05_ad_hoc_analysis/README.md) | Complete | OrbitMart KPI diagnostic and operational handoff |

**Pillar evidence standard:** sound analytical design, reproducible results, decision-relevant interpretation, explicit limitations, and an executive-ready communication artifact.

## Pillar 2 — Machine Learning

**Objective:** Demonstrate how a model progresses from a business need to a reliable and operationally useful system.

Initial portfolio scope:

- an end-to-end supervised learning case with a strong baseline, leakage controls, cross-validation, calibration, explainability, and threshold selection
- a second case that broadens the modeling evidence, such as forecasting, ranking, recommendation, or anomaly detection
- a production-readiness layer covering inference design, experiment tracking, model versioning, drift, performance monitoring, and retraining decisions

**Pillar evidence standard:** comparison against appropriate baselines, reproducible training and inference, decision-aware metrics, error analysis, documented model risks, and a credible monitoring plan.

## Pillar 3 — Large Language Models

**Objective:** Demonstrate LLM applications whose quality is measured, traceable, and grounded in a real workflow.

Initial portfolio scope:

- a retrieval-augmented generation application with ingestion, chunking, retrieval evaluation, citations, and grounded-answer checks
- a structured-generation workflow with schema validation, prompt and model comparisons, and deterministic failure handling
- an evaluation and safety layer covering curated test sets, hallucination checks, prompt-injection resistance, privacy, latency, and cost

**Pillar evidence standard:** explicit task and quality definitions, representative evaluation data, reproducible model configuration, grounded outputs, safety controls, failure analysis, and cost/latency reporting.

## Pillar 4 — AI Agentic Frameworks

**Objective:** Demonstrate dependable multi-step systems that plan or route work, use tools, preserve state, and involve people at appropriate control points.

Initial portfolio scope:

- a tool-using agent that completes a bounded business workflow with typed inputs and outputs
- an orchestrated workflow that demonstrates routing, state management, retries, idempotency, and human approval gates
- an observability and evaluation layer for traces, tool-selection accuracy, task completion, cost, latency, and recovery from failure

**Pillar evidence standard:** clear boundaries for agent autonomy, least-privilege tool access, deterministic controls around side effects, traceable execution, scenario-based evaluation, and documented recovery paths.

## Pillar 5 — Data Warehousing, Data Marts & Data Modeling

**Objective:** Demonstrate how raw operational data becomes trusted, understandable, and reusable analytical data products.

Initial portfolio scope:

- a dimensional warehouse case with declared grain, conformed dimensions, fact tables, slowly changing dimensions, and documented business rules
- tested transformation pipelines with staging, intermediate, and mart layers
- role-oriented data marts and a semantic layer with governed metrics, lineage, freshness, and ownership

**Pillar evidence standard:** defensible modeling choices, reproducible transformations, source-to-target documentation, data-quality tests, lineage, performance considerations, and consistent metric definitions.

## Delivery sequence

The portfolio will be expanded one vertical slice at a time so that every completed increment is independently reviewable:

1. **Foundation complete — Analytics:** retain and maintain the five finished analytical modules.
2. **Next — Machine Learning:** define the first case study and reuse the strongest patterns from the predictive analytics module.
3. **Then — Large Language Models:** build an evaluated LLM application on top of trusted data and retrieval foundations.
4. **Then — AI Agentic Frameworks:** extend the LLM evidence into controlled, tool-using workflows.
5. **Then — Data Architecture:** consolidate warehouse, mart, and modeling evidence into a reusable analytical foundation.

This sequence is directional, not date-bound. Target dates will be added only after the scope and available delivery cadence are agreed.

## GitHub Project workflow

The [Data & AI Portfolio Roadmap](https://github.com/users/laura-rivera-sancho/projects/2) GitHub Project is the execution layer for this roadmap. It provides:

- a **Board** view grouped by status: Backlog, Planned, In progress, In review, and Complete
- a **Roadmap** view for sequencing portfolio tracks once target dates are agreed
- a **Pillar** field using the five portfolio areas above
- lightweight planning fields for Priority, Start date, Target date, and repository linkage

The Markdown roadmap remains the durable portfolio narrative. GitHub Project items track the work needed to deliver it and may evolve more frequently.

## Review gates

Before a new pillar is marked complete, it should pass four reviews:

1. **Technical:** correctness, reproducibility, testing, security, and operational realism
2. **Analytical:** appropriate evaluation, honest limitations, and decision relevance
3. **Communication:** clear narrative, visuals, stakeholder readout, and concise outcomes
4. **Portfolio:** intuitive navigation, representative previews, consistent styling, and no confidential data

## Completed repository foundation

The Analytics pillar already includes centralized dependencies, automated analytical and repository-integrity tests, linting and formatting, GitHub Actions, licensing and citation metadata, contribution guidance, standardized reports, PowerPoint readouts, and a completed recruiter-experience review.
