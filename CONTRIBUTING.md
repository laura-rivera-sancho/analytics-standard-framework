# Contributing

Thank you for helping improve the Analytics Standard Framework. Contributions
should strengthen its value as a reusable, decision-focused analytics resource.

## Ways to contribute

- correct unclear guidance, broken links, or reproducibility issues
- improve tests, documentation, accessibility, or developer experience
- propose a new case study, analytical method, or reusable template
- complete or extend a planned module using the repository standard

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

## Module standard

A module described as complete should include:

1. a module README with audience, decisions supported, navigation, and run steps
2. fundamentals and methodology documentation
3. a fictional business case and data dictionary
4. deterministic synthetic-data generation with a small reviewable sample
5. reusable analysis code with explicit validation and assumptions
6. a guided notebook and an independent challenge notebook
7. deterministic expected results or an answer key
8. a stakeholder communication template
9. limitations, privacy disclosure, and a monitoring or follow-up plan
10. passing repository-quality checks

See the [roadmap](ROADMAP.md) for the canonical completion standard and planned
module scope.

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
python -m compileall 01_ab_testing 02_pre_post_analysis 04_predictive_analytics
pytest --cov
```

Also run any changed analysis workflow end to end and confirm that documented
results still match its expected-results file or answer key.

## Pull requests

Use the pull request template and explain the decision or learner need addressed,
the analytical impact, and the validation performed. Include screenshots or
generated artifacts when a visible output changes. Small, focused pull requests
are easier to review and maintain.

By contributing, you agree that your contribution will be licensed under the
repository's [MIT License](LICENSE).
