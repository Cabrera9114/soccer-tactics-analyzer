import streamlit as st
import pandas as pd

from utils.field_plot import plot_players, plot_heatmap
from utils.formation import estimate_formation
from utils.metrics import (
    calculate_team_width,
    calculate_team_depth,
    calculate_compactness,
    calculate_role_lines,
    calculate_spacing_metrics,
    calculate_passing_lanes,
)
from utils.summary import generate_tactical_summary
from utils.ai_analysis import generate_ai_analysis
from utils.ai_coach import generate_coaching_feedback
from utils.report import generate_pdf

st.set_page_config(page_title="Soccer Tactics Analyzer", layout="wide")

st.title("⚽ Soccer Tactics Analyzer")
st.write("Upload player position data to visualize team shape, estimate formation, and analyze tactics.")

option = st.selectbox(
    "Choose Formation Example",
    ["4-3-3", "4-4-2", "3-5-2"]
)

file_map = {
    "4-3-3": "data/433.csv",
    "4-4-2": "data/442.csv",
    "3-5-2": "data/352.csv"
}

uploaded_file = st.file_uploader("Upload your own CSV (optional)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.info("Using uploaded CSV file")
else:
    selected_file = file_map[option]
    df = pd.read_csv(selected_file)
    st.info(f"Using sample data for {option}: {selected_file}")
    st.write("Currently loaded file:", selected_file)

view_mode = st.radio(
    "Choose Visualization",
    ["Player Positions", "Heatmap"],
    horizontal=True
)

col_a, col_b, col_c = st.columns(3)
show_labels = col_a.checkbox("Show Player Labels", value=True)
show_passing_lanes = col_b.checkbox("Show Passing Lanes", value=False)
compare_mode = col_c.checkbox("Compare with Team B", value=False)

if compare_mode:
    df_b = pd.read_csv("data/team_b.csv")
else:
    df_b = None

required_columns = {"player", "x", "y", "team", "role"}

if not required_columns.issubset(df.columns):
    st.error(f"CSV must contain these columns: {required_columns}")
    st.stop()

st.subheader("Player Position Data")

if df_b is not None:
    st.dataframe(pd.concat([df, df_b], ignore_index=True))
else:
    st.dataframe(df)

# Analyze Team A if present, otherwise analyze all uploaded data
if "Team A" in df["team"].unique():
    df_analysis = df[df["team"] == "Team A"].copy()
else:
    df_analysis = df.copy()

formation = estimate_formation(df_analysis)
width = calculate_team_width(df_analysis)
depth = calculate_team_depth(df_analysis)
compactness = calculate_compactness(df_analysis)
role_lines = calculate_role_lines(df_analysis)
spacing_metrics = calculate_spacing_metrics(df_analysis)

if df_b is not None:
    df_plot = pd.concat([df, df_b], ignore_index=True)
else:
    df_plot = df

if show_passing_lanes:
    if df_b is not None:
        passing_lanes = calculate_passing_lanes(df_plot)
    else:
        passing_lanes = calculate_passing_lanes(df_analysis)
else:
    passing_lanes = None

st.subheader("Team Shape Visualization")

if view_mode == "Player Positions":
    fig = plot_players(df_plot, role_lines, show_labels, passing_lanes)
else:
    fig = plot_heatmap(df_analysis)

st.pyplot(fig)

summary = generate_tactical_summary(formation, width, depth, compactness, role_lines)

col1, col2, col3 = st.columns(3)
col1.metric("Estimated Formation", formation)
col2.metric("Team Width", f"{width:.2f}")
col3.metric("Team Depth", f"{depth:.2f}")

col4, col5 = st.columns(2)
col4.metric("Avg X Spacing", f"{spacing_metrics['avg_x_spacing']:.2f}")
col5.metric("Avg Y Spacing", f"{spacing_metrics['avg_y_spacing']:.2f}")

st.subheader("Tactical Summary")
st.write(summary)

st.subheader("🤖 AI Tactical Analysis")

if st.button("Generate AI Analysis"):
    with st.spinner("Analyzing tactics with AI..."):
        ai_text = generate_ai_analysis(formation, width, depth, compactness)
        st.markdown(f"### 📊 AI Insight\n\n{ai_text}")

st.subheader("🧠 AI Tactical Coaching Feedback")

if st.button("Generate Coaching Feedback"):
    with st.spinner("Generating coaching feedback..."):
        coaching_text = generate_coaching_feedback(
            formation,
            width,
            depth,
            compactness,
            spacing_metrics
        )
        st.markdown(f"### 🎯 Coaching Notes\n\n{coaching_text}")

st.subheader("📄 Export Tactical Report")

if st.button("Generate PDF Report"):
    with st.spinner("Generating PDF report..."):
        report_text = generate_coaching_feedback(
            formation,
            width,
            depth,
            compactness,
            spacing_metrics
        )

        filename = "soccer_tactics_report.pdf"

        generate_pdf(
            filename,
            formation,
            width,
            depth,
            compactness,
            spacing_metrics,
            report_text
        )

        with open(filename, "rb") as f:
            st.download_button(
                label="Download PDF Report",
                data=f,
                file_name=filename,
                mime="application/pdf"
            )