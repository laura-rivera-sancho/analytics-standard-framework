import importlib.util
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

MODULE = Path(__file__).parents[1] / "08_macro_correlation_monitor" / "src" / "market_analysis.py"
SPEC = importlib.util.spec_from_file_location("market_analysis", MODULE)
market = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(market)


def sample_levels() -> pd.DataFrame:
    index = pd.date_range("2025-01-01", periods=8, freq="D")
    return pd.DataFrame(
        {
            "gold": [100, 102, 101, 104, 106, 105, 108, 110],
            "dxy": [100, 99, 100, 98, 97, 98, 96, 95],
            "us10y": [4.0, 4.1, 4.05, 4.2, 4.1, 4.0, 3.9, 3.8],
        },
        index=index,
    )


def test_align_market_series_inner_joins_and_deduplicates():
    levels = sample_levels()
    dxy = levels["dxy"].drop(levels.index[2])
    aligned = market.align_market_series(
        {"gold": levels["gold"], "dxy": dxy, "us10y": levels["us10y"]}
    )
    assert list(aligned.columns) == ["gold", "dxy", "us10y"]
    assert levels.index[2] not in aligned.index
    assert aligned.index.is_monotonic_increasing


def test_transform_uses_log_returns_and_yield_point_changes():
    levels = sample_levels()
    changes = market.transform_daily_changes(levels)
    assert changes.iloc[0]["gold"] == pytest.approx(np.log(102 / 100))
    assert changes.iloc[0]["dxy"] == pytest.approx(np.log(99 / 100))
    assert changes.iloc[0]["us10y"] == pytest.approx(0.1)


def test_rolling_correlations_match_direct_calculation():
    changes = market.transform_daily_changes(sample_levels())
    result = market.rolling_correlations(changes, window=4).dropna()
    expected = changes["gold"].iloc[-4:].corr(changes["dxy"].iloc[-4:])
    assert result.iloc[-1]["gold_dxy"] == pytest.approx(expected)


def test_drawdown_is_zero_at_peaks_and_negative_below_peak():
    result = market.drawdown(pd.Series([100.0, 110.0, 99.0, 121.0]))
    assert result.tolist() == pytest.approx([0.0, 0.0, -0.1, 0.0])


def test_invalid_series_contract_fails_loudly():
    levels = sample_levels()
    with pytest.raises(ValueError, match="Missing required series"):
        market.align_market_series({"gold": levels["gold"], "dxy": levels["dxy"]})
    bad_gold = levels["gold"].copy()
    bad_gold.iloc[2] = 0
    with pytest.raises(ValueError, match="non-positive"):
        market.align_market_series(
            {"gold": bad_gold, "dxy": levels["dxy"], "us10y": levels["us10y"]}
        )


def test_fundamentals_and_intelligence_contract_preserve_analysis_scope():
    module_root = MODULE.parents[1]
    fundamentals = (module_root / "macro_correlation_fundamentals.md").read_text(encoding="utf-8")
    contract = (module_root / "case_study" / "intelligence_layer_contract.md").read_text(
        encoding="utf-8"
    )
    assert "interview" not in fundamentals.lower()
    assert "correlation" in fundamentals.lower()
    assert "cited llm research" in contract.lower()
    assert "mandatory human approval" in contract.lower()
