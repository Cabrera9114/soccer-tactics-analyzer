import pandas as pd
import numpy as np


def estimate_formation(df: pd.DataFrame) -> str:
    """
    Estimate formation using outfield player x-position clustering.
    Returns classic outputs like 4-3-3, 4-4-2, 3-5-2 where possible.
    """

    outfield = df[df["role"] != "GK"].copy()

    if outfield.empty or len(outfield) < 10:
        return "Unknown"

    # Normalize direction so lower x = defensive line, higher x = attacking line
    x_vals = np.sort(outfield["x"].to_numpy())

    # Split into 3 lines using gaps
    gaps = np.diff(x_vals)

    if len(gaps) < 2:
        return "Unknown"

    # Get the two biggest gaps as line separators
    split_indices = np.argsort(gaps)[-2:]
    split_indices = np.sort(split_indices)

    idx1, idx2 = split_indices[0] + 1, split_indices[1] + 1

    line1 = x_vals[:idx1]
    line2 = x_vals[idx1:idx2]
    line3 = x_vals[idx2:]

    counts = [len(line1), len(line2), len(line3)]

    # Clean common edge cases
    if sum(counts) != 10:
        return "Unknown"

    return "-".join(map(str, counts))