"""Pure analytical utilities for the A8 macro correlation monitor."""

from __future__ import annotations

import numpy as np
import pandas as pd

REQUIRED_SERIES = ("gold", "dxy", "us10y")


def align_market_series(series: dict[str, pd.Series]) -> pd.DataFrame:
    """Inner-join validated, numeric market series on a unique date index."""
    missing = set(REQUIRED_SERIES) - set(series)
    if missing:
        raise ValueError(f"Missing required series: {sorted(missing)}")
    cleaned: dict[str, pd.Series] = {}
    for name in REQUIRED_SERIES:
        values = pd.to_numeric(series[name], errors="coerce")
        values.index = pd.to_datetime(values.index)
        values = values[~values.index.duplicated(keep="last")].sort_index().dropna()
        if (values <= 0).any():
            raise ValueError(f"{name} contains a non-positive value")
        cleaned[name] = values
    aligned = pd.concat(cleaned, axis=1, join="inner").dropna()
    if len(aligned) < 3:
        raise ValueError("At least three common observations are required")
    return aligned


def transform_daily_changes(levels: pd.DataFrame) -> pd.DataFrame:
    """Return log returns for price/index series and point changes for the yield."""
    changes = pd.DataFrame(index=levels.index)
    changes["gold"] = np.log(levels["gold"]).diff()
    changes["dxy"] = np.log(levels["dxy"]).diff()
    changes["us10y"] = levels["us10y"].diff()
    return changes.dropna()


def rolling_correlations(changes: pd.DataFrame, window: int) -> pd.DataFrame:
    """Calculate prespecified rolling gold correlations."""
    if window < 3:
        raise ValueError("Window must contain at least three observations")
    return pd.DataFrame(
        {
            "gold_dxy": changes["gold"].rolling(window).corr(changes["dxy"]),
            "gold_us10y": changes["gold"].rolling(window).corr(changes["us10y"]),
        }
    )


def annualized_volatility(changes: pd.DataFrame, periods: int = 252) -> pd.Series:
    """Annualize sample volatility for the transformed daily series."""
    return changes.std(ddof=1) * np.sqrt(periods)


def drawdown(levels: pd.Series) -> pd.Series:
    """Return the path of percentage drawdowns from each running peak."""
    return levels / levels.cummax() - 1
