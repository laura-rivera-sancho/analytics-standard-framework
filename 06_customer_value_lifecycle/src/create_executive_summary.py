import os
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / "data" / ".matplotlib")
)

import matplotlib
import pandas as pd
from analyze_customer_value import run_analysis

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

COLORS = {
    "navy": "#12263A",
    "blue": "#2E6F95",
    "teal": "#3AAFA9",
    "gold": "#F2B134",
    "coral": "#E76F51",
    "light": "#F4F7FA",
    "gray": "#5D6B78",
}


def main():
    module_root = Path(__file__).resolve().parents[1]
    data = pd.read_csv(module_root / "data/raw/harbor_pine_orders_full.csv")
    results = run_analysis(data)
    profiles = results["profiles"].sort_values("value_share")
    movement = results["migration_summary"].reindex(["Improved", "Stable", "Declined"])
    activation = results["activation"]

    fig = plt.figure(figsize=(16, 9), facecolor=COLORS["light"])
    grid = fig.add_gridspec(12, 24)
    fig.text(
        0.055,
        0.935,
        "Harbor & Pine customer value decision",
        fontsize=25,
        weight="bold",
        color=COLORS["navy"],
    )
    fig.text(
        0.055,
        0.895,
        "RFM snapshot as of 31 Aug 2026 · trailing 365 days · synthetic portfolio case",
        fontsize=11,
        color=COLORS["gray"],
    )

    kpis = [
        ("3,000", "customers profiled"),
        ("55.5%", "value from Champions"),
        ("503", "At Risk customers"),
        ("$323.2K", "value in first wave"),
    ]
    for index, (value, label) in enumerate(kpis):
        x = 0.055 + index * 0.225
        fig.text(x, 0.82, value, fontsize=24, weight="bold", color=COLORS["blue"])
        fig.text(x, 0.785, label, fontsize=10, color=COLORS["gray"])

    ax_value = fig.add_subplot(grid[4:10, 0:14])
    y = range(len(profiles))
    ax_value.barh(
        [position - 0.18 for position in y],
        profiles["value_share"] * 100,
        height=0.34,
        color=COLORS["blue"],
        label="Value share",
    )
    ax_value.barh(
        [position + 0.18 for position in y],
        profiles["customer_share"] * 100,
        height=0.34,
        color=COLORS["teal"],
        label="Customer share",
    )
    ax_value.set_yticks(list(y), profiles.index)
    ax_value.set_xlabel("Share of total (%)")
    ax_value.set_title(
        "Value is concentrated among Champions", loc="left", weight="bold", color=COLORS["navy"]
    )
    ax_value.legend(frameon=False, ncol=2, loc="lower right")
    ax_value.spines[["top", "right", "left"]].set_visible(False)
    ax_value.grid(axis="x", alpha=0.18)

    ax_move = fig.add_subplot(grid[4:9, 16:24])
    ax_move.set_position([0.68, 0.43, 0.28, 0.28])
    movement_colors = [COLORS["teal"], COLORS["blue"], COLORS["coral"]]
    ax_move.bar(movement.index, movement["customers"], color=movement_colors)
    for position, value in enumerate(movement["customers"]):
        ax_move.text(
            position,
            value + 25,
            f"{int(value):,}",
            ha="center",
            weight="bold",
            color=COLORS["navy"],
        )
    ax_move.set_ylim(0, movement["customers"].max() * 1.25)
    ax_move.set_title(
        "Quarterly lifecycle movement", loc="left", weight="bold", color=COLORS["navy"]
    )
    ax_move.spines[["top", "right", "left"]].set_visible(False)
    ax_move.tick_params(axis="y", left=False, labelleft=False)

    fig.text(0.67, 0.31, "Recommended first wave", fontsize=13, weight="bold", color=COLORS["navy"])
    fig.text(
        0.67,
        0.265,
        f"{len(activation):,} consented customers",
        fontsize=17,
        weight="bold",
        color=COLORS["coral"],
    )
    fig.text(0.67, 0.225, "398 At Risk · 102 Needs Attention", fontsize=10.5, color=COLORS["gray"])
    fig.text(
        0.67, 0.185, "Run a randomized holdout before scaling.", fontsize=10.5, color=COLORS["navy"]
    )

    fig.text(
        0.055,
        0.055,
        "Decision boundary: RFM is descriptive; the activation is a controlled test, not an impact forecast.",
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
