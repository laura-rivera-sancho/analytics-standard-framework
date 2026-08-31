from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def test_relative_markdown_links_resolve():
    broken = []
    pattern = re.compile(r"\[[^]]*\]\(([^)]+)\)")

    for path in ROOT.rglob("*.md"):
        if ".venv" in path.parts:
            continue
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            relative = target.split("#", 1)[0]
            if relative and not urlparse(relative).scheme and not (path.parent / relative).exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")

    assert not broken, "Broken Markdown links:\n" + "\n".join(broken)


def test_notebooks_are_valid_json_and_code_cells_compile():
    errors = []
    notebooks = list(ROOT.rglob("*.ipynb"))
    assert notebooks

    for path in notebooks:
        if ".venv" in path.parts:
            continue
        notebook = json.loads(path.read_text(encoding="utf-8"))
        if notebook.get("nbformat") != 4:
            errors.append(f"{path.relative_to(ROOT)}: expected nbformat 4")
        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            try:
                compile("".join(cell.get("source", [])), f"{path}:cell{index}", "exec")
            except SyntaxError as exc:
                errors.append(str(exc))

    assert not errors, "Notebook errors:\n" + "\n".join(errors)


def test_completed_modules_exist():
    completed = [
        "01_ab_testing",
        "02_pre_post_analysis",
        "03_target_analysis",
        "04_predictive_analytics",
        "05_ad_hoc_analysis",
        "06_customer_value_lifecycle",
    ]
    for module in completed:
        root = ROOT / module
        assert (root / "README.md").exists()
        assert (root / "methodology.md").exists()
        assert (root / "case_study/business_case.md").exists()
        assert (root / "case_study/data_dictionary.md").exists()
        assert list(root.glob("*fundamentals*.md"))
        assert list((root / "notebooks").glob("guided*.ipynb"))
        if module != "06_customer_value_lifecycle":
            assert list((root / "notebooks").glob("challenge*.ipynb"))
        assert list((root / "src").glob("*.py"))
        assert list((root / "templates").glob("*readout*.md"))


def test_repository_does_not_track_large_generated_datasets():
    tracked = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.splitlines()
    oversized = []
    for relative in tracked:
        path = ROOT / relative
        if path.is_file() and path.stat().st_size > 2_000_000:
            oversized.append(relative)
    assert not oversized, f"Unexpected tracked files over 2 MB: {oversized}"


def test_module_requirements_delegate_to_root_environment():
    for module in [
        "01_ab_testing",
        "02_pre_post_analysis",
        "03_target_analysis",
        "04_predictive_analytics",
        "05_ad_hoc_analysis",
        "06_customer_value_lifecycle",
        "06_customer_value_lifecycle",
    ]:
        requirement = (ROOT / module / "requirements.txt").read_text(encoding="utf-8")
        assert "-r ../requirements.txt" in requirement


def test_community_health_files_exist_and_are_linked():
    expected = [
        "LICENSE",
        "CONTRIBUTING.md",
        "CITATION.cff",
        ".github/pull_request_template.md",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/ISSUE_TEMPLATE/module_proposal.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
    ]
    assert all((ROOT / relative).exists() for relative in expected)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "[CONTRIBUTING.md](CONTRIBUTING.md)" in readme
    assert "[MIT License](LICENSE)" in readme
    assert "[citation metadata](CITATION.cff)" in readme


def test_citation_metadata_identifies_repository_and_license():
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert "cff-version: 1.2.0" in citation
    assert 'title: "Analytics Standard Framework"' in citation
    assert "license: MIT" in citation
    assert "laura-rivera-sancho/analytics-standard-framework" in citation


def test_completed_modules_publish_stakeholder_artifacts():
    for module in [
        "01_ab_testing",
        "02_pre_post_analysis",
        "03_target_analysis",
        "04_predictive_analytics",
        "05_ad_hoc_analysis",
        "06_customer_value_lifecycle",
    ]:
        report_root = ROOT / module / "reports"
        markdown = report_root / "stakeholder_readout.md"
        preview = report_root / "executive_summary.png"
        deck = report_root / "stakeholder_readout.pptx"

        text = markdown.read_text(encoding="utf-8")
        assert "synthetically generated" in text
        assert "![" in text and "executive_summary.png" in text
        assert "[Download the five-slide PowerPoint readout](stakeholder_readout.pptx)" in text
        assert preview.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
        assert deck.read_bytes().startswith(b"PK")


def test_markdown_accessibility_basics():
    image_pattern = re.compile(r"!\[([^]]*)\]\([^)]+\)")
    link_pattern = re.compile(r"(?<!!)\[([^]]+)\]\([^)]+\)")
    generic_labels = {"click here", "here", "link", "read more", "learn more"}
    errors = []

    for path in ROOT.rglob("*.md"):
        if ".venv" in path.parts or ".github" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        headings = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            match = re.match(r"^(#{1,6})\s+", line)
            if match:
                headings.append((line_number, len(match.group(1))))

        if sum(level == 1 for _, level in headings) != 1:
            errors.append(f"{path.relative_to(ROOT)}: expected exactly one level-one heading")
        for previous, current in zip(headings, headings[1:]):
            if current[1] > previous[1] + 1:
                errors.append(
                    f"{path.relative_to(ROOT)}:{current[0]}: heading level jumps "
                    f"from {previous[1]} to {current[1]}"
                )

        for alt_text in image_pattern.findall(text):
            if len(alt_text.strip()) < 12:
                errors.append(f"{path.relative_to(ROOT)}: image needs descriptive alt text")
        for label in link_pattern.findall(text):
            if label.strip().lower() in generic_labels:
                errors.append(f"{path.relative_to(ROOT)}: generic link label '{label}'")

    assert not errors, "Markdown accessibility errors:\n" + "\n".join(errors)


def test_recruiter_shortcuts_link_to_finished_reports():
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "## Recommended portfolio review path" in root_readme

    for module in [
        "01_ab_testing",
        "02_pre_post_analysis",
        "03_target_analysis",
        "04_predictive_analytics",
        "05_ad_hoc_analysis",
    ]:
        module_readme = (ROOT / module / "README.md").read_text(encoding="utf-8")
        assert "**Portfolio shortcut:**" in module_readme
        assert "[Finished stakeholder readout](reports/stakeholder_readout.md)" in module_readme


def test_a6_completed_module_uses_guided_notebook_standard():
    module = ROOT / "06_customer_value_lifecycle"
    assert (module / "README.md").exists()
    assert (module / "customer_value_lifecycle_fundamentals.md").exists()
    assert (module / "methodology.md").exists()
    assert (module / "case_study/expected_results.md").exists()
    assert list((module / "notebooks").glob("guided*.ipynb"))
    assert not list((module / "notebooks").glob("challenge*.ipynb"))
    assert (module / "reports/executive_summary.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    assert (module / "reports/stakeholder_readout.pptx").read_bytes().startswith(b"PK")


def test_a7_foundation_is_decision_ready():
    module = ROOT / "07_marketing_experimentation"
    assert (module / "README.md").exists()
    assert (module / "marketing_experimentation_fundamentals.md").exists()
    assert (module / "case_study/business_case.md").exists()
    assert not list((module / "notebooks").glob("challenge*.ipynb"))

    business_case = (module / "case_study/business_case.md").read_text(encoding="utf-8")
    assert "Experiment 1 — Lifecycle-message split test" in business_case
    assert "Experiment 2 — Full-factorial multivariate test" in business_case
    assert "one guided notebook and no challenge notebook" in business_case
