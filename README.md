# Analytics Standard Framework

**A portfolio-ready analytics operating model for turning business questions into reproducible analysis, defensible decisions, and stakeholder communication.**

This repository demonstrates how I approach common analytics engagements from end to end: framing the decision, defining metrics and assumptions, validating data, selecting an appropriate method, interpreting uncertainty, estimating business impact, and communicating a recommendation.

Each module combines a reusable methodology with a fictional business case, synthetic data, reproducible Python code, guided practice, and an executive communication standard. No employer, client, or confidential data are used.

## What this project demonstrates

- **Business problem framing** — translating broad requests into decision-ready analytical questions.
- **Experimentation and causal reasoning** — distinguishing randomized evidence from observational comparisons.
- **Statistical analysis** — effect sizes, confidence intervals, hypothesis tests, guardrails, and practical significance.
- **Predictive modeling** — leakage-safe features, temporal validation, calibration, capacity-aware evaluation, and business value.
- **Data quality** — deliberate validation of duplicates, missingness, invalid values, inconsistent categories, and timing logic.
- **Reproducible analytics** — deterministic synthetic-data generators, reusable analysis functions, and documented assumptions.
- **Stakeholder communication** — concise recommendations that separate evidence, limitations, and next actions.

## Featured case studies

| Case study | Business decision | Analytical approach | Portfolio evidence |
|---|---|---|---|
| **NovaPay** | Should a simplified checkout experience be rolled out? | Randomized A/B test | Treatment increased checkout completion from **72.64% to 75.95%** (**+3.31 percentage points**, 95% CI **+2.45 to +4.17 pp**) while materially reducing checkout time. |
| **FinFlow** | Should an automated verification workflow continue scaling? | Pre/Post analysis and adjusted interrupted time series | Completion, manual-review demand, and verification time improve after launch. The recommendation remains appropriately cautious because the design is observational and includes trend, ramp, campaign, and traffic-mix effects. |
| **PayWave** | Which customers should receive capacity-constrained retention outreach? | Temporal binary-classification workflow | Gradient Boosting captures **3,853** future-inactive customers at 5,000-contact capacity—**552 more** than the recency rule—with **77.06% precision** and **2.58x lift** on the held-out Test cohort. |

### NovaPay decision snapshot

| KPI | Control | Treatment | Decision signal |
|---|---:|---:|---|
| Checkout completion | 72.64% | 75.95% | +3.31 pp; statistically credible and above the assumed business threshold |
| Mean checkout time | ~89.35 sec | ~64.16 sec | Material reduction in customer friction |
| Support contact rate | 5.655% | 4.570% | Favorable guardrail movement |
| Payment decline rate | 5.495% | 5.180% | Small reduction; not statistically conclusive |
| Fraud rate | 0.355% | 0.350% | No meaningful difference detected |

**Recommendation:** proceed toward rollout with continued monitoring of fraud, payment declines, and segment stability. See the [full reference results](01_ab_testing/case_study/expected_results.md) and [guided analysis](01_ab_testing/notebooks/guided_ab_test_analysis.ipynb).

### FinFlow decision snapshot

The simple Pre/Post comparison is intentionally not treated as proof of causality. The workflow re-derives launch timing, separates the seven-day stabilization ramp, examines traffic-mix changes, and estimates an adjusted interrupted time-series model with baseline trend, weekday, campaign, ramp, and customer-mix controls.

**Recommendation:** continue the automated workflow with defined guardrail monitoring and moderate—not high—causal confidence. See the [expected analytical narrative](02_pre_post_analysis/templates/challenge_answer_key.md) and [guided analysis](02_pre_post_analysis/notebooks/guided_pre_post_analysis.ipynb).

## Modules and roadmap

| Module | Status | Focus | Start here |
|---|---|---|---|
| `01_ab_testing` | Core module complete | Controlled experiments and causal product or process decisions | [A/B Testing](01_ab_testing/README.md) |
| `02_pre_post_analysis` | Complete | Impact analysis when randomized control is unavailable | [Pre/Post Analysis](02_pre_post_analysis/README.md) |
| `03_target_analysis` | Planned | Segmentation, opportunity sizing, and target-population definition | Roadmap item |
| `04_predictive_analytics` | Complete | Predictive modeling from framing through validation and operationalization | [Predictive Analytics](04_predictive_analytics/README.md) |
| `05_ad_hoc_analysis` | Planned | Structured diagnostic and exploratory analysis | Roadmap item |

`Core module complete` means the principal A/B methodology, case study, code, guided notebook, challenge notebook, reference results, and communication templates are present. Repository-wide automation and presentation improvements remain on the project roadmap.

## Repository map

```text
analytics-standard-framework/
├── 01_ab_testing/
│   ├── case_study/      # NovaPay business case, data dictionary, and reference results
│   ├── data/raw/        # Compact synthetic sample
│   ├── notebooks/       # Guided and challenge analyses
│   ├── src/             # Data generator and reference analysis
│   └── templates/       # Experiment planning, validation, and stakeholder readout
├── 02_pre_post_analysis/
│   ├── case_study/      # FinFlow business case and data dictionary
│   ├── notebooks/       # Guided and challenge analyses
│   ├── src/             # Data generator and Pre/Post/ITS analysis
│   └── templates/       # Readout, answer key, rubric, and PowerPoint generator
├── 04_predictive_analytics/
│   ├── case_study/      # PayWave business case and data dictionary
│   ├── data/raw/        # Compact synthetic sample
│   ├── notebooks/       # Guided and challenge modeling workflows
│   ├── src/             # Synthetic data and temporal model evaluation
│   └── templates/       # Answer key, rubric, and stakeholder readout
└── README.md
```

## Quick start

### Requirements

- Python 3.11 or newer
- `pip`
- Jupyter for the guided and challenge notebooks
- Node.js only when generating the PowerPoint readout templates

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

## Project status

This repository is under active development. The next planned modules are Target Analysis and Ad Hoc Analysis. Automated tests, continuous integration, dependency locking, licensing, and richer visual result previews are part of the repository-improvement roadmap.
