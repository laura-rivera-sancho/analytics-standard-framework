from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load_source_module(name: str, relative_path: str):
    """Load a source file whose numbered parent directory is not a Python package."""
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="session")
def ab_generator():
    return load_source_module("ab_generator", "01_ab_testing/src/generate_synthetic_data.py")


@pytest.fixture(scope="session")
def ab_analysis():
    return load_source_module("ab_analysis", "01_ab_testing/src/analyze_experiment.py")


@pytest.fixture(scope="session")
def prepost_generator():
    return load_source_module(
        "prepost_generator", "02_pre_post_analysis/src/generate_synthetic_data.py"
    )


@pytest.fixture(scope="session")
def prepost_analysis():
    return load_source_module("prepost_analysis", "02_pre_post_analysis/src/analyze_pre_post.py")


@pytest.fixture(scope="session")
def target_generator():
    return load_source_module(
        "target_generator", "03_target_analysis/src/generate_synthetic_data.py"
    )


@pytest.fixture(scope="session")
def target_analysis():
    return load_source_module("target_analysis", "03_target_analysis/src/analyze_targets.py")


@pytest.fixture(scope="session")
def adhoc_generator():
    return load_source_module(
        "adhoc_generator", "05_ad_hoc_analysis/src/generate_synthetic_data.py"
    )


@pytest.fixture(scope="session")
def adhoc_analysis():
    return load_source_module("adhoc_analysis", "05_ad_hoc_analysis/src/diagnose_kpi_change.py")


@pytest.fixture(scope="session")
def lifecycle_generator():
    return load_source_module(
        "lifecycle_generator", "06_customer_value_lifecycle/src/generate_synthetic_data.py"
    )


@pytest.fixture(scope="session")
def lifecycle_analysis():
    return load_source_module(
        "lifecycle_analysis", "06_customer_value_lifecycle/src/analyze_customer_value.py"
    )


@pytest.fixture(scope="session")
def experimentation_generator():
    return load_source_module(
        "generate_synthetic_data",
        "07_marketing_experimentation/src/generate_synthetic_data.py",
    )


@pytest.fixture(scope="session")
def experimentation_validation(experimentation_generator):
    return load_source_module(
        "validate_experiment_data",
        "07_marketing_experimentation/src/validate_experiment_data.py",
    )


@pytest.fixture(scope="session")
def experimentation_analysis(experimentation_validation):
    return load_source_module(
        "experimentation_analysis",
        "07_marketing_experimentation/src/analyze_marketing_experiments.py",
    )
