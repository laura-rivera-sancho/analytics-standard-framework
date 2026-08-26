from pathlib import Path

import numpy as np
import pandas as pd

SEED = 84
LAUNCH_DATE = pd.Timestamp("2026-04-01")
START_DATE = pd.Timestamp("2026-02-01")
END_DATE = pd.Timestamp("2026-05-31")
CAMPAIGN_START = pd.Timestamp("2026-05-04")
CAMPAIGN_END = pd.Timestamp("2026-05-10")


def _logit(p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def _sigmoid(x):
    return 1 / (1 + np.exp(-x))


def generate_clean_data(seed=SEED):
    """Generate the clean synthetic FinFlow transaction-level reference dataset."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(START_DATE, END_DATE, freq="D")
    rows = []
    transaction_counter = 1

    for date in dates:
        dow = date.dayofweek
        days_from_launch = (date - LAUNCH_DATE).days
        post = int(date >= LAUNCH_DATE)
        ramp = int(LAUNCH_DATE <= date <= LAUNCH_DATE + pd.Timedelta(days=6))
        campaign = int(CAMPAIGN_START <= date <= CAMPAIGN_END)

        # Day-of-week volume pattern plus campaign lift.
        weekday_factor = 1.00 if dow < 5 else 0.78
        trend_factor = 1 + 0.0012 * (date - START_DATE).days
        campaign_factor = 1.34 if campaign else 1.0
        mean_volume = 560 * weekday_factor * trend_factor * campaign_factor
        daily_n = max(250, int(rng.normal(mean_volume, 30)))

        # Post period intentionally shifts traffic mix modestly.
        country_probs = (
            np.array([0.48, 0.22, 0.10, 0.20]) if not post else np.array([0.44, 0.24, 0.10, 0.22])
        )
        device_probs = np.array([0.67, 0.33]) if not post else np.array([0.72, 0.28])
        new_share = 0.36 + (0.07 if post else 0.0) + (0.10 if campaign else 0.0)
        new_share = min(new_share, 0.62)
        tenure_probs = np.array([new_share, 1 - new_share])
        risk_probs = np.array([0.59, 0.31, 0.10]) if not post else np.array([0.56, 0.32, 0.12])

        countries = rng.choice(["US", "MX", "CR", "BR"], size=daily_n, p=country_probs)
        devices = rng.choice(["Mobile", "Desktop"], size=daily_n, p=device_probs)
        tenures = rng.choice(["New", "Existing"], size=daily_n, p=tenure_probs)
        risks = rng.choice(["Low", "Medium", "High"], size=daily_n, p=risk_probs)

        # Transaction values are intentionally right-skewed.
        values = np.clip(rng.lognormal(mean=np.log(78), sigma=0.85, size=daily_n), 5, 2500)

        # Completion has a mild baseline improvement trend, a positive launch level effect,
        # a smaller post-launch slope improvement, and weaker performance during ramp.
        pre_trend = 0.00032 * (date - START_DATE).days
        level_effect = 0.035 if post else 0.0
        post_slope = 0.00020 * max(days_from_launch, 0)
        ramp_penalty = -0.022 if ramp else 0.0
        weekend_penalty = -0.008 if dow >= 5 else 0.0

        base_completion = (
            0.842 + pre_trend + level_effect + post_slope + ramp_penalty + weekend_penalty
        )
        logodds = _logit(base_completion)
        logodds += np.where(devices == "Mobile", -0.08, 0.03)
        logodds += np.where(tenures == "Existing", 0.14, -0.08)
        logodds += np.select([risks == "Medium", risks == "High"], [-0.22, -0.62], default=0.08)
        logodds += np.where(countries == "BR", -0.08, 0.0)
        completion_prob = _sigmoid(logodds)
        completed = rng.binomial(1, completion_prob)

        # Manual review falls materially after automation, except during the ramp and for high-risk cases.
        manual_prob = 0.265 - (0.105 if post else 0.0) + (0.035 if ramp else 0.0)
        manual_prob = np.full(daily_n, manual_prob, dtype=float)
        manual_prob += np.select([risks == "Medium", risks == "High"], [0.13, 0.36], default=-0.05)
        manual_prob += np.where(values > 300, 0.06, 0.0)
        manual_prob = np.clip(manual_prob, 0.01, 0.92)
        manual = rng.binomial(1, manual_prob)

        # Verification time is right-skewed; automation reduces the central tendency.
        mean_seconds = 96 - (31 if post else 0) + (10 if ramp else 0) + (8 if dow >= 5 else 0)
        mean_seconds += np.where(manual == 1, 54, -8)
        mean_seconds += np.select([risks == "Medium", risks == "High"], [10, 28], default=-4)
        mean_seconds = np.clip(mean_seconds, 18, None)
        sigma = 0.52
        verification_time = rng.lognormal(np.log(mean_seconds) - 0.5 * sigma**2, sigma)
        verification_time = np.clip(verification_time, 5, 1800)

        # Guardrails. Fraud is intentionally rare and slightly noisy post-launch.
        decline_prob = 0.061 + np.select(
            [risks == "Medium", risks == "High"], [0.028, 0.115], default=-0.010
        )
        decline_prob += np.where(countries == "BR", 0.010, 0.0)
        decline_prob += 0.001 if post else 0.0
        declined = rng.binomial(1, np.clip(decline_prob, 0.005, 0.35))

        support_prob = 0.049 - (0.010 if post else 0.0) + (0.008 if ramp else 0.0)
        support_prob = np.full(daily_n, support_prob, dtype=float)
        support_prob += np.where(completed == 0, 0.045, 0.0)
        support_prob += np.where(manual == 1, 0.016, 0.0)
        support = rng.binomial(1, np.clip(support_prob, 0.005, 0.25))

        fraud_prob = 0.0032 + (0.00035 if post else 0.0)
        fraud_prob = np.full(daily_n, fraud_prob, dtype=float)
        fraud_prob += np.select(
            [risks == "Medium", risks == "High"], [0.0018, 0.0095], default=-0.0008
        )
        fraud_prob += np.where(values > 350, 0.0022, 0.0)
        fraud = rng.binomial(1, np.clip(fraud_prob, 0.0005, 0.04))

        customer_pool = np.arange(1, 26001)
        customer_ids = rng.choice(customer_pool, size=daily_n, replace=True)

        for i in range(daily_n):
            rows.append(
                {
                    "transaction_id": f"TXN{transaction_counter:07d}",
                    "customer_id": f"CUST{customer_ids[i]:06d}",
                    "transaction_date": date.strftime("%Y-%m-%d"),
                    "period": "Post" if post else "Pre",
                    "days_from_launch": days_from_launch,
                    "post_flag": post,
                    "ramp_flag": ramp,
                    "campaign_flag": campaign,
                    "country": countries[i],
                    "device_type": devices[i],
                    "customer_tenure": tenures[i],
                    "risk_tier": risks[i],
                    "transaction_value_usd": round(float(values[i]), 2),
                    "verification_completed": int(completed[i]),
                    "verification_time_seconds": round(float(verification_time[i]), 2),
                    "manual_review": int(manual[i]),
                    "payment_declined": int(declined[i]),
                    "support_contact": int(support[i]),
                    "fraud_confirmed": int(fraud[i]),
                }
            )
            transaction_counter += 1

    return pd.DataFrame(rows)


def generate_raw_data(seed=SEED):
    """Add deliberate data-quality defects to the clean reference data."""
    rng = np.random.default_rng(seed + 1)
    clean = generate_clean_data(seed)
    raw = clean.copy()

    # Duplicate transactions.
    duplicate_rows = raw.sample(32, random_state=seed).copy()
    raw = pd.concat([raw, duplicate_rows], ignore_index=True)

    # Missing critical/context fields.
    idx = rng.choice(raw.index, size=24, replace=False)
    raw.loc[idx[:10], "risk_tier"] = None
    raw.loc[idx[10:16], "device_type"] = None
    raw.loc[idx[16:], "verification_time_seconds"] = np.nan

    # Inconsistent casing.
    idx = rng.choice(raw.index, size=28, replace=False)
    raw.loc[idx, "country"] = raw.loc[idx, "country"].str.lower()

    # Implausible duration values.
    idx = rng.choice(raw.index, size=12, replace=False)
    raw.loc[idx[:4], "verification_time_seconds"] = -5
    raw.loc[idx[4:], "verification_time_seconds"] = rng.integers(5000, 12000, size=8)

    # Corrupt a few derived flags so the analysis must re-derive them from date.
    idx = rng.choice(raw.index, size=16, replace=False)
    raw.loc[idx, "post_flag"] = 1 - raw.loc[idx, "post_flag"]

    return raw.sample(frac=1, random_state=seed + 2).reset_index(drop=True)


def build_training_sample(raw, n=1000, seed=SEED):
    """Create a compact portfolio sample that preserves deliberate defects."""
    rng = np.random.default_rng(seed + 3)
    base = raw.drop_duplicates("transaction_id").sample(n - 30, random_state=seed).copy()

    duplicates = base.sample(10, random_state=seed + 1).copy()
    casing = base.sample(10, random_state=seed + 2).copy()
    casing["country"] = casing["country"].astype(str).str.lower()
    anomalies = base.sample(10, random_state=seed + 3).copy()
    anomalies.loc[anomalies.index[:4], "verification_time_seconds"] = -5
    anomalies.loc[anomalies.index[4:], "verification_time_seconds"] = rng.integers(
        5000, 9000, size=6
    )

    sample = pd.concat([base, duplicates, casing, anomalies], ignore_index=True)
    return sample.sample(frac=1, random_state=seed + 4).reset_index(drop=True)


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_dir = module_root / "data" / "raw"
    processed_dir = module_root / "data" / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    clean = generate_clean_data()
    raw = generate_raw_data()
    sample = build_training_sample(raw)

    raw.to_csv(raw_dir / "finflow_verification_pre_post_full.csv", index=False)
    sample.to_csv(raw_dir / "finflow_verification_pre_post_sample.csv", index=False)
    clean.to_csv(processed_dir / "finflow_verification_clean_reference.csv", index=False)

    print(f"Clean reference rows: {len(clean):,}")
    print(f"Raw training rows: {len(raw):,}")
    print(f"Portfolio sample rows: {len(sample):,}")


if __name__ == "__main__":
    main()
