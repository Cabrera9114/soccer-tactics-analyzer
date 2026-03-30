def generate_tactical_summary(formation, width, depth, compactness, role_lines):
    summary = []

    summary.append(f"The estimated formation is {formation}.")
    summary.append(f"The team width is approximately {width:.2f} units.")
    summary.append(f"The team depth is approximately {depth:.2f} units.")
    summary.append(f"The overall compactness score is {compactness:.2f}.")

    if width > 40:
        summary.append("The team appears to use the full width of the field effectively.")
    else:
        summary.append("The team shape looks relatively narrow.")

    if depth > 50:
        summary.append("The team is stretched vertically, suggesting a more direct or expansive shape.")
    else:
        summary.append("The team remains fairly compact from back to front.")

    if "DEF" in role_lines and "MID" in role_lines:
        dm_gap = role_lines["MID"] - role_lines["DEF"]
        summary.append(f"The average distance between defense and midfield is {dm_gap:.2f} units.")

    if "MID" in role_lines and "FWD" in role_lines:
        mf_gap = role_lines["FWD"] - role_lines["MID"]
        summary.append(f"The average distance between midfield and attack is {mf_gap:.2f} units.")

    return " ".join(summary)