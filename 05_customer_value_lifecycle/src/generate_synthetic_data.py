from pathlib import Path

import numpy as np
import pandas as pd

SEED = 606
AS_OF_DATE = pd.Timestamp("2026-08-31")


def _order_offsets(rng, profile, count):
    if profile == "champion":
        return (rng.beta(1.0, 3.2, count) * 360).astype(int)
    if profile == "loyal":
        return (rng.beta(1.5, 2.2, count) * 420).astype(int)
    if profile == "promising":
        return rng.integers(2, 150, count)
    if profile == "at_risk":
        return rng.integers(115, 520, count)
    return rng.integers(370, 720, count)


def generate_clean_data(seed=SEED, customers=3_000):
    """Generate fictional customer-order history with deliberate lifecycle patterns."""
    rng = np.random.default_rng(seed)
    customer_ids = [f"C{number:05d}" for number in range(1, customers + 1)]
    profiles = rng.choice(
        ["champion", "loyal", "promising", "at_risk", "hibernating"],
        customers,
        p=[0.14, 0.29, 0.22, 0.20, 0.15],
    )
    channels = rng.choice(
        ["organic", "paid_search", "paid_social", "email", "referral"],
        customers,
        p=[0.31, 0.23, 0.17, 0.12, 0.17],
    )
    countries = rng.choice(["US", "MX", "BR", "CR"], customers, p=[0.42, 0.24, 0.22, 0.12])
    consent = rng.random(customers) < 0.78
    created_offsets = rng.integers(30, 720, customers)
    rows = []
    order_number = 1

    order_counts = {
        "champion": lambda: rng.poisson(13) + 5,
        "loyal": lambda: rng.poisson(7) + 3,
        "promising": lambda: rng.poisson(2) + 1,
        "at_risk": lambda: rng.poisson(7) + 2,
        "hibernating": lambda: rng.poisson(3) + 1,
    }
    revenue_scale = {
        "champion": 125,
        "loyal": 82,
        "promising": 58,
        "at_risk": 96,
        "hibernating": 49,
    }

    for customer_id, profile, channel, country, has_consent, created_offset in zip(
        customer_ids, profiles, channels, countries, consent, created_offsets, strict=True
    ):
        created_at = AS_OF_DATE - pd.Timedelta(days=int(created_offset))
        count = int(order_counts[profile]())
        offsets = _order_offsets(rng, profile, count)
        order_dates = AS_OF_DATE - pd.to_timedelta(offsets, unit="D")
        order_dates = [max(date, created_at + pd.Timedelta(days=1)) for date in order_dates]

        for order_date in sorted(order_dates):
            revenue = max(8, rng.gamma(shape=2.4, scale=revenue_scale[profile] / 2.4))
            rows.append(
                {
                    "customer_id": customer_id,
                    "customer_created_at": created_at.strftime("%Y-%m-%d"),
                    "acquisition_channel": channel,
                    "country_code": country,
                    "marketing_consent": bool(has_consent),
                    "order_id": f"O{order_number:07d}",
                    "order_timestamp": order_date.strftime("%Y-%m-%d"),
                    "recognized_revenue": round(revenue, 2),
                }
            )
            order_number += 1
    return pd.DataFrame(rows)


def generate_raw_data(seed=SEED, customers=3_000):
    """Add inspectable defects so quality control precedes segmentation."""
    rng = np.random.default_rng(seed + 1)
    raw = generate_clean_data(seed, customers)

    missing_channel = rng.choice(raw.index, 25, replace=False)
    raw.loc[missing_channel, "acquisition_channel"] = np.nan

    negative_revenue = rng.choice(raw.index.difference(missing_channel), 15, replace=False)
    raw.loc[negative_revenue, "recognized_revenue"] = -10

    future_orders = rng.choice(
        raw.index.difference(np.concatenate([missing_channel, negative_revenue])),
        12,
        replace=False,
    )
    raw.loc[future_orders, "order_timestamp"] = "2026-09-15"

    duplicates = raw.sample(30, random_state=seed)
    return pd.concat([raw, duplicates], ignore_index=True)


def main():
    module_root = Path(__file__).resolve().parents[1]
    full_path = module_root / "data" / "raw" / "harbor_pine_orders_full.csv"
    sample_path = module_root / "data" / "raw" / "harbor_pine_orders_sample.csv"
    full_path.parent.mkdir(parents=True, exist_ok=True)
    raw = generate_raw_data()
    raw.to_csv(full_path, index=False)
    raw.sample(3_000, random_state=SEED).to_csv(sample_path, index=False)
    print(f"Wrote {len(raw):,} rows to {full_path}")
    print(f"Wrote 3,000 inspectable rows to {sample_path}")


if __name__ == "__main__":
    main()
