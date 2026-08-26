"""Generate the synthetic NovaPay checkout A/B test dataset.

NovaPay is fictional. The generator is deterministic so the case can be
reproduced by any analyst.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
N_CUSTOMERS = 40_000


def generate_clean_data(n: int = N_CUSTOMERS, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    group = np.array(["Control"] * (n // 2) + ["Treatment"] * (n - n // 2))
    rng.shuffle(group)

    country = rng.choice(["US", "MX", "CR", "BR"], size=n, p=[0.50, 0.20, 0.10, 0.20])
    device = rng.choice(["Mobile", "Desktop"], size=n, p=[0.68, 0.32])
    tenure = rng.choice(["New", "Existing"], size=n, p=[0.45, 0.55])

    # Primary outcome. Treatment is designed to have a positive overall effect,
    # with a stronger effect for Mobile customers.
    completion_p = np.full(n, 0.718)
    completion_p += (device == "Mobile") * 0.010
    completion_p += (tenure == "Existing") * 0.008
    completion_p += ((group == "Treatment") & (device == "Mobile")) * 0.043
    completion_p += ((group == "Treatment") & (device == "Desktop")) * 0.012
    completion_p += (country == "BR") * -0.012
    completion_p += (country == "US") * 0.005
    completion_p = np.clip(completion_p, 0.05, 0.95)
    checkout_completed = rng.binomial(1, completion_p)

    # Checkout time is intentionally right-skewed.
    target_mean = np.where(group == "Treatment", 67.0, 92.0)
    target_mean -= np.where(device == "Mobile", 4.0, 0.0)
    sigma = 0.35
    mu = np.log(target_mean) - 0.5 * sigma**2
    checkout_time = np.maximum(10, rng.lognormal(mu, sigma, size=n)).round(1)

    # Transaction values are intentionally strongly right-skewed.
    transaction_value = np.clip(rng.lognormal(mean=np.log(70), sigma=0.90, size=n), 5, 2000).round(
        2
    )

    decline_p = 0.054 - (group == "Treatment") * 0.001 + (country == "BR") * 0.008
    payment_declined = rng.binomial(1, np.clip(decline_p, 0.005, 0.30))

    support_p = 0.048 - (group == "Treatment") * 0.009 + (checkout_completed == 0) * 0.030
    support_contact = rng.binomial(1, np.clip(support_p, 0.005, 0.35))

    fraud_p = (
        0.0031
        + (group == "Treatment") * 0.0005
        + (transaction_value > 300) * 0.0025
        + (country == "BR") * 0.0008
    )
    fraud_flag = rng.binomial(1, np.clip(fraud_p, 0.0, 0.05))

    dates = pd.to_datetime("2026-06-01") + pd.to_timedelta(rng.integers(0, 14, size=n), unit="D")

    return pd.DataFrame(
        {
            "customer_id": [f"C{i:07d}" for i in range(1, n + 1)],
            "experiment_group": group,
            "experiment_date": dates.strftime("%Y-%m-%d"),
            "country": country,
            "device_type": device,
            "customer_tenure": tenure,
            "transaction_value_usd": transaction_value,
            "checkout_completed": checkout_completed,
            "checkout_time_seconds": checkout_time,
            "payment_declined": payment_declined,
            "support_contact": support_contact,
            "fraud_flag": fraud_flag,
        }
    )


def generate_raw_data(n: int = N_CUSTOMERS, seed: int = SEED) -> pd.DataFrame:
    """Add deliberate quality issues to the otherwise clean synthetic data."""
    clean = generate_clean_data(n=n, seed=seed)
    rng = np.random.default_rng(seed + 100)

    raw = clean.copy()

    # Duplicate 24 experimental units.
    raw = pd.concat([raw, raw.sample(24, random_state=7)], ignore_index=True)

    # Missing treatment assignment.
    missing_idx = rng.choice(raw.index, 12, replace=False)
    raw.loc[missing_idx, "experiment_group"] = np.nan

    # Inconsistent country casing.
    casing_idx = rng.choice(raw.index, 18, replace=False)
    raw.loc[casing_idx, "country"] = raw.loc[casing_idx, "country"].str.lower()

    return raw


def build_training_sample(clean: pd.DataFrame) -> pd.DataFrame:
    """Create a small committed sample with known data-quality issues."""
    base = clean.sample(970, random_state=123).copy()
    duplicates = base.sample(10, random_state=5).copy()

    remaining = clean.drop(base.index)
    missing = remaining.sample(10, random_state=6).copy()
    missing["experiment_group"] = np.nan

    casing = remaining.drop(missing.index).sample(10, random_state=7).copy()
    casing["country"] = casing["country"].str.lower()

    sample = pd.concat([base, duplicates, missing, casing], ignore_index=True)
    return sample.sort_values(["customer_id", "experiment_group"], na_position="last")


def main() -> None:
    module_root = Path(__file__).resolve().parents[1]
    raw_dir = module_root / "data" / "raw"
    processed_dir = module_root / "data" / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    clean = generate_clean_data()
    raw = generate_raw_data()
    sample = build_training_sample(clean)

    raw.to_csv(raw_dir / "novapay_checkout_experiment_full.csv", index=False)
    sample.to_csv(raw_dir / "novapay_checkout_experiment_sample.csv", index=False)
    clean.to_csv(processed_dir / "novapay_checkout_experiment_clean_reference.csv", index=False)

    print(f"Generated {len(raw):,} raw rows")
    print(f"Generated {len(sample):,} training-sample rows")
    print(f"Generated {len(clean):,} clean-reference rows")


if __name__ == "__main__":
    main()
