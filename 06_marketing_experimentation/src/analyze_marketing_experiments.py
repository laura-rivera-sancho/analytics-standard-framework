import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from generate_synthetic_data import FACTORIAL_EXPERIMENT, SPLIT_EXPERIMENT
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
from validate_experiment_data import (
    assignment_counts,
    clean_experiment_data,
    validation_report,
)

ALPHA = 0.05
POWER = 0.80
GUARDRAIL_THRESHOLDS = {
    "unsubscribed_14d": 0.015,
    "complained_14d": 0.005,
    "sms_opt_out_14d": 0.015,
    "refunded_30d": 0.090,
}


def required_sample_per_arm(baseline_rate, minimum_effect, alpha=ALPHA, power=POWER):
    """Return equal-allocation sample required per arm for a two-sided proportion test."""
    treatment_rate = baseline_rate + minimum_effect
    effect_size = abs(proportion_effectsize(baseline_rate, treatment_rate))
    required = NormalIndPower().solve_power(
        effect_size=effect_size,
        power=power,
        alpha=alpha,
        ratio=1,
        alternative="two-sided",
    )
    return int(math.ceil(required))


def detectable_absolute_effect(baseline_rate, n_control, n_treatment, alpha=ALPHA, power=POWER):
    """Translate detectable Cohen h back to an absolute probability difference."""
    ratio = n_treatment / n_control
    effect_size = NormalIndPower().solve_power(
        effect_size=None,
        nobs1=n_control,
        alpha=alpha,
        power=power,
        ratio=ratio,
        alternative="two-sided",
    )
    baseline_angle = math.asin(math.sqrt(baseline_rate))
    detectable_rate = math.sin(baseline_angle + effect_size / 2) ** 2
    return float(detectable_rate - baseline_rate)


def build_power_plan(clean):
    """Document planned and validated-sample sensitivity for the key estimands."""
    split = clean.loc[clean["experiment_id"].eq(SPLIT_EXPERIMENT)]
    split_counts = split.groupby("arm").size()
    active = clean.loc[clean["experiment_id"].eq(FACTORIAL_EXPERIMENT) & ~clean["is_holdout"]]
    message_counts = active.groupby("message_framing").size()
    cell_counts = active.groupby("arm").size()
    return pd.DataFrame(
        [
            {
                "estimand": "Split treatment vs control",
                "baseline_rate": 0.085,
                "minimum_effect": 0.015,
                "required_per_group": required_sample_per_arm(0.085, 0.015),
                "validated_group_1": int(split_counts.min()),
                "validated_group_2": int(split_counts.max()),
                "detectable_effect_validated": detectable_absolute_effect(
                    0.085, int(split_counts.min()), int(split_counts.max())
                ),
            },
            {
                "estimand": "Factorial pooled main effect",
                "baseline_rate": 0.075,
                "minimum_effect": 0.012,
                "required_per_group": required_sample_per_arm(0.075, 0.012),
                "validated_group_1": int(message_counts.min()),
                "validated_group_2": int(message_counts.max()),
                "detectable_effect_validated": detectable_absolute_effect(
                    0.075, int(message_counts.min()), int(message_counts.max())
                ),
            },
            {
                "estimand": "Active cell vs holdout",
                "baseline_rate": 0.070,
                "minimum_effect": 0.025,
                "required_per_group": required_sample_per_arm(0.070, 0.025),
                "validated_group_1": int(cell_counts.min()),
                "validated_group_2": int(
                    clean.loc[
                        clean["experiment_id"].eq(FACTORIAL_EXPERIMENT) & clean["is_holdout"]
                    ].shape[0]
                ),
                "detectable_effect_validated": detectable_absolute_effect(
                    0.070,
                    int(cell_counts.min()),
                    int(
                        clean.loc[
                            clean["experiment_id"].eq(FACTORIAL_EXPERIMENT) & clean["is_holdout"]
                        ].shape[0]
                    ),
                ),
            },
        ]
    )


def add_contribution_margin(df):
    """Derive contribution margin from inspectable value and cost components."""
    result = df.copy()
    refund_impact = result["refunded_30d"] * result["recognized_revenue_14d"]
    result["contribution_margin_14d"] = (
        result["recognized_revenue_14d"]
        - result["product_cost_14d"]
        - result["discount_cost_14d"]
        - result["shipping_subsidy_14d"]
        - result["messaging_cost"]
        - refund_impact
    )
    return result


