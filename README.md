# Analytics Standard Framework

[![Repository quality](https://github.com/laura-rivera-sancho/analytics-standard-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/laura-rivera-sancho/analytics-standard-framework/actions/workflows/ci.yml)

**A portfolio-ready analytics operating model for turning business questions into reproducible analysis, defensible decisions, and stakeholder communication.**

This repository demonstrates how I approach common analytics engagements from end to end: framing the decision, defining metrics and assumptions, validating data, selecting an appropriate method, interpreting uncertainty, estimating business impact, and communicating a recommendation.

Each module combines a reusable methodology with a fictional business case, inspectable data, reproducible implementation, practical learning material where relevant, and an executive communication standard. No employer, client, or confidential data are used.

## Recommended portfolio review path

If you are reviewing this repository for a role or project, these links provide
the fastest route to the strongest evidence:

| What to assess | Start here | What it demonstrates |
|---|---|---|
| Decision communication | [NovaPay A/B testing readout](01_ab_testing/reports/stakeholder_readout.md) | Experiment validity, effect size, guardrails, and a rollout recommendation |
| Causal judgment | [FinFlow Pre/Post readout](02_pre_post_analysis/reports/stakeholder_readout.md) | Interrupted time series, confounder review, limitations, and risk monitoring |
| Target-population design | [LuminaPay targeting readout](03_target_analysis/reports/stakeholder_readout.md) | Eligibility governance, opportunity sizing, transparent prioritization, and activation controls |
| Predictive decision design | [PayWave modeling readout](04_predictive_analytics/reports/stakeholder_readout.md) | Temporal validation, capacity metrics, business value, and a controlled-pilot plan |
| Diagnostic judgment | [OrbitMart ad hoc readout](05_ad_hoc_analysis/reports/stakeholder_readout.md) | KPI trees, rate-and-mix decomposition, exploratory controls, and evidence-calibrated action |
| Customer value strategy | [Harbor & Pine lifecycle readout](06_customer_value_lifecycle/reports/stakeholder_readout.md) | RFM value concentration, lifecycle migration, consent-aware prioritization, and test design |
| Marketing experimentation | [Harbor & Pine experimentation readout](07_marketing_experimentation/reports/stakeholder_readout.md) | Power planning, randomization checks, factorial effects, multiplicity control, economics, and rollout governance |
| Live macro intelligence | [Private live Macro Correlation Monitor](https://macro-correlation-monitor.nachilu10.chatgpt.site) | Live API integration, rolling relationships, transparent market context, and a governed foundation for cited LLM and Agentic AI research |
| Reproducible implementation | [Source workflows](01_ab_testing/src) and [automated tests](tests) | Reusable Python, deterministic data, analytical tests, and repository checks |
| Portfolio scope and milestones | [Roadmap](ROADMAP.md) | Five-repository architecture, planned case studies, completion criteria, and delivery sequence |

## What this project demonstrates

- **Business problem framing** — translating broad requests into decision-ready analytical questions.
- **Experimentation and causal reasoning** — distinguishing randomized evidence from observational comparisons.
- **Statistical analysis** — effect sizes, confidence intervals, hypothesis tests, guardrails, and practical significance.
- **Predictive modeling** — leakage-safe features, temporal validation, calibration, capacity-aware evaluation, and business value.
- **Target design** — auditable eligibility rules, denominator-consistent funnels, opportunity sizing, and capacity allocation.
- **Diagnostic analysis** — KPI trees, bounded exploration, rate-and-mix decomposition, and time-boxed decision support.
- **Customer value analytics** — RFM scoring, value concentration, lifecycle migration, and controlled activation design.
- **Marketing experimentation** — split and factorial testing, power planning, multiplicity control, guardrails, and decision-stage governance.
- **Macro correlation analysis** — live market data, returns and yield-change transformations, rolling-window comparisons, and regime-aware interpretation.
- **Data quality** — deliberate validation of duplicates, missingness, invalid values, inconsistent categories, and timing logic.
- **Reproducible analytics** — deterministic synthetic-data generators, reusable analysis functions, and documented assumptions.
- **Stakeholder communication** — concise recommendations that separate evidence, limitations, and next actions.

## Featured case studies

| Case study | Business decision | Analytical approach | Portfolio evidence |
|---|---|---|---|
| **NovaPay** | Should a simplified checkout experience be rolled out? | Randomized A/B test | [Finished stakeholder readout](01_ab_testing/reports/stakeholder_readout.md): **+3.31 pp** completion lift, 95% CI **+2.45 to +4.17 pp**, with materially lower checkout time. |
| **FinFlow** | Should an automated verification workflow continue scaling? | Pre/Post analysis and adjusted interrupted time series | [Finished stakeholder readout](02_pre_post_analysis/reports/stakeholder_readout.md): **+5.65 pp** observed completion change and **+3.20 pp** adjusted launch-level estimate, with moderate causal confidence. |
| **LuminaPay** | Which eligible merchants should receive limited Instant Settlement outreach? | Rule-based target analysis and capacity sensitivity | [Finished stakeholder readout](03_target_analysis/reports/stakeholder_readout.md): **25,805** eligible merchants and a controlled **6,000-contact** first wave with explicit activation safeguards. |
| **PayWave** | Which customers should receive capacity-constrained retention outreach? | Temporal binary-classification workflow | [Finished stakeholder readout](04_predictive_analytics/reports/stakeholder_readout.md): **3,853** captures at capacity—**552 more** than the recency rule—with **77.06% precision** and **2.58x lift**. |
| **OrbitMart** | Why did checkout completion fall while traffic increased? | KPI-tree diagnosis, rate/mix decomposition, and controlled segment drill-down | [Finished stakeholder readout](05_ad_hoc_analysis/reports/stakeholder_readout.md): **−0.97 pp** completion decline localized to Android 8.4 wallet traffic, with an estimated **254-order** gap. |
| **Harbor & Pine** | Which customer groups create the most value, and where should limited retention capacity focus? | Point-in-time RFM scoring, lifecycle migration, and consent-aware prioritization | [Finished stakeholder readout](06_customer_value_lifecycle/reports/stakeholder_readout.md): Champions are **23.1%** of customers but **55.5%** of value; a controlled **500-customer** first wave represents **$323.2K** in trailing-year value. |
| **Harbor & Pine Experimentation** | Which retention treatment should advance without approving broad rollout? | Split test and `2 × 2 × 2` factorial experiment | [Finished stakeholder readout](07_marketing_experimentation/reports/stakeholder_readout.md): the leading cell improves conversion by **+2.67 pp** after Holm correction, while margin uncertainty requires a controlled validation stage. |
| **Macro Correlation Monitor** | When have gold's relationships with DXY and US10Y shifted enough to warrant deeper research? | Live API pipeline, rolling cross-asset correlation, and rules-based market context | [Interactive module](08_macro_correlation_monitor/README.md): selectable **30/90/252-day** views, exact source/freshness metadata, deterministic fallback behavior, and a governed handoff to later cited LLM and Agentic AI layers. |

### NovaPay decision snapshot

| KPI | Control | Treatment | Decision signal |
|---|---:|---:|---|
| Checkout completion | 72.64% | 75.95% | +3.31 pp; statistically credible and above the assumed business threshold |
| Mean checkout time | ~89.35 sec | ~64.16 sec | Material reduction in customer friction |
| Support contact rate | 5.655% | 4.570% | Favorable guardrail movement |
| Payment decline rate | 5.495% | 5.180% | Small reduction; not statistically conclusive |
| Fraud rate | 0.355% | 0.350% | No meaningful difference detected |

**Recommendation:** proceed toward rollout with continued monitoring of fraud, payment declines, and segment stability. See the [finished stakeholder readout](01_ab_testing/reports/stakeholder_readout.md), [full reference results](01_ab_testing/case_study/expected_results.md), and [guided analysis](01_ab_testing/notebooks/guided_ab_test_analysis.ipynb).

### FinFlow decision snapshot

The simple Pre/Post comparison is intentionally not treated as proof of causality. The workflow re-derives launch timing, separates the seven-day stabilization ramp, examines traffic-mix changes, and estimates an adjusted interrupted time-series model with baseline trend, weekday, campaign, ramp, and customer-mix controls.

**Recommendation:** continue the automated workflow with defined guardrail monitoring and moderate—not high—causal confidence. See the [finished stakeholder readout](02_pre_post_analysis/reports/stakeholder_readout.md), [expected analytical narrative](02_pre_post_analysis/templates/challenge_answer_key.md), and [guided analysis](02_pre_post_analysis/notebooks/guided_pre_post_analysis.ipynb).

## Modules and roadmap

| Module | Status | Focus | Start here |
|---|---|---|---|
| `01_ab_testing` | Complete | Controlled experiments and causal product or process decisions | [A/B Testing](01_ab_testing/README.md) |
| `02_pre_post_analysis` | Complete | Impact analysis when randomized control is unavailable | [Pre/Post Analysis](02_pre_post_analysis/README.md) |
| `03_target_analysis` | Complete | Eligibility, segmentation, opportunity sizing, prioritization, and activation handoff | [Target Analysis](03_target_analysis/README.md) |
| `04_predictive_analytics` | Complete | Predictive modeling from framing through validation and operationalization | [Predictive Analytics](04_predictive_analytics/README.md) |
| `05_ad_hoc_analysis` | Complete | Structured, time-bounded KPI diagnosis and decision handoff | [Ad Hoc Analysis](05_ad_hoc_analysis/README.md) |
| `06_customer_value_lifecycle` | Complete | RFM segmentation, lifecycle migration, value concentration, and controlled retention activation | [Customer Value & Lifecycle](06_customer_value_lifecycle/README.md) |
| `07_marketing_experimentation` | Complete | Split testing, factorial multivariate testing, interaction effects, multiplicity, and rollout governance | [Marketing Experimentation Suite](07_marketing_experimentation/README.md) |
| `08_macro_correlation_monitor` | Complete | Live gold–US10Y–DXY monitoring, rolling correlations, source governance, and regime-aware interpretation | [Macro Correlation Monitor](08_macro_correlation_monitor/README.md) |

Seven completed Analytics case studies now form the **Analytics** pillar. The completed PayWave predictive module is classified as a **Machine Learning seed case** and remains here so its links, tests, and reports continue to work; it can later be adapted as a transfer case in the dedicated [`machine-learning-standard-framework`](https://github.com/laura-rivera-sancho/machine-learning-standard-framework) repository.

The broader portfolio will use one repository per pillar. See the [portfolio roadmap](ROADMAP.md) for the five-repository architecture, agreed marketing and trading projects, shared evidence standards, and delivery sequence. Execution is tracked in the [Data & AI Portfolio Roadmap project](https://github.com/users/laura-rivera-sancho/projects/2).

## Repository map

```text
analytics-standard-framework/
├── 01_ab_testing/
│   ├── case_study/      # NovaPay business case, data dictionary, and reference results
│   ├── data/raw/        # Compact synthetic sample
│   ├── notebooks/       # Guided and challenge analyses
│   ├── reports/         # Finished Markdown readout, preview, and PowerPoint deck
│   ├── src/             # Data generator and reference analysis
│   └── templates/       # Experiment planning, validation, and stakeholder readout
├── 02_pre_post_analysis/
│   ├── case_study/      # FinFlow business case and data dictionary
│   ├── data/raw/        # Compact synthetic sample
│   ├── notebooks/       # Guided and challenge analyses
│   ├── reports/         # Finished Markdown readout, preview, and PowerPoint deck
│   ├── src/             # Data generator and Pre/Post/ITS analysis
│   └── templates/       # Authoring guide, answer key, rubric, and reusable template
├── 03_target_analysis/
│   ├── case_study/      # LuminaPay decision, dictionary, and expected results
│   ├── data/raw/        # Compact synthetic merchant sample
│   ├── notebooks/       # Guided and challenge targeting workflows
│   ├── reports/         # Finished Markdown readout, preview, and PowerPoint deck
│   ├── src/             # Synthetic data, eligibility, sizing, and prioritization
│   └── templates/       # Answer key, rubric, and activation readout
├── 04_predictive_analytics/
│   ├── case_study/      # PayWave business case and data dictionary
│   ├── data/raw/        # Compact synthetic sample
│   ├── notebooks/       # Guided and challenge modeling workflows
│   ├── reports/         # Finished Markdown readout, preview, and PowerPoint deck
│   ├── src/             # Synthetic data and temporal model evaluation
│   └── templates/       # Answer key, rubric, and stakeholder readout
├── 05_ad_hoc_analysis/
│   ├── case_study/      # OrbitMart diagnostic case, dictionary, and results
│   ├── data/raw/        # Compact synthetic checkout sample
│   ├── notebooks/       # Guided and challenge diagnostic workflows
│   ├── reports/         # Finished Markdown readout, preview, and PowerPoint deck
│   ├── src/             # Synthetic data, KPI tree, decomposition, and inference
│   └── templates/       # Intake brief, answer key, rubric, and readout
├── 06_customer_value_lifecycle/
│   ├── case_study/      # Harbor & Pine decision, dictionary, and reference results
│   ├── data/raw/        # Compact synthetic customer-order sample
│   ├── notebooks/       # Guided lifecycle analysis
│   ├── reports/         # Finished Markdown readout, preview, and PowerPoint deck
│   ├── src/             # Synthetic data, RFM, migration, prioritization, and visualization
│   └── templates/       # Reusable lifecycle stakeholder readout
├── 07_marketing_experimentation/
│   ├── case_study/      # Harbor & Pine charter, dictionary, and reference results
│   ├── data/raw/        # Compact synthetic split-test and factorial-assignment sample
│   ├── notebooks/       # Guided experimentation analysis
│   ├── reports/         # Finished Markdown readout, preview, and PowerPoint deck
│   ├── src/             # Generator, validation, analysis, and visualization
│   └── templates/       # Reusable experiment stakeholder readout
├── 08_macro_correlation_monitor/
│   ├── case_study/      # Exact market-data source contract and limitations
│   ├── reports/         # Research-oriented stakeholder readout
│   ├── site/            # Live Sites dashboard and market-data API route
│   └── src/             # Tested alignment, transformation, and risk utilities
├── ROADMAP.md            # Five-repository portfolio plan and milestone definitions
└── README.md             # Portfolio landing page
```

## Quick start

### Requirements

- Python 3.11 or 3.12
- `pip`
- Jupyter for the guided notebooks
- Node.js only for the optional reusable PowerPoint template generators

### Run an analysis

Clone the repository and choose a module:

```bash
git clone https://github.com/laura-rivera-sancho/analytics-standard-framework.git
cd analytics-standard-framework/01_ab_testing

python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

python src/generate_synthetic_data.py
python src/analyze_experiment.py
```

All completed modules use the same pinned root environment. From the repository root, install the full runtime with:

```bash
pip install -r requirements.txt
```

For tests and linting:

```bash
pip install -r requirements-dev.txt
ruff check .
pytest
```

Open the guided notebook:

```bash
jupyter notebook notebooks/guided_ab_test_analysis.ipynb
```

Equivalent instructions and module-specific assumptions are documented in each module README.

## Core analytics lifecycle

1. Frame the business problem and decision.
2. Define the analytical question and hypothesis.
3. Specify the population, scope, and unit of analysis.
4. Define data requirements and success metrics before reading outcomes.
5. Validate data quality and analytical integrity.
6. Select and execute the appropriate method.
7. Quantify uncertainty, effect size, and practical significance.
8. Investigate segments, assumptions, and alternative explanations.
9. Translate findings into business impact.
10. Recommend an action with limitations and a monitoring plan.
11. Document the work for reproducibility and handoff.

## Design principles

- Start with the business decision, not the statistical technique.
- Define hypotheses and success metrics before reading outcomes.
- Validate data and experiment or model integrity before interpretation.
- Separate statistical significance from business significance.
- Treat exploratory findings as hypotheses when appropriate.
- Make assumptions, exclusions, and limitations explicit.
- End every analysis with a clear recommendation and decision path.

## Data and privacy

All companies, scenarios, customer identifiers, datasets, and results in this repository are fictional or synthetically generated for education and portfolio demonstration. They do not represent confidential information from any employer or client.

## Contributing and reuse

Contributions that improve analytical rigor, reproducibility, documentation, or
accessibility are welcome. Review [CONTRIBUTING.md](CONTRIBUTING.md) for the
module standard, synthetic-data policy, local checks, and pull request workflow.

This project is available under the [MIT License](LICENSE). If you reference the
framework in academic or professional work, GitHub can generate a citation from
the repository's [citation metadata](CITATION.cff).
