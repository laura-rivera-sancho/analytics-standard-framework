# Contributing

Thank you for helping improve the Decision Analytics Case Studies. Contributions
should strengthen their value as reusable, decision-focused analytical evidence.

## Ways to contribute

- correct unclear guidance, broken links, or reproducibility issues
- improve tests, documentation, accessibility, or developer experience
- propose a new case study, analytical method, or reusable template
- complete or extend a decision case using the repository evidence standard

For substantial changes, open a module proposal before implementation so the
business decision, method, and intended deliverables can be discussed first.

## Local setup

Use Python 3.11 or 3.12 from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Create a focused branch, keep commits small and descriptive, and avoid mixing
unrelated changes in the same pull request.

## Case-study evidence standard

A published case study should include:

1. a module README with audience, decisions supported, navigation, and run steps
2. method notes and methodology documentation
3. a fictional business case and data dictionary
4. deterministic synthetic-data generation with a small reviewable sample
5. reusable analysis code with explicit validation and assumptions
6. a reproducible notebook only when it materially improves the review experience; place optional exercises in a secondary reference area
7. deterministic expected results or reference findings
8. a stakeholder communication template
9. limitations, privacy disclosure, and a monitoring or follow-up plan
10. passing repository-quality checks

See the [roadmap](ROADMAP.md) for the shared evidence standard and cross-portfolio
readiness map.

## Data and privacy

Only fictional or synthetically generated data belongs in this repository. Do
not submit personal data, confidential business information, credentials, API
keys, or employer/client artifacts. Generated datasets should be deterministic,
documented, and small enough for review; large outputs should remain untracked.

## Quality checks

Run these checks before opening a pull request:

```bash
ruff check .
ruff format --check .
python -m compileall -q 01_ab_testing/src 02_pre_post_analysis/src 03_target_analysis/src 04_ad_hoc_analysis/src 05_customer_value_lifecycle/src 06_marketing_experimentation/src 07_macro_correlation_monitor/src tests
pytest --cov
```

Also run any changed analysis workflow end to end and confirm that documented
results still match its expected-results file or reference findings.

## Accessibility and inclusive communication

- Use one level-one heading per standalone Markdown document and do not skip heading levels.
- Give links descriptive labels that make sense outside the surrounding sentence.
- Describe the evidence or purpose of every image in its alternative text.
- Use real table headers and never rely on color alone to communicate status or meaning.
- Keep charts labeled directly and state important findings in text as well as visually.
- Prefer plain language, expand uncommon abbreviations, and explain analytical limitations explicitly.

## Pull requests

Use the pull request template and explain the decision or reviewer need addressed,
the analytical impact, and the validation performed. Include screenshots or
generated artifacts when a visible output changes. Small, focused pull requests
are easier to review and maintain.

By contributing, you agree that your contribution will be licensed under the
repository's [MIT License](LICENSE).
