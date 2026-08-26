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
def predictive_generator():
    return load_source_module(
        "predictive_generator", "04_predictive_analytics/src/generate_synthetic_data.py"
    )


@pytest.fixture(scope="session")
def predictive_analysis():
    return load_source_module(
        "predictive_analysis", "04_predictive_analytics/src/train_evaluate_models.py"
    )
