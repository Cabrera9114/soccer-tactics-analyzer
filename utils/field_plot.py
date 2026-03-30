import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter
from matplotlib.lines import Line2D


def draw_pitch():
    fig, ax = plt.subplots(figsize=(12, 8))

    # Outer boundaries
    ax.plot([0, 100], [0, 0], color="black")
    ax.plot([0, 100], [68, 68], color="black")
    ax.plot([0, 0], [0, 68], color="black")
    ax.plot([100, 100], [0, 68], color="black")

    # Halfway line
    ax.plot([50, 50], [0, 68], color="black")

    # Center circle
    center_circle = plt.Circle((50, 34), 9.15, color="black", fill=False)
    ax.add_patch(center_circle)

    # Left penalty area
    ax.plot([0, 16.5], [13.84, 13.84], color="black")
    ax.plot([16.5, 16.5], [13.84, 54.16], color="black")
    ax.plot([16.5, 0], [54.16, 54.16], color="black")

    # Right penalty area
    ax.plot([100, 83.5], [13.84, 13.84], color="black")
    ax.plot([83.5, 83.5], [13.84, 54.16], color="black")
    ax.plot([83.5, 100], [54.16, 54.16], color="black")

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 68)
    ax.set_aspect("equal")
    ax.axis("off")

    return fig, ax


def draw_tactical_lines(ax, role_lines):
    colors = {
        "DEF": "blue",
        "MID": "green",
        "FWD": "red"
    }

    for role, x in role_lines.items():
        flipped_x = 100 - x
        ax.axvline(
            x=flipped_x,
            linestyle="--",
            color=colors.get(role, "black"),
            alpha=0.4,
            linewidth=1
        )


def draw_passing_lanes(ax, lanes):
    for p1, p2, distance in lanes:
        if p1["team"] == "Team A":
            x1 = 100 - p1["x"] - 4
            x2 = 100 - p2["x"] - 4
        else:
            x1 = p1["x"] + 4
            x2 = p2["x"] + 4

        y1 = p1["y"]
        y2 = p2["y"]

        strength = max(0.1, 1 - distance / 50)

        ax.plot(
            [x1, x2],
            [y1, y2],
            color="gray",
            alpha=strength,
            linewidth=1 + 2 * strength
        )


def plot_players(df, role_lines=None, show_labels=True, passing_lanes=None):
    fig, ax = draw_pitch()

    colors = {
        "Team A": (0, 0, 1, 0.9),
        "Team B": (1, 0, 0, 0.75)
    }

    horizontal_shift = 4

    for _, row in df.iterrows():
        if row["team"] == "Team A":
            x = 100 - row["x"]
            x_plot = x - horizontal_shift
        else:
            x = row["x"]
            x_plot = x + horizontal_shift

        y_plot = row["y"]
        color = colors.get(row["team"], "black")

        ax.scatter(x_plot, y_plot, s=160, color=color)

        if show_labels:
            label = row["player"]

            if row["team"] == "Team A":
                ax.text(
                    x_plot - 2,
                    y_plot,
                    label,
                    fontsize=8,
                    ha="right",
                    va="center",
                    bbox=dict(facecolor="white", alpha=0.6, edgecolor="none")
                )
            else:
                ax.text(
                    x_plot + 2,
                    y_plot,
                    label,
                    fontsize=8,
                    ha="left",
                    va="center",
                    bbox=dict(facecolor="white", alpha=0.6, edgecolor="none")
                )

    if passing_lanes:
        draw_passing_lanes(ax, passing_lanes)

    if role_lines:
        draw_tactical_lines(ax, role_lines)

    legend_elements = [
        Line2D([0], [0], marker="o", color="w", label="Team A",
               markerfacecolor="blue", markersize=10),
        Line2D([0], [0], marker="o", color="w", label="Team B",
               markerfacecolor="red", markersize=10)
    ]

    ax.legend(handles=legend_elements, loc="upper right")
    ax.set_title("Team Shape Comparison", fontsize=14, pad=10)

    return fig


def plot_heatmap(df, flip=True):
    fig, ax = draw_pitch()

    x = df["x"].to_numpy()
    y = df["y"].to_numpy()

    if flip:
        x = 100 - x

    heatmap, _, _ = np.histogram2d(
        x,
        y,
        bins=(60, 40),
        range=[[0, 100], [0, 68]]
    )

    heatmap = gaussian_filter(heatmap, sigma=3)

    ax.imshow(
        heatmap.T,
        extent=[0, 100, 0, 68],
        origin="lower",
        cmap="Reds",
        alpha=0.7,
        aspect="auto"
    )

    ax.set_title("Team Position Heatmap", fontsize=14, pad=10)

    return fig