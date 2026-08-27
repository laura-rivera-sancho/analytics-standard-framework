# Analytics Standard Framework

[![Repository quality](https://github.com/laura-rivera-sancho/analytics-standard-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/laura-rivera-sancho/analytics-standard-framework/actions/workflows/ci.yml)

**A portfolio-ready analytics operating model for turning business questions into reproducible analysis, defensible decisions, and stakeholder communication.**

This repository demonstrates how I approach common analytics engagements from end to end: framing the decision, defining metrics and assumptions, validating data, selecting an appropriate method, interpreting uncertainty, estimating business impact, and communicating a recommendation.

Each module combines a reusable methodology with a fictional business case, synthetic data, reproducible Python code, guided practice, and an executive communication standard. No employer, client, or confidential data are used.

## Recommended portfolio review path

If you are reviewing this repository for a role or project, these links provide
the fastest route to the strongest evidence:

| What to assess | Start here | What it demonstrates |
|---|---|---|
| Decision communication | [NovaPay A/B testing readout](01_ab_testing/reports/stakeholder_readout.md) | Experiment validity, effect size, guardrails, and a rollout recommendation |
| Causal judgment | [FinFlow Pre/Post readout](02_pre_post_analysis/reports/stakeholder_readout.md) | Interrupted time series, confounder review, limitations, and risk monitoring |
| Target-population design | [LuminaPay targeting readout](03_target_analysis/reports/stakeholder_readout.md) | Eligibility governance, opportunity sizing, transparent prioritization, and activation controls |
| Predictive decision design | [PayWave modeling readout](04_predictive_analytics/reports/stakeholder_readout.md) | Temporal validation, capacity metrics, business value, and a controlled-pilot plan |
| Reproducible implementation | [Source workflows](01_ab_testing/src) and [automated tests](tests) | Reusable Python, deterministic data, analytical tests, and repository checks |
| Project scope and next modules | [Roadmap](ROADMAP.md) | Completion criteria, current status, and planned work |

## What this project demonstrates

- **Business problem framing** — translating broad requests into decision-ready analytical questions.
- **Experimentation and causal reasoning** — distinguishing randomized evidence from observational comparisons.
- **Statistical analysis** — effect sizes, confidence intervals, hypothesis tests, guardrails, and practical significance.
- **Predictive modeling** — leakage-safe features, temporal validation, calibration, capacity-aware evaluation, and business value.
- **Target design** — auditable eligibility rules, denominator-consistent funnels, opportunity sizing, and capacity allocation.
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
| `05_ad_hoc_analysis` | Planned | Structured diagnostic and exploratory analysis | [Module plan](05_ad_hoc_analysis/README.md) |

See the [project roadmap and module completion standard](ROADMAP.md) for objective status definitions, planned deliverables, and repository-wide improvements.

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
│   └── README.md         # Planned scope and completion criteria
├── ROADMAP.md            # Status definitions and cross-module completion standard
└── README.md             # Portfolio landing page
```

## Quick start

### Requirements

- Python 3.11 or 3.12
- `pip`
- Jupyter for the guided and challenge notebooks
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
