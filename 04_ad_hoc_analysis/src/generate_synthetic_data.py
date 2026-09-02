from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 505
DATES = pd.date_range("2026-07-06", "2026-08-16", freq="D")
CURRENT_START = pd.Timestamp("2026-08-10")
PILOT_START = pd.Timestamp("2026-08-03")


def _version_shares(date, country, platform):
    if platform == "Web":
        return [("web", 1.0)]
    if platform == "iOS":
        return [("ios-12.1", 1.0)]
    if country in {"MX", "BR"} and date >= CURRENT_START:
        return [("android-8.3", 0.18), ("android-8.4", 0.82)]
    if country in {"MX", "BR"} and date >= PILOT_START:
        return [("android-8.3", 0.85), ("android-8.4", 0.15)]
    return [("android-8.3", 1.0)]


def generate_clean_data(seed=SEED):
    """Generate synthetic daily checkout-funnel aggregates for diagnostic analysis."""
    rng = np.random.default_rng(seed)
    rows = []
    countries = ["US", "MX", "BR", "CR"]
    platforms = ["Web", "iOS", "Android"]
    payment_methods = ["Card", "Digital wallet", "Bank transfer"]
    channels = ["Organic", "Paid search", "Paid social"]

    country_scale = {"US": 1.65, "MX": 1.05, "BR": 0.95, "CR": 0.42}
    platform_scale = {"Web": 1.15, "iOS": 0.82, "Android": 1.10}
    payment_scale = {"Card": 1.35, "Digital wallet": 0.90, "Bank transfer": 0.48}
    channel_scale = {"Organic": 1.10, "Paid search": 0.78, "Paid social": 0.63}

    for date, country, platform, payment_method, channel in product(
        DATES, countries, platforms, payment_methods, channels
    ):
        weekday_scale = 1.10 if date.dayofweek in {4, 5} else 0.96
        for app_version, version_share in _version_shares(date, country, platform):
            mean_starts = (
                43
                * country_scale[country]
                * platform_scale[platform]
                * payment_scale[payment_method]
                * channel_scale[channel]
                * weekday_scale
                * version_share
            )
            starts = max(8, rng.poisson(mean_starts))

            attempt_rate = 0.965 - 0.012 * (channel == "Paid social")
            approval_rate = {
                "Card": 0.914,
                "Digital wallet": 0.944,
                "Bank transfer": 0.892,
            }[payment_method]
            approval_rate -= 0.012 * (country == "BR") + 0.006 * (country == "MX")
            completion_after_approval = 0.987

            # Current-week issue: Android 8.4 digital-wallet approvals deteriorate in MX and BR.
            incident_slice = (
                date >= CURRENT_START
                and country in {"MX", "BR"}
                and app_version == "android-8.4"
                and payment_method == "Digital wallet"
            )
            if incident_slice:
                approval_rate -= 0.235

            attempts = rng.binomial(starts, np.clip(attempt_rate, 0, 1))
            approvals = rng.binomial(attempts, np.clip(approval_rate, 0, 1))
            orders = rng.binomial(approvals, completion_after_approval)

            aov = {
                "US": 82,
                "MX": 49,
                "BR": 44,
                "CR": 53,
            }[country] * {"Organic": 1.04, "Paid search": 1.00, "Paid social": 0.91}[channel]
            revenue = orders * max(8, rng.normal(aov, aov * 0.05))
            support = rng.poisson(0.008 * starts + (0.055 * starts if incident_slice else 0))

            rows.append(
                {
                    "date": date.strftime("%Y-%m-%d"),
                    "country": country,
                    "platform": platform,
                    "app_version": app_version,
                    "payment_method": payment_method,
                    "acquisition_channel": channel,
                    "checkout_starts": starts,
                    "payment_attempts": attempts,
                    "payment_approvals": approvals,
                    "orders_completed": orders,
                    "revenue_usd": round(revenue, 2),
                    "checkout_support_contacts": support,
                }
            )

    return pd.DataFrame(rows)


def generate_raw_data(seed=SEED):
    """Add deliberate defects to make validation part of the diagnostic workflow."""
    rng = np.random.default_rng(seed + 1)
    raw = generate_clean_data(seed)

    missing_idx = rng.choice(raw.index, 25, replace=False)
    raw.loc[missing_idx, "acquisition_channel"] = np.nan

    casing_idx = rng.choice(raw.index, 12, replace=False)
    raw.loc[casing_idx, "country"] = raw.loc[casing_idx, "country"].str.lower()

    defect_idx = rng.choice(raw.index, 12, replace=False)
    raw.loc[defect_idx[:6], "checkout_starts"] = -1
    raw.loc[defect_idx[6:], "orders_completed"] = raw.loc[defect_idx[6:], "payment_approvals"] + 3

    duplicates = raw.sample(18, random_state=seed)
    return pd.concat([raw, duplicates], ignore_index=True)


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_path = module_root / "data" / "raw" / "orbitmart_checkout_diagnostic_full.csv"
    sample_path = module_root / "data" / "raw" / "orbitmart_checkout_diagnostic_sample.csv"
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    raw = generate_raw_data()
    raw.to_csv(raw_path, index=False)
    raw.sample(2_500, random_state=SEED).to_csv(sample_path, index=False)
    print(f"Wrote {len(raw):,} rows to {raw_path}")
    print(f"Wrote 2,500 inspectable rows to {sample_path}")


if __name__ == "__main__":
    main()
