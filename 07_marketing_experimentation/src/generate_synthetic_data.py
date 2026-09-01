from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 707
EXTRACT_AT = pd.Timestamp("2026-10-31T23:59:59Z")
SPLIT_EXPERIMENT = "HP_RETENTION_AB_2026_09"
FACTORIAL_EXPERIMENT = "HP_RETENTION_MVT_2026_09"


def _balanced_assignments(labels, per_label, rng):
    assignments = np.repeat(np.asarray(labels, dtype=object), per_label)
    rng.shuffle(assignments)
    return assignments


def _base_customers(size, start, rng, dual_consent=False):
    return pd.DataFrame(
        {
            "customer_id": [f"C{number:06d}" for number in range(start, start + size)],
            "lifecycle_segment": rng.choice(
                ["At Risk", "Needs Attention"], size=size, p=[0.68, 0.32]
            ),
            "value_band": rng.choice(
                ["High", "Medium", "Standard"], size=size, p=[0.19, 0.36, 0.45]
            ),
            "email_consent": True,
            "sms_consent": True if dual_consent else rng.random(size) < 0.72,
        }
    )


def _assignment_times(size, rng):
    base = pd.Timestamp("2026-09-01T09:00:00Z")
    minutes = rng.integers(0, 7 * 24 * 60, size=size)
    return base + pd.to_timedelta(minutes, unit="m")


def _binary_draw(probabilities, rng):
    return (rng.random(len(probabilities)) < probabilities).astype(int)


def _conversion_fields(frame, probabilities, rng):
    converted = _binary_draw(probabilities, rng)
    delay_hours = rng.integers(2, 14 * 24, size=len(frame))
    conversion_timestamp = frame["assigned_at"] + pd.to_timedelta(delay_hours, unit="h")
    conversion_timestamp = conversion_timestamp.where(converted.astype(bool), pd.NaT)
    base_revenue = rng.gamma(shape=2.3, scale=42, size=len(frame))
    value_multiplier = frame["value_band"].map({"High": 1.55, "Medium": 1.12, "Standard": 0.82})
    revenue = np.where(converted, np.maximum(18, base_revenue * value_multiplier), 0)
    return converted, conversion_timestamp, revenue


def _finish_value_and_guardrails(frame, rng):
    converted = frame["converted_14d"].astype(bool)
    revenue = frame["recognized_revenue_14d"].to_numpy()
    frame["product_cost_14d"] = np.round(revenue * rng.uniform(0.40, 0.50, len(frame)), 2)
    frame["discount_cost_14d"] = np.where(
        converted & frame["offer"].eq("discount_10"), np.round(revenue * 0.10, 2), 0
    )
    frame["shipping_subsidy_14d"] = np.where(
        converted & frame["offer"].eq("free_shipping"), 7.25, 0
    )
    frame["messaging_cost"] = np.where(frame["is_holdout"], 0, 0.01)
    frame["messaging_cost"] += np.where(frame["channel_plan"].eq("email_plus_sms"), 0.04, 0)
    refund_probability = np.where(frame["offer"].eq("discount_10"), 0.075, 0.052)
    frame["refunded_30d"] = converted.astype(int) * _binary_draw(refund_probability, rng)

    contacted = ~frame["is_holdout"]
    sms_contact = frame["channel_plan"].eq("email_plus_sms")
    frame["unsubscribed_14d"] = contacted.astype(int) * _binary_draw(
        np.where(sms_contact, 0.010, 0.007), rng
    )
    frame["complained_14d"] = contacted.astype(int) * _binary_draw(
        np.where(frame["message_framing"].eq("urgency_led"), 0.0027, 0.0016), rng
    )
    frame["sms_opt_out_14d"] = sms_contact.astype(int) * _binary_draw(
        np.repeat(0.008, len(frame)), rng
    )
    return frame


