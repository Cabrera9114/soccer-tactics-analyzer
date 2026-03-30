import pandas as pd
import numpy as np


def calculate_team_width(df: pd.DataFrame) -> float:
    return float(df["y"].max() - df["y"].min())


def calculate_team_depth(df: pd.DataFrame) -> float:
    return float(df["x"].max() - df["x"].min())


def calculate_compactness(df: pd.DataFrame) -> float:
    width = calculate_team_width(df)
    depth = calculate_team_depth(df)
    return float(width + depth)


def calculate_role_lines(df: pd.DataFrame):
    lines = {}

    for role in ["DEF", "MID", "FWD"]:
        role_df = df[df["role"] == role]
        if not role_df.empty:
            lines[role] = float(role_df["x"].mean())

    return lines


def calculate_spacing_metrics(df: pd.DataFrame):
    outfield = df[df["role"] != "GK"].copy()

    if len(outfield) < 2:
        return {"avg_x_spacing": 0.0, "avg_y_spacing": 0.0}

    x_sorted = np.sort(outfield["x"].to_numpy())
    y_sorted = np.sort(outfield["y"].to_numpy())

    avg_x_spacing = float(np.mean(np.diff(x_sorted))) if len(x_sorted) > 1 else 0.0
    avg_y_spacing = float(np.mean(np.diff(y_sorted))) if len(y_sorted) > 1 else 0.0

    return {
        "avg_x_spacing": avg_x_spacing,
        "avg_y_spacing": avg_y_spacing
    }


def calculate_passing_lanes(df: pd.DataFrame, max_distance: float = 18.0):
    outfield = df[df["role"] != "GK"].copy()
    lanes = []

    players = outfield[["player", "x", "y", "team"]].to_dict("records")

    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            p1 = players[i]
            p2 = players[j]

            if p1["team"] != p2["team"]:
                continue

            dx = p1["x"] - p2["x"]
            dy = p1["y"] - p2["y"]
            dist = float(np.sqrt(dx**2 + dy**2))

            if dist <= max_distance:
                lanes.append((p1, p2, dist))

    return lanes