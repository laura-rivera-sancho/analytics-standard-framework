# Data & AI Portfolio Roadmap

This roadmap defines a five-repository professional portfolio. Each repository represents one capability pillar and contains a small set of connected, end-to-end case studies rather than isolated demos.

The portfolio is organized around two complementary business domains:

- **Growth & Marketing Intelligence:** customer value, experimentation, campaign response, segmentation, and governed marketing data products
- **Market & Trading Intelligence:** macro-market monitoring, cited research, and human-governed paper-trading workflows

## Portfolio architecture

| Pillar | Planned repository | Primary portfolio outcome | Status |
|---|---|---|---|
| 1. Analytics | [`analytics-standard-framework`](https://github.com/laura-rivera-sancho/analytics-standard-framework) | Decision-ready analytics, experimentation, customer insight, and live market monitoring | **In progress** |
| 2. Machine Learning | `machine-learning-standard-framework` | Supervised and unsupervised models tied to measurable business decisions | **Planned** |
| 3. Large Language Models | `llm-systems-framework` | A cited, evaluated trading research copilot | **Planned** |
| 4. AI Agentic Frameworks | `agentic-ai-framework` | A controlled research and paper-trading workflow with mandatory human approval | **Planned** |
| 5. Data Warehousing & Modeling | [`data-architecture-standard-framework`](https://github.com/laura-rivera-sancho/data-architecture-standard-framework) | A governed omnichannel marketing warehouse, marts, and semantic layer | **Complete** |

The three remaining repository names are working names and will become links after those repositories are created. A future GitHub profile README will act as the portfolio landing page, while the [Data & AI Portfolio Roadmap](https://github.com/users/laura-rivera-sancho/projects/2) GitHub Project coordinates work across all five repositories.

## Repository strategy

Use **one repository per pillar**, with multiple related case studies inside it. This keeps each repository substantial enough to show depth while giving recruiters a clear path to the capability they want to assess.

Every repository should include:

- a recruiter-friendly landing page and recommended review path
- case-study folders with business context, data, implementation, tests, and results
- shared utilities only when they are genuinely reused within that pillar
- architecture or workflow documentation
- representative visual previews and an executive-ready readout
- automated quality checks, pinned dependencies, licensing, and citation metadata

## Status definitions

| Status | Meaning |
|---|---|
| **Backlog** | The opportunity is recorded but has not been scoped. |
| **Planned** | The business case, evidence, and acceptance criteria are defined. |
| **In progress** | Implementation has started but does not yet meet the evidence standard. |
| **In review** | The work is undergoing technical, narrative, and recruiter-experience review. |
| **Complete** | The work meets its evidence standard and is ready to share publicly. |

## Shared portfolio evidence standard

A case study is **Complete** only when it includes, where applicable:

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

**Repository:** `analytics-standard-framework`

**Objective:** Demonstrate rigorous analysis that turns business questions into defensible decisions across experimentation, customer strategy, operational diagnosis, and market intelligence.

### Existing foundation

| Case study | Classification | Status | Portfolio evidence |
|---|---|---|---|
| [NovaPay A/B Testing](01_ab_testing/README.md) | Analytics | Complete | Randomized checkout experiment and rollout recommendation |
| [FinFlow Pre/Post Analysis](02_pre_post_analysis/README.md) | Analytics | Complete | Adjusted observational impact evaluation |
| [LuminaPay Target Analysis](03_target_analysis/README.md) | Analytics | Complete | Governed merchant eligibility and prioritization |
| [PayWave Predictive Analytics](04_predictive_analytics/README.md) | **Machine Learning seed case** | Complete | Capacity-constrained inactivity model with temporal validation |
| [OrbitMart Ad Hoc Analysis](05_ad_hoc_analysis/README.md) | Analytics | Complete | KPI diagnosis and operational handoff |

The PayWave module remains in this repository temporarily to preserve working links, tests, and reports. It is now classified as supervised Machine Learning evidence and will be migrated only after the Machine Learning repository foundation exists.

### Planned Analytics milestones

| Milestone | Business question | Core evidence | Status |
|---|---|---|---|
| **A6 — Customer Value & Lifecycle Analytics** | Which customers create the most value, and how should lifecycle treatment differ? | RFM scoring, segment profiles, migration analysis, recommended actions, and an executive dashboard | Complete |
| **A7 — Marketing Experimentation Suite** | Which campaign, message, offer, or channel combination performs best? | Split testing and multivariate testing, power/MDE planning, interaction effects, multiplicity controls, guardrails, and rollout guidance | Complete |
| **A8 — Macro Correlation & Market Context Monitor** | How do Gold, the US 10-year Treasury yield, and the US Dollar Index move across market regimes, and what context should trigger deeper research? | API-based data pipeline, returns/changes, 30/90/252-day rolling correlations, volatility, drawdowns, transparent rules-based context, a live Sites dashboard, and a governed interface for later cited LLM and Agentic AI layers | In review |

The macro dashboard displays source and freshness metadata and clearly states that correlation does not establish causation. The implemented source contract uses COMEX gold futures (`GC=F`), the ICE U.S. Dollar Index (`DX-Y.NYB`), and the Cboe 10-year yield index (`^TNX`), with exact instrument limitations documented in the module.

A8 is the shared market-context foundation for the trading-focused LLM and Agentic AI projects. The Analytics layer owns validated observations, calculations, and reproducible rule labels. The LLM layer will own cited news and macro synthesis; the Agentic layer will own controlled orchestration, risk review, and mandatory human approval. These responsibilities must remain separately identifiable in data contracts and traces.

**Pillar completion gate:** existing Analytics cases remain portfolio-ready, A6–A8 meet the shared evidence standard, and the repository landing page presents the full Analytics review path.

## Pillar 2 — Machine Learning

**Planned repository:** `machine-learning-standard-framework`

**Objective:** Demonstrate supervised and unsupervised modeling from business framing through reliable evaluation, operational decision design, explainability, and monitoring.

### Planned Machine Learning milestones

| Milestone | Use case | Core evidence | Status |
|---|---|---|---|
| **ML1 — Supervised Predictive Modeling** | Predict campaign response and allocate limited marketing capacity | Logistic-regression baseline, simple decision tree, tree-based champion, leakage controls, temporal/cross-validation design, calibration, lift/gains, threshold economics, explainability, and monitoring | Planned |
| **ML1 transfer case — PayWave Inactivity** | Prioritize retention outreach under capacity constraints | Migrate or adapt the completed PayWave case to prove the supervised framework transfers across domains | Planned |
| **ML2 — Unsupervised Customer Segmentation** | Discover stable, actionable customer groups beyond fixed RFM rules | RFM/behavioral features, K-means baseline, Gaussian-mixture comparison, density-based challenger, stability checks, interpretable personas, and activation guidance | Planned |
| **ML3 — Production Readiness** | How would the selected models be operated responsibly? | Reproducible training/inference, model registry approach, drift and performance monitoring, retraining triggers, rollback, and model card | Planned |

The campaign-response case is the primary supervised marketing project. PayWave is retained as a transfer case, not discarded. The unsupervised project extends the RFM work from descriptive customer rules into data-driven segmentation.

**Pillar completion gate:** both modeling paradigms have defensible baselines, reproducible evaluation, decision-aware metrics, error/stability analysis, documented risks, and credible monitoring plans.

### Proposed repository structure

```text
machine-learning-standard-framework/
├── supervised_learning/
│   ├── campaign_response_propensity/
│   └── paywave_inactivity/
├── unsupervised_learning/
│   └── customer_segmentation/
├── shared/
├── tests/
└── README.md
```

## Pillar 3 — Large Language Models

**Planned repository:** `llm-systems-framework`

**Objective:** Build a cited trading research copilot that synthesizes evidence without presenting unsupported claims or autonomous investment instructions.

### Planned LLM milestones

| Milestone | Capability | Core evidence | Status |
|---|---|---|---|
| **LLM1 — Research Corpus & Retrieval** | Retrieve relevant filings, macro releases, approved news, and research sources around the A8 market context | Document ingestion, publisher/source policy, metadata, chunking, hybrid retrieval, reranking, source traceability, and retrieval evaluation | Planned |
| **LLM2 — Cited Trading Research Copilot** | Produce a structured, evidence-grounded research brief | Thesis, counter-thesis, catalysts, risks, uncertainty, citations, numerical grounding, and schema-validated output | Planned |
| **LLM3 — Evaluation, Safety & Operations** | Measure answer quality and control failure modes | Curated evaluation set, citation correctness, groundedness, hallucination and prompt-injection tests, privacy, latency, cost, and failure handling | Planned |

The copilot is a research system, not a buy/sell signal generator. It should distinguish retrieved facts, model synthesis, and unresolved uncertainty.

**Pillar completion gate:** representative evaluations demonstrate useful retrieval, valid citations, grounded claims, predictable structured output, safety controls, and transparent cost/latency reporting.

## Pillar 4 — AI Agentic Frameworks

**Planned repository:** `agentic-ai-framework`

**Objective:** Demonstrate a dependable market-research and paper-trading workflow in which tools and agents can prepare actions but a person must approve every order submission.

### Planned Agentic AI milestones

| Milestone | Capability | Core evidence | Status |
|---|---|---|---|
| **AG1 — Governed Research Workflow** | Consume the A8 market-context payload and coordinate bounded specialist tasks for market and company research | Typed inputs/outputs, freshness validation, source policy, routing, state, tool permissions, retries, timeouts, and traceable synthesis | Planned |
| **AG2 — Risk Review & Trade Proposal** | Convert an approved research thesis into a constrained paper-trade proposal | Position and exposure limits, freshness checks, policy validation, risk-agent review, rejection reasons, and immutable proposal record | Planned |
| **AG3 — Mandatory Human Approval & Paper Execution** | Submit a paper order only after explicit human authorization | Approval checkpoint, separation of proposal and execution, idempotency, audit trail, paper-broker sandbox, and kill switch | Planned |
| **AG4 — Observability & Scenario Evaluation** | Prove the workflow behaves safely under normal and failure conditions | Trace review, tool-selection accuracy, completion rate, cost/latency, stale-data and tool-failure scenarios, denied approval, duplicate request, and recovery tests | Planned |

**Non-negotiable boundary:** no live trading. The system may research, draft, validate, and simulate, but it must never submit even a paper order without a recorded human approval.

**Pillar completion gate:** the system demonstrates least-privilege access, deterministic controls around side effects, mandatory human approval, traceable execution, failure recovery, and scenario-based evaluation.

## Pillar 5 — Data Warehousing, Data Marts & Data Modeling

**Repository:** [`data-architecture-standard-framework`](https://github.com/laura-rivera-sancho/data-architecture-standard-framework)

**Objective:** Build a governed omnichannel marketing data platform that supports the Analytics and Machine Learning marketing cases with trusted, reusable data products.

### Completed Data Architecture milestones

| Milestone | Capability | Core evidence | Status |
|---|---|---|---|
| **DA1 — Source Contracts & Staging** | Standardize customer, order, campaign, experiment, and behavioral event data | Source contracts, ingestion assumptions, staging models, identifiers, freshness rules, and data-quality tests | Complete |
| **DA2 — Dimensional Warehouse** | Create a defensible cross-channel analytical model | Declared grain; order, item, touchpoint, exposure, and event facts; conformed customer, product, campaign, channel, and date dimensions; slowly changing dimensions | Complete |
| **DA3 — Business Data Marts** | Serve consistent data for specific analytical decisions | `customer_360`, `rfm_segments`, `campaign_performance`, `experiment_results`, `ml_features`, and `executive_growth` marts | Complete |
| **DA4 — Semantic Governance & Operations** | Make metrics trusted and maintainable | Governed metric definitions, lineage, ownership, tests, documentation, performance, freshness monitoring, and change management | Complete |

**Pillar completion gate:** transformations are reproducible and tested, business grain and rules are explicit, lineage is inspectable, metrics are consistent, and the marts directly support at least the RFM, experimentation, and campaign-response cases.

## Cross-pillar delivery sequence

The build order follows data and capability dependencies while delivering independently reviewable increments:

1. **Portfolio foundation:** maintain the completed case studies and update the profile-level portfolio navigation.
2. **Marketing data foundation:** build the warehouse core and the customer/campaign/experiment marts needed by downstream work.
3. **RFM analytics:** deliver Customer Value & Lifecycle Analytics on the trusted customer mart.
4. **Marketing experimentation:** deliver the split and multivariate testing suite.
5. **Supervised Machine Learning:** deliver campaign response propensity, then migrate/adapt PayWave as a transfer case.
6. **Unsupervised Machine Learning:** extend RFM into stable, actionable customer segmentation.
7. **Macro market dashboard:** deliver the Gold–US10Y–DXY correlation monitor and live site.
8. **Cited LLM research copilot:** build and evaluate the trading research workflow.
9. **Human-governed agentic workflow:** add risk review, mandatory approval, and paper execution only after the LLM research foundation is reliable.
10. **Portfolio consolidation:** complete cross-repository navigation, consistent visual identity, final recruiter review, and public-launch readiness.

This sequence is directional, not date-bound. Dates will be added only after delivery cadence and project scope are agreed.

## GitHub Project workflow

The [Data & AI Portfolio Roadmap](https://github.com/users/laura-rivera-sancho/projects/2) GitHub Project is the cross-repository execution layer. It should use:

- **Board:** Backlog, Planned, In progress, In review, and Complete
- **Roadmap:** sequencing by Start date and Target date once dates are agreed
- **Pillar:** Analytics, Machine Learning, Large Language Models, AI Agentic Frameworks, and Data Warehouse & Modeling
- **Priority:** High, Medium, or Low
- **Repository:** the pillar repository that owns the work

Project items should represent the milestones above, not duplicate every technical task. Repository issues can hold implementation-level work and be linked to the appropriate milestone.

The Markdown roadmap is the durable portfolio narrative; the GitHub Project tracks execution and may change more frequently.

## Review gates

Before a case study or pillar is marked complete, it must pass four reviews:

1. **Technical:** correctness, reproducibility, testing, security, and operational realism
2. **Analytical:** appropriate evaluation, honest limitations, and decision relevance
3. **Communication:** clear narrative, visuals, stakeholder readout, and concise outcomes
4. **Portfolio:** intuitive navigation, representative previews, consistent styling, and no confidential data

The portfolio and GitHub Project will remain private until these review gates are complete and the work is ready for a coordinated public launch.
