import os
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / "data" / ".matplotlib")
)

import matplotlib
import numpy as np
import pandas as pd
from analyze_marketing_experiments import run_analysis

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

COLORS = {
    "navy": "#12263A",
    "blue": "#2E6F95",
    "teal": "#3AAFA9",
    "coral": "#E76F51",
    "gold": "#F2B134",
    "light": "#F4F7FA",
    "gray": "#5D6B78",
    "pale": "#DCE7EF",
}


def _short_arm(arm):
    message, offer, channel = arm.split("__")
    message_label = "Benefit" if message == "benefit_led" else "Urgency"
    offer_label = "10% off" if offer == "discount_10" else "Free ship"
    channel_label = "Email + SMS" if channel == "email_plus_sms" else "Email"
    return f"{message_label} · {offer_label} · {channel_label}"


def main():
    module_root = Path(__file__).resolve().parents[1]
    raw = pd.read_csv(module_root / "data/raw/harbor_pine_experiment_assignments_full.csv")
    results = run_analysis(raw)
    cells = results["factorial_cells"].sort_values("absolute_effect")
    effects = (
        results["factorial_effects"]
        .loc[results["factorial_effects"]["effect_type"].eq("main")]
        .copy()
    )

    fig = plt.figure(figsize=(16, 9), facecolor=COLORS["light"])
    grid = fig.add_gridspec(12, 24)
    fig.text(
        0.055,
        0.94,
        "Harbor & Pine experimentation decision",
        fontsize=25,
        weight="bold",
        color=COLORS["navy"],
    )
    fig.text(
        0.055,
        0.898,
        "Split test + 2 × 2 × 2 factorial · intention to treat · synthetic portfolio case",
        fontsize=11,
        color=COLORS["gray"],
    )

    kpis = [
        ("25,942", "validated assignments"),
        ("+2.67 pp", "winning cell vs holdout"),
        ("0.027", "Holm-adjusted p-value"),
        ("+$0.16", "margin/customer; uncertain"),
    ]
    for index, (value, label) in enumerate(kpis):
        x = 0.055 + index * 0.225
        fig.text(x, 0.82, value, fontsize=23, weight="bold", color=COLORS["blue"])
        fig.text(x, 0.785, label, fontsize=10, color=COLORS["gray"])

    ax_cells = fig.add_subplot(grid[4:10, 0:14])
    y = np.arange(len(cells))
    errors = np.vstack(
        [cells["absolute_effect"] - cells["ci_low"], cells["ci_high"] - cells["absolute_effect"]]
    )
    bar_colors = [
        COLORS["coral"] if credible else COLORS["pale"] for credible in cells["credible_after_holm"]
    ]
    ax_cells.barh(
        y,
        cells["absolute_effect"] * 100,
        xerr=errors * 100,
        color=bar_colors,
        ecolor=COLORS["gray"],
        capsize=3,
    )
    ax_cells.set_yticks(y, [_short_arm(arm) for arm in cells["arm"]], fontsize=9)
    ax_cells.axvline(0, color=COLORS["navy"], linewidth=1)
    ax_cells.set_xlabel("Conversion effect versus holdout (percentage points)")
    ax_cells.set_title(
        "Only one cell survives family-wise correction",
        loc="left",
        weight="bold",
        color=COLORS["navy"],
    )
    ax_cells.spines[["top", "right", "left"]].set_visible(False)
    ax_cells.grid(axis="x", alpha=0.18)

    ax_effects = fig.add_subplot(grid[4:7, 16:24])
    labels = ["Message", "Offer", "Channel"]
    values = effects["absolute_effect"].to_numpy() * 100
    lower = (effects["absolute_effect"] - effects["ci_low"]).to_numpy() * 100
    upper = (effects["ci_high"] - effects["absolute_effect"]).to_numpy() * 100
    effect_colors = [COLORS["pale"], COLORS["teal"], COLORS["pale"]]
    ax_effects.bar(
        labels,
        values,
        yerr=np.vstack([lower, upper]),
        color=effect_colors,
        ecolor=COLORS["gray"],
        capsize=4,
    )
    ax_effects.axhline(0, color=COLORS["navy"], linewidth=1)
    ax_effects.set_ylabel("Main effect (pp)")
    ax_effects.set_title(
        "Discount is the supported factor",
        loc="left",
        weight="bold",
        color=COLORS["navy"],
    )
    ax_effects.spines[["top", "right", "left"]].set_visible(False)
    ax_effects.grid(axis="y", alpha=0.18)

    fig.text(0.67, 0.34, "Recommended next stage", fontsize=13, weight="bold", color=COLORS["navy"])
    fig.text(
        0.67,
        0.292,
        "Urgency + 10% off + email",
        fontsize=17,
        weight="bold",
        color=COLORS["coral"],
    )
    fig.text(0.67, 0.247, "Retain a no-contact holdout.", fontsize=11, color=COLORS["gray"])
    fig.text(
        0.67,
        0.207,
        "Validate contribution margin before scale.",
        fontsize=11,
        color=COLORS["navy"],
    )
    fig.text(
        0.67,
        0.167,
        "Do not add SMS: no supported main effect.",
        fontsize=11,
        color=COLORS["navy"],
    )
    fig.text(
        0.055,
        0.055,
        "Decision boundary: conversion survives Holm correction; margin uncertainty still includes downside, so broad rollout is not approved.",
        fontsize=10,
        color=COLORS["gray"],
    )
    output = module_root / "reports/executive_summary.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