def sample_ratio_checks(clean):
    """Run an assignment-count chi-square check for each experiment."""
    rows = []
    for experiment_id, experiment in clean.groupby("experiment_id"):
        counts = experiment.groupby("arm").size().sort_index()
        allocations = experiment.groupby("arm")["planned_allocation"].first().reindex(counts.index)
        expected = allocations / allocations.sum() * counts.sum()
        chi_square, p_value = stats.chisquare(counts.to_numpy(), expected.to_numpy())
        rows.append(
            {
                "experiment_id": experiment_id,
                "assigned_customers": int(counts.sum()),
                "arms": len(counts),
                "chi_square": float(chi_square),
                "p_value": float(p_value),
                "passes_at_0_01": bool(p_value >= 0.01),
            }
        )
    return pd.DataFrame(rows)


def binary_effect(control, treatment, outcome):
    """Estimate an unpooled Wald interval and pooled two-sided z-test."""
    control_values = control[outcome].astype(float)
    treatment_values = treatment[outcome].astype(float)
    n_control, n_treatment = len(control_values), len(treatment_values)
    control_rate, treatment_rate = control_values.mean(), treatment_values.mean()
    difference = treatment_rate - control_rate
    unpooled_se = math.sqrt(
        control_rate * (1 - control_rate) / n_control
        + treatment_rate * (1 - treatment_rate) / n_treatment
    )
    pooled = (control_values.sum() + treatment_values.sum()) / (n_control + n_treatment)
    pooled_se = math.sqrt(pooled * (1 - pooled) * (1 / n_control + 1 / n_treatment))
    z_stat = difference / pooled_se if pooled_se else 0.0
    p_value = 2 * stats.norm.sf(abs(z_stat))
    return {
        "control_n": n_control,
        "treatment_n": n_treatment,
        "control_rate": float(control_rate),
        "treatment_rate": float(treatment_rate),
        "absolute_effect": float(difference),
        "relative_lift": float(difference / control_rate) if control_rate else np.nan,
        "ci_low": float(difference - 1.96 * unpooled_se),
        "ci_high": float(difference + 1.96 * unpooled_se),
        "z_stat": float(z_stat),
        "p_value": float(p_value),
    }


def continuous_effect(control, treatment, outcome):
    """Estimate a mean difference with a Welch confidence interval and test."""
    control_values = control[outcome].astype(float)
    treatment_values = treatment[outcome].astype(float)
    test = stats.ttest_ind(treatment_values, control_values, equal_var=False)
    mean_difference = treatment_values.mean() - control_values.mean()
    variance = control_values.var(ddof=1) / len(control_values) + treatment_values.var(
        ddof=1
    ) / len(treatment_values)
    se = math.sqrt(variance)
    numerator = variance**2
    denominator = (control_values.var(ddof=1) / len(control_values)) ** 2 / (
        len(control_values) - 1
    ) + (treatment_values.var(ddof=1) / len(treatment_values)) ** 2 / (len(treatment_values) - 1)
    degrees_freedom = numerator / denominator
    critical = stats.t.ppf(0.975, degrees_freedom)
    return {
        "control_n": len(control_values),
        "treatment_n": len(treatment_values),
        "control_mean": float(control_values.mean()),
        "treatment_mean": float(treatment_values.mean()),
        "mean_effect": float(mean_difference),
        "ci_low": float(mean_difference - critical * se),
        "ci_high": float(mean_difference + critical * se),
        "p_value": float(test.pvalue),
    }


def arm_summary(clean):
    """Publish assignment, outcome, value, and guardrail summaries by arm."""
    return (
        clean.groupby(["experiment_id", "arm"], as_index=False)
        .agg(
            assigned_customers=("customer_id", "nunique"),
            conversion_rate=("converted_14d", "mean"),
            revenue_per_customer=("recognized_revenue_14d", "mean"),
            margin_per_customer=("contribution_margin_14d", "mean"),
            unsubscribe_rate=("unsubscribed_14d", "mean"),
            complaint_rate=("complained_14d", "mean"),
            sms_opt_out_rate=("sms_opt_out_14d", "mean"),
            refund_rate=("refunded_30d", "mean"),
            email_delivery_rate=("delivered_email", "mean"),
            sms_delivery_rate=("delivered_sms", "mean"),
        )
        .sort_values(["experiment_id", "arm"])
    )


