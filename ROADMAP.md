# Data & AI Evidence and Readiness Map

This document maps the evidence available across five connected capability pillars. Each repository contains end-to-end case studies or working implementations rather than isolated demos.

The portfolio is organized around two complementary business domains:

- **Growth & Marketing Intelligence:** customer value, experimentation, campaign response, segmentation, and governed marketing data products
- **Market & Trading Intelligence:** macro-market monitoring, cited research, and human-governed paper-trading workflows

## Portfolio architecture

| Pillar | Planned repository | Primary portfolio outcome | Status |
|---|---|---|---|
| 1. Analytics | [`analytics-standard-framework`](https://github.com/laura-rivera-sancho/analytics-standard-framework) | Decision-ready analytics, experimentation, customer insight, and live market monitoring | **Evidence available** |
| 2. Machine Learning | [`machine-learning-standard-framework`](https://github.com/laura-rivera-sancho/machine-learning-standard-framework) | Supervised and unsupervised models tied to measurable business decisions | **Evidence available** |
| 3. Large Language Models | `llm-systems-framework` | A cited, evaluated trading research copilot | **Planned** |
| 4. AI Agentic Frameworks | `agentic-ai-framework` | A controlled research and paper-trading workflow with mandatory human approval | **Planned** |
| 5. Data Warehousing & Modeling | [`data-architecture-standard-framework`](https://github.com/laura-rivera-sancho/data-architecture-standard-framework) | A governed omnichannel marketing warehouse, marts, and semantic layer | **Evidence available** |

The two remaining repository names are working names and will become links after those repositories are created. The GitHub profile README acts as the public portfolio landing page; detailed implementation sequencing remains an internal delivery artifact.

## Repository strategy

Use **one repository per pillar**, with multiple related case studies inside it. This gives readers a clear path from general methods to worked examples and implementation details.

Every repository should include:

- a clear repository landing page and portfolio navigation path
- case-study folders with business context, data, implementation, tests, and results
- shared utilities only when they are genuinely reused within that pillar
- architecture or workflow documentation
- representative visual previews and an executive-ready readout
- automated quality checks, pinned dependencies, licensing, and citation metadata

## Evidence and readiness labels

| Status | Meaning |
|---|---|
| **Backlog** | The opportunity is recorded but has not been scoped. |
| **Planned** | The business case, evidence, and acceptance criteria are defined. |
| **In progress** | Implementation has started but does not yet meet the evidence standard. |
| **In review** | The work is undergoing technical, narrative, and reader-experience review. |
| **Evidence available** | A public implementation, validation evidence, limitations, and decision artifact are available for inspection. |

## Shared portfolio evidence standard

A case study is **ready for public review** when it includes, where applicable:

1. a clear business problem, decision, audience, and success criteria
2. documented assumptions, constraints, risks, and ethical considerations
3. an inspectable data source or deterministic synthetic-data generator
4. a reproducible implementation with pinned dependencies
5. a justified baseline and fit-for-purpose evaluation
6. tests for critical logic, data quality, and expected behavior
7. operational considerations such as cost, latency, monitoring, failure modes, and rollback
8. architecture, data-flow, or lifecycle documentation
9. a concise stakeholder readout with findings, limitations, and recommended action
10. a clear README, navigation path, and representative output preview

Pillar-specific criteria extend this standard; they do not replace it.

## Pillar 1 — Analytics

**Repository:** `analytics-standard-framework`

**Objective:** Demonstrate rigorous analysis that turns business questions into defensible decisions across experimentation, customer strategy, operational diagnosis, and market intelligence.

### Existing foundation

| Case study | Classification | Evidence status | Portfolio evidence |
|---|---|---|---|
| [NovaPay A/B Testing](01_ab_testing/README.md) | Analytics | Evidence available | Randomized checkout experiment and rollout recommendation |
| [FinFlow Pre/Post Analysis](02_pre_post_analysis/README.md) | Analytics | Evidence available | Adjusted observational impact evaluation |
| [LuminaPay Target Analysis](03_target_analysis/README.md) | Analytics | Evidence available | Governed merchant eligibility and prioritization |
| [OrbitMart Ad Hoc Analysis](04_ad_hoc_analysis/README.md) | Analytics | Evidence available | KPI diagnosis and operational handoff |

### Implemented Analytics capabilities

| Capability | Business question | Core evidence | Evidence status |
|---|---|---|---|
| **A6 — Customer Value & Lifecycle Analytics** | Which customers create the most value, and how should lifecycle treatment differ? | RFM scoring, segment profiles, migration analysis, recommended actions, and an executive dashboard | Evidence available |
| **A7 — Marketing Experimentation Suite** | Which campaign, message, offer, or channel combination performs best? | Split testing and multivariate testing, power/MDE planning, interaction effects, multiplicity controls, guardrails, and rollout guidance | Evidence available |
| **A8 — Macro Correlation & Market Context Monitor** | How do Gold, the US 10-year Treasury yield, and the US Dollar Index move across market regimes, and what context should trigger deeper research? | API-based data pipeline, returns/changes, 30/90/252-day rolling correlations, volatility, drawdowns, transparent rules-based context, a live Sites dashboard, and a governed interface for later cited LLM and Agentic AI layers | Evidence available |

The macro dashboard displays source and freshness metadata and clearly states that correlation does not establish causation. The implemented source contract uses COMEX gold futures (`GC=F`), the ICE U.S. Dollar Index (`DX-Y.NYB`), and the Cboe 10-year yield index (`^TNX`), with exact instrument limitations documented in the module.

A8 is the shared market-context foundation for the trading-focused LLM and Agentic AI projects. The Analytics layer owns validated observations, calculations, and reproducible rule labels. The LLM layer will own cited news and macro synthesis; the Agentic layer will own controlled orchestration, risk review, and mandatory human approval. These responsibilities must remain separately identifiable in data contracts and traces.

**Readiness evidence:** the Analytics cases meet the shared evidence standard, and the repository landing page provides a buyer-first review path.

## Pillar 2 — Machine Learning

**Repository:** [`machine-learning-standard-framework`](https://github.com/laura-rivera-sancho/machine-learning-standard-framework)

**Objective:** Demonstrate supervised and unsupervised modeling from business framing through reliable evaluation, operational decision design, explainability, and monitoring.

### Machine Learning capabilities

| Capability | Use case | Core evidence | Evidence status |
|---|---|---|---|
| **ML1 — Campaign Response Propensity** | Predict campaign response and allocate limited marketing capacity | Logistic-regression baseline, simple decision tree, tree-based champion, leakage controls, temporal validation, calibration, lift/gains, threshold economics, explainability, and monitoring | **Evidence available** |
| [**ML2 — Unsupervised Customer Segmentation**](https://github.com/laura-rivera-sancho/machine-learning-standard-framework/tree/main/unsupervised_learning/customer_segmentation) | Discover stable, actionable customer groups beyond fixed RFM rules | RFM/behavioral features, K-means baseline, Gaussian-mixture comparison, density-based challenger, bootstrap and temporal stability, interpretable personas, and activation guidance | **Evidence available** |
| **ML3 — Production Readiness** | How should the selected models be operated responsibly? | Training/inference contracts, registry approach, monitoring, retraining, rollback, operating runbooks, executable release validation, and executive readout | **Evidence available** |

The campaign-response case is the primary supervised marketing project, and ML2 extends the RFM work from descriptive customer rules into stable, data-driven segmentation.

**Readiness evidence:** both modeling paradigms have defensible baselines, reproducible evaluation, decision-aware metrics, error/stability analysis, documented risks, and credible monitoring plans. The PayWave transfer case and ML3 operating controls add supporting evidence.

### Proposed repository structure

```text
machine-learning-standard-framework/
├── supervised_learning/
│   └── campaign_response_propensity/
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

**Readiness evidence required:** representative evaluations must demonstrate useful retrieval, valid citations, grounded claims, predictable structured output, safety controls, and transparent cost/latency reporting.

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

**Readiness evidence required:** the system must demonstrate least-privilege access, deterministic controls around side effects, mandatory human approval, traceable execution, failure recovery, and scenario-based evaluation.

## Pillar 5 — Data Warehousing, Data Marts & Data Modeling

**Repository:** [`data-architecture-standard-framework`](https://github.com/laura-rivera-sancho/data-architecture-standard-framework)

**Objective:** Build a governed omnichannel marketing data platform that supports the Analytics and Machine Learning marketing cases with trusted, reusable data products.

### Implemented Data Architecture capabilities

| Capability | Outcome | Core evidence | Evidence status |
|---|---|---|---|
| **DA1 — Source Contracts & Staging** | Standardize customer, order, campaign, experiment, and behavioral event data | Source contracts, ingestion assumptions, staging models, identifiers, freshness rules, and data-quality tests | Evidence available |
| **DA2 — Dimensional Warehouse** | Create a defensible cross-channel analytical model | Declared grain; order, item, touchpoint, exposure, and event facts; conformed customer, product, campaign, channel, and date dimensions; slowly changing dimensions | Evidence available |
| **DA3 — Business Data Marts** | Serve consistent data for specific analytical decisions | `customer_360`, `rfm_segments`, `campaign_performance`, `experiment_results`, `ml_features`, and `executive_growth` marts | Evidence available |
| **DA4 — Semantic Governance & Operations** | Make metrics trusted and maintainable | Governed metric definitions, lineage, ownership, tests, documentation, performance, freshness monitoring, and change management | Evidence available |

**Readiness evidence:** transformations are reproducible and tested, business grain and rules are explicit, lineage is inspectable, metrics are consistent, and the marts directly support the RFM, experimentation, and campaign-response cases.

## Cross-pillar delivery sequence

The build order follows data and capability dependencies while delivering independently reviewable increments:

1. **Portfolio foundation:** maintain the completed case studies and update the profile-level portfolio navigation.
2. **Marketing data foundation:** build the warehouse core and the customer/campaign/experiment marts needed by downstream work.
3. **RFM analytics:** deliver Customer Value & Lifecycle Analytics on the trusted customer mart.
4. **Marketing experimentation:** deliver the split and multivariate testing suite.
5. **Supervised Machine Learning:** deliver campaign response propensity with decision-aware evaluation and monitoring.
6. **Unsupervised Machine Learning:** extend RFM into stable, actionable customer segmentation.
7. **Macro market dashboard:** deliver the Gold–US10Y–DXY correlation monitor and live site.
8. **Cited LLM research copilot:** build and evaluate the trading research workflow.
9. **Human-governed agentic workflow:** add risk review, mandatory approval, and paper execution only after the LLM research foundation is reliable.
10. **Portfolio consolidation:** complete cross-repository navigation, consistent visual identity, final content review, and public-launch readiness.

This sequence is directional, not date-bound. Dates will be added only after delivery cadence and project scope are agreed.

## Internal delivery workflow

The internal cross-repository delivery board should use:

- **Board:** Backlog, Planned, In progress, In review, and Complete
- **Roadmap:** sequencing by Start date and Target date once dates are agreed
- **Pillar:** Analytics, Machine Learning, Large Language Models, AI Agentic Frameworks, and Data Warehouse & Modeling
- **Priority:** High, Medium, or Low
- **Repository:** the pillar repository that owns the work

Project items should represent the capabilities above, not duplicate every technical task. Repository issues can hold implementation-level work and be linked to the appropriate capability.

The Markdown roadmap is the durable portfolio narrative; the GitHub Project tracks execution and may change more frequently.

## Evidence review

Before a case study or pillar is presented as decision-ready evidence, it must pass four reviews:

1. **Technical:** correctness, reproducibility, testing, security, and operational realism
2. **Analytical:** appropriate evaluation, honest limitations, and decision relevance
3. **Communication:** clear narrative, visuals, stakeholder readout, and concise outcomes
4. **Portfolio:** intuitive navigation, representative previews, consistent styling, and no confidential data

The completed Analytics, Machine Learning, and Data Architecture repositories are public. Planned LLM and Agentic AI repositories should be published only after their applicable review gates are complete.
