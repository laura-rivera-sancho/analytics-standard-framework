from pathlib import Path

import numpy as np
import pandas as pd

SEED = 314
N_MERCHANTS = 60_000
AS_OF_DATE = "2026-08-01"


def generate_clean_data(seed=SEED, n_merchants=N_MERCHANTS):
    """Generate a synthetic merchant population for an Instant Settlement campaign."""
    rng = np.random.default_rng(seed)
    latent_scale = rng.normal(0, 1, n_merchants)
    latent_friction = rng.normal(0, 1, n_merchants)

    country = rng.choice(["US", "MX", "BR", "CR"], n_merchants, p=[0.42, 0.25, 0.23, 0.10])
    industry = rng.choice(
        ["Retail", "Food & beverage", "Professional services", "Digital goods", "Travel"],
        n_merchants,
        p=[0.30, 0.24, 0.22, 0.16, 0.08],
    )
    tenure = np.clip((rng.gamma(2.4, 11.5, n_merchants) + 1).round(), 1, 84).astype(int)
    account_status = rng.choice(["Active", "Paused", "Closed"], n_merchants, p=[0.91, 0.06, 0.03])
    kyc_status = rng.choice(["Verified", "Pending", "Expired"], n_merchants, p=[0.90, 0.07, 0.03])
    risk_tier = rng.choice(["Low", "Medium", "High"], n_merchants, p=[0.62, 0.28, 0.10])
    profitability_tier = rng.choice(["Low", "Medium", "High"], n_merchants, p=[0.33, 0.45, 0.22])

    volume = np.clip(
        np.exp(9.45 + 0.75 * latent_scale + rng.normal(0, 0.45, n_merchants)), 500, 350_000
    )
    transaction_count = np.maximum(
        1, (volume / rng.lognormal(4.25, 0.35, n_merchants)).round()
    ).astype(int)
    delay = np.clip(
        26 + 10 * latent_friction + 5 * (country == "BR") + rng.normal(0, 7, n_merchants), 4, 96
    )
    failure_rate = np.clip(
        0.011 + 0.008 * latent_friction + rng.normal(0, 0.007, n_merchants), 0, 0.09
    )
    support_contacts = rng.poisson(np.clip(0.55 + 0.48 * np.maximum(latent_friction, 0), 0.1, 4.5))
    mobile_active = rng.binomial(1, np.clip(0.69 + 0.08 * latent_scale, 0.35, 0.92))
    enabled_prob = np.clip(0.20 + 0.06 * latent_scale + 0.04 * (tenure > 18), 0.05, 0.52)
    enabled = rng.binomial(1, enabled_prob)
    contacted = rng.binomial(1, np.clip(0.09 + 0.05 * (profitability_tier == "High"), 0, 0.30))

    return pd.DataFrame(
        {
            "merchant_id": [f"LS{value:06d}" for value in range(1, n_merchants + 1)],
            "as_of_date": AS_OF_DATE,
            "country": country,
            "industry": industry,
            "tenure_months": tenure,
            "account_status": account_status,
            "kyc_status": kyc_status,
            "risk_tier": risk_tier,
            "profitability_tier": profitability_tier,
            "monthly_payment_volume_usd": np.round(volume, 2),
            "transaction_count_30d": transaction_count,
            "avg_settlement_delay_hours": np.round(delay, 1),
            "payout_failure_rate_90d": np.round(failure_rate, 4),
            "support_contacts_90d": support_contacts,
            "mobile_app_active": mobile_active,
            "instant_settlement_enabled": enabled,
            "contacted_last_30d": contacted,
        }
    )


def generate_raw_data(seed=SEED, n_merchants=N_MERCHANTS):
    """Add small, deliberate quality defects for validation practice."""
    rng = np.random.default_rng(seed + 1)
    raw = generate_clean_data(seed, n_merchants)

    missing_count = max(1, int(n_merchants * 0.004))
    missing_idx = rng.choice(raw.index, missing_count, replace=False)
    raw.loc[missing_idx, "industry"] = np.nan

    defect_count = max(3, int(n_merchants * 0.001))
    defect_idx = rng.choice(raw.index, defect_count, replace=False)
    thirds = np.array_split(defect_idx, 3)
    raw.loc[thirds[0], "country"] = raw.loc[thirds[0], "country"].str.lower()
    raw.loc[thirds[1], "monthly_payment_volume_usd"] = -100
    raw.loc[thirds[2], "tenure_months"] = -1

    duplicate_count = max(1, int(n_merchants * 0.0005))
    duplicates = raw.sample(duplicate_count, random_state=seed)
    return pd.concat([raw, duplicates], ignore_index=True)


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_path = module_root / "data" / "raw" / "lumina_settlement_target_full.csv"
    sample_path = module_root / "data" / "raw" / "lumina_settlement_target_sample.csv"
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    raw = generate_raw_data()
    raw.to_csv(raw_path, index=False)
    raw.sample(2_500, random_state=SEED).to_csv(sample_path, index=False)
    print(f"Wrote {len(raw):,} rows to {raw_path}")
    print(f"Wrote 2,500 inspectable rows to {sample_path}")


if __name__ == "__main__":
    main()