def split_test_effects(clean):
    """Return the split-test primary, value, and guardrail effects."""
    split = clean.loc[clean["experiment_id"].eq(SPLIT_EXPERIMENT)]
    control = split.loc[split["arm"].eq("control_current_reminder")]
    treatment = split.loc[split["arm"].eq("treatment_lifecycle_message")]
    rows = []
    for outcome in [
        "converted_14d",
        "unsubscribed_14d",
        "complained_14d",
        "refunded_30d",
    ]:
        rows.append(
            {
                "metric": outcome,
                "metric_type": "binary",
                **binary_effect(control, treatment, outcome),
            }
        )
    for outcome in ["recognized_revenue_14d", "contribution_margin_14d"]:
        result = continuous_effect(control, treatment, outcome)
        rows.append({"metric": outcome, "metric_type": "continuous", **result})
    return pd.DataFrame(rows)


def _proportion_contrast(data, dimensions, weights, outcome="converted_14d"):
    grouped = data.groupby(dimensions)[outcome].agg(["sum", "count"])
    estimate = 0.0
    variance = 0.0
    for key, weight in weights.items():
        lookup = key if len(dimensions) > 1 else key[0]
        successes = grouped.loc[lookup, "sum"]
        count = grouped.loc[lookup, "count"]
        rate = successes / count
        estimate += weight * rate
        variance += weight**2 * rate * (1 - rate) / count
    se = math.sqrt(variance)
    z_stat = estimate / se if se else 0.0
    return {
        "absolute_effect": float(estimate),
        "ci_low": float(estimate - 1.96 * se),
        "ci_high": float(estimate + 1.96 * se),
        "z_stat": float(z_stat),
        "p_value": float(2 * stats.norm.sf(abs(z_stat))),
    }


def factorial_effects(clean):
    """Estimate pooled main effects and the two prespecified interactions."""
    active = clean.loc[clean["experiment_id"].eq(FACTORIAL_EXPERIMENT) & ~clean["is_holdout"]]
    rows = []
    contrasts = [
        ("message: benefit vs urgency", "message_framing", "urgency_led", "benefit_led"),
        ("offer: discount vs free shipping", "offer", "free_shipping", "discount_10"),
        ("channel: email+SMS vs email", "channel_plan", "email_only", "email_plus_sms"),
    ]
    for label, dimension, control_level, treatment_level in contrasts:
        result = binary_effect(
            active.loc[active[dimension].eq(control_level)],
            active.loc[active[dimension].eq(treatment_level)],
            "converted_14d",
        )
        rows.append({"effect": label, "effect_type": "main", **result})

    message_offer = _proportion_contrast(
        active,
        ["message_framing", "offer"],
        {
            ("benefit_led", "discount_10"): 1,
            ("urgency_led", "discount_10"): -1,
            ("benefit_led", "free_shipping"): -1,
            ("urgency_led", "free_shipping"): 1,
        },
    )
    rows.append(
        {
            "effect": "interaction: message × offer",
            "effect_type": "interaction",
            **message_offer,
        }
    )
    offer_channel = _proportion_contrast(
        active,
        ["offer", "channel_plan"],
        {
            ("discount_10", "email_plus_sms"): 1,
            ("free_shipping", "email_plus_sms"): -1,
            ("discount_10", "email_only"): -1,
            ("free_shipping", "email_only"): 1,
        },
    )
    rows.append(
        {
            "effect": "interaction: offer × channel",
            "effect_type": "interaction",
            **offer_channel,
        }
    )
    result = pd.DataFrame(rows)
    result["adjusted_p_value"] = multipletests(result["p_value"], method="holm")[1]
    result["credible_after_holm"] = result["adjusted_p_value"].lt(ALPHA)
    return result


def factorial_cells_vs_holdout(clean):
    """Compare each active cell with holdout and apply Holm control."""
    factorial = clean.loc[clean["experiment_id"].eq(FACTORIAL_EXPERIMENT)]
    holdout = factorial.loc[factorial["is_holdout"]]
    rows = []
    for arm, cell in factorial.loc[~factorial["is_holdout"]].groupby("arm"):
        conversion = binary_effect(holdout, cell, "converted_14d")
        margin = continuous_effect(holdout, cell, "contribution_margin_14d")
        rows.append(
            {
                "arm": arm,
                **conversion,
                "holdout_margin_per_customer": margin["control_mean"],
                "cell_margin_per_customer": margin["treatment_mean"],
                "incremental_margin_per_customer": margin["mean_effect"],
                "margin_ci_low": margin["ci_low"],
                "margin_ci_high": margin["ci_high"],
                "margin_p_value": margin["p_value"],
            }
        )
    result = pd.DataFrame(rows).sort_values("absolute_effect", ascending=False)
    result["adjusted_p_value"] = multipletests(result["p_value"], method="holm")[1]
    result["credible_after_holm"] = result["adjusted_p_value"].lt(ALPHA)
    result["positive_margin"] = result["incremental_margin_per_customer"].gt(0)
    return result


def guardrail_summary(clean):
    """Check every arm against prespecified absolute risk thresholds."""
    rows = []
    for (experiment_id, arm), group in clean.groupby(["experiment_id", "arm"]):
        for metric, threshold in GUARDRAIL_THRESHOLDS.items():
            rate = group[metric].mean()
            rows.append(
                {
                    "experiment_id": experiment_id,
                    "arm": arm,
                    "metric": metric,
                    "customers": len(group),
                    "rate": float(rate),
                    "threshold": threshold,
                    "passes": bool(rate <= threshold),
                }
            )
    return pd.DataFrame(rows)


def recommended_cell(cell_results, guardrails):
    """Select a staged-rollout candidate only when every decision gate passes."""
    factorial_guardrails = guardrails.loc[guardrails["experiment_id"].eq(FACTORIAL_EXPERIMENT)]
    safe_arms = set(
        factorial_guardrails.groupby("arm")["passes"].all().loc[lambda values: values].index
    )
    candidates = cell_results.loc[
        cell_results["credible_after_holm"]
        & cell_results["positive_margin"]
        & cell_results["arm"].isin(safe_arms)
    ].copy()
    if candidates.empty:
        return None
    candidates = candidates.sort_values(
        ["incremental_margin_per_customer", "absolute_effect"], ascending=False
    )
    return candidates.iloc[0]["arm"]


def run_analysis(raw):
    """Execute validation, health checks, inference, economics, and decision gates."""
    clean = add_contribution_margin(clean_experiment_data(raw))
    cells = factorial_cells_vs_holdout(clean)
    guardrails = guardrail_summary(clean)
    return {
        "validation": validation_report(raw),
        "clean": clean,
        "assignment_counts": assignment_counts(clean),
        "power_plan": build_power_plan(clean),
        "srm": sample_ratio_checks(clean),
        "arm_summary": arm_summary(clean),
        "split_effects": split_test_effects(clean),
        "factorial_effects": factorial_effects(clean),
        "factorial_cells": cells,
        "guardrails": guardrails,
        "recommended_cell": recommended_cell(cells, guardrails),
    }


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw_path = module_root / "data/raw/harbor_pine_experiment_assignments_full.csv"
    processed = module_root / "data/processed"
    results = run_analysis(pd.read_csv(raw_path))
    processed.mkdir(parents=True, exist_ok=True)
    tables = {
        "assignment_counts": results["assignment_counts"],
        "power_plan": results["power_plan"],
        "sample_ratio_checks": results["srm"],
        "arm_summary": results["arm_summary"],
        "split_effects": results["split_effects"],
        "factorial_effects": results["factorial_effects"],
        "factorial_cells_vs_holdout": results["factorial_cells"],
        "guardrail_summary": results["guardrails"],
    }
    for name, table in tables.items():
        table.to_csv(processed / f"{name}.csv", index=False)
    summary = {
        "validation": results["validation"],
        "recommended_cell": results["recommended_cell"],
    }
    (processed / "analysis_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(results["srm"].round(4).to_string(index=False))
    print("\nSplit effects\n", results["split_effects"].round(4).to_string(index=False))
    print("\nFactorial effects\n", results["factorial_effects"].round(4).to_string(index=False))
    print("\nTop cells\n", results["factorial_cells"].head(4).round(4).to_string(index=False))
    print(f"\nRecommended staged-rollout cell: {results['recommended_cell']}")


if __name__ == "__main__":
    main()