def generate_split_test(seed=SEED, per_arm=4_000):
    """Generate a balanced two-arm retention-message experiment."""
    rng = np.random.default_rng(seed)
    arms = ["control_current_reminder", "treatment_lifecycle_message"]
    frame = _base_customers(per_arm * len(arms), 1, rng)
    frame["assignment_id"] = [f"AB-{number:06d}" for number in range(1, len(frame) + 1)]
    frame["experiment_id"] = SPLIT_EXPERIMENT
    frame["experiment_type"] = "split_test"
    frame["assigned_at"] = _assignment_times(len(frame), rng)
    frame["extract_at"] = EXTRACT_AT
    frame["outcome_matured_at"] = frame["assigned_at"] + pd.Timedelta(days=14)
    frame["arm"] = _balanced_assignments(arms, per_arm, rng)
    treatment = frame["arm"].eq("treatment_lifecycle_message")
    frame["message_framing"] = np.where(treatment, "benefit_led", "current_reminder")
    frame["offer"] = "none"
    frame["channel_plan"] = "email_only"
    frame["is_holdout"] = False
    frame["planned_allocation"] = 0.5
    frame["delivered_email"] = _binary_draw(np.repeat(0.965, len(frame)), rng)
    frame["delivered_sms"] = 0
    exposure_delay = pd.to_timedelta(rng.integers(1, 18, len(frame)), unit="h")
    frame["exposed_at"] = (frame["assigned_at"] + exposure_delay).where(
        frame["delivered_email"].astype(bool), pd.NaT
    )
    baseline = np.where(frame["lifecycle_segment"].eq("At Risk"), 0.078, 0.101)
    probabilities = baseline + np.where(treatment, 0.014, 0)
    converted, timestamp, revenue = _conversion_fields(frame, probabilities, rng)
    frame["converted_14d"] = converted
    frame["conversion_timestamp"] = timestamp
    frame["recognized_revenue_14d"] = np.round(revenue, 2)
    return _finish_value_and_guardrails(frame, rng)


def factorial_arm_catalog():
    """Return the eight active factorial combinations and holdout."""
    active = []
    for message, offer, channel in product(
        ["benefit_led", "urgency_led"],
        ["free_shipping", "discount_10"],
        ["email_only", "email_plus_sms"],
    ):
        active.append(f"{message}__{offer}__{channel}")
    return ["holdout_no_contact", *active]


def generate_factorial_test(seed=SEED + 1, per_cell=2_000):
    """Generate a balanced 2x2x2 experiment plus no-contact holdout."""
    rng = np.random.default_rng(seed)
    arms = factorial_arm_catalog()
    frame = _base_customers(per_cell * len(arms), 100_001, rng, dual_consent=True)
    frame["assignment_id"] = [f"MVT-{number:06d}" for number in range(1, len(frame) + 1)]
    frame["experiment_id"] = FACTORIAL_EXPERIMENT
    frame["experiment_type"] = "factorial"
    frame["assigned_at"] = _assignment_times(len(frame), rng)
    frame["extract_at"] = EXTRACT_AT
    frame["outcome_matured_at"] = frame["assigned_at"] + pd.Timedelta(days=14)
    frame["arm"] = _balanced_assignments(arms, per_cell, rng)
    frame["is_holdout"] = frame["arm"].eq("holdout_no_contact")
    factors = frame["arm"].str.split("__", expand=True)
    frame["message_framing"] = np.where(frame["is_holdout"], "none", factors[0])
    frame["offer"] = np.where(frame["is_holdout"], "none", factors[1])
    frame["channel_plan"] = np.where(frame["is_holdout"], "none", factors[2])
    frame["planned_allocation"] = 1 / len(arms)

    active = ~frame["is_holdout"]
    email_probability = np.where(active, 0.958, 0)
    sms_probability = np.where(frame["channel_plan"].eq("email_plus_sms"), 0.925, 0)
    frame["delivered_email"] = _binary_draw(email_probability, rng)
    frame["delivered_sms"] = _binary_draw(sms_probability, rng)
    exposure_delay = pd.to_timedelta(rng.integers(1, 18, len(frame)), unit="h")
    frame["exposed_at"] = (frame["assigned_at"] + exposure_delay).where(
        frame["delivered_email"].astype(bool), pd.NaT
    )

    probabilities = np.where(frame["lifecycle_segment"].eq("At Risk"), 0.061, 0.079)
    probabilities = probabilities + np.where(active, 0.008, 0)
    probabilities = probabilities + np.where(frame["message_framing"].eq("benefit_led"), 0.006, 0)
    probabilities = probabilities + np.where(frame["offer"].eq("discount_10"), 0.011, 0.005)
    probabilities = probabilities + np.where(frame["channel_plan"].eq("email_plus_sms"), 0.007, 0)
    probabilities = probabilities + np.where(
        frame["message_framing"].eq("urgency_led") & frame["offer"].eq("discount_10"),
        0.004,
        0,
    )
    probabilities = probabilities + np.where(
        frame["offer"].eq("discount_10") & frame["channel_plan"].eq("email_plus_sms"),
        0.003,
        0,
    )
    converted, timestamp, revenue = _conversion_fields(frame, probabilities, rng)
    frame["converted_14d"] = converted
    frame["conversion_timestamp"] = timestamp
    frame["recognized_revenue_14d"] = np.round(revenue, 2)
    return _finish_value_and_guardrails(frame, rng)


def _choose_disjoint(rng, candidates, used, count):
    available = np.asarray(sorted(set(candidates) - used))
    selected = rng.choice(available, size=count, replace=False)
    used.update(int(index) for index in selected)
    return selected


def generate_raw_data(seed=SEED):
    """Combine both experiments and add a documented set of deliberate defects."""
    raw = pd.concat(
        [generate_split_test(seed), generate_factorial_test(seed + 1)], ignore_index=True
    )
    rng = np.random.default_rng(seed + 2)
    used = set()

    active = raw.index[~raw["is_holdout"]]
    exposure_defects = _choose_disjoint(rng, active, used, 12)
    raw.loc[exposure_defects, "exposed_at"] = raw.loc[
        exposure_defects, "assigned_at"
    ] - pd.Timedelta(hours=2)

    conversion_defects = _choose_disjoint(rng, raw.index, used, 10)
    raw.loc[conversion_defects, "converted_14d"] = 1
    raw.loc[conversion_defects, "conversion_timestamp"] = raw.loc[
        conversion_defects, "assigned_at"
    ] - pd.Timedelta(hours=1)
    raw.loc[conversion_defects, "recognized_revenue_14d"] = 55.0
    raw.loc[conversion_defects, "product_cost_14d"] = 24.75

    sms_candidates = raw.index[raw["channel_plan"].eq("email_plus_sms")]
    consent_defects = _choose_disjoint(rng, sms_candidates, used, 10)
    raw.loc[consent_defects, "sms_consent"] = False

    lifecycle_defects = _choose_disjoint(rng, raw.index, used, 10)
    raw.loc[lifecycle_defects, "lifecycle_segment"] = np.nan

    arm_defects = _choose_disjoint(rng, raw.index, used, 8)
    raw.loc[arm_defects, "arm"] = "invalid_variant"

    immature_defects = _choose_disjoint(rng, raw.index, used, 8)
    raw.loc[immature_defects, "assigned_at"] = pd.Timestamp("2026-10-27T09:00:00Z")
    raw.loc[immature_defects, "outcome_matured_at"] = raw.loc[
        immature_defects, "assigned_at"
    ] + pd.Timedelta(days=14)
    raw.loc[immature_defects, "converted_14d"] = 0
    raw.loc[immature_defects, "conversion_timestamp"] = pd.NaT
    raw.loc[immature_defects, "recognized_revenue_14d"] = 0.0
    raw.loc[immature_defects, "product_cost_14d"] = 0.0
    raw.loc[immature_defects, "discount_cost_14d"] = 0.0
    raw.loc[immature_defects, "shipping_subsidy_14d"] = 0.0
    raw.loc[immature_defects, "exposed_at"] = (
        raw.loc[immature_defects, "assigned_at"] + pd.Timedelta(hours=1)
    ).where(~raw.loc[immature_defects, "is_holdout"], pd.NaT)

    duplicates = raw.sample(20, random_state=seed)
    return pd.concat([raw, duplicates], ignore_index=True)


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_root = module_root / "data" / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    full_path = raw_root / "harbor_pine_experiment_assignments_full.csv"
    sample_path = raw_root / "harbor_pine_experiment_assignments_sample.csv"
    raw = generate_raw_data()
    raw.to_csv(full_path, index=False)
    raw.sample(4_000, random_state=SEED).to_csv(sample_path, index=False)
    print(f"Wrote {len(raw):,} rows to {full_path}")
    print(f"Wrote 4,000 inspectable rows to {sample_path}")


if __name__ == "__main__":
    main()
