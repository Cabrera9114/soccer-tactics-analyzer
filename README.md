# ⚽ Soccer Tactics Analyzer

An interactive AI-powered soccer analytics application that visualizes team formations, analyzes tactical structure, and generates coaching insights from player positioning data.

## Overview

Soccer Tactics Analyzer is a Streamlit-based project that combines data visualization, tactical analysis, and AI-generated feedback to simulate a lightweight soccer analytics platform.

The application allows users to explore team shape through multiple sample formations or uploaded CSV data, compare two teams on the same pitch, analyze spacing and passing lanes, generate AI tactical insights, and export results to a PDF report.

## Features

- **Formation Detection**
  - Estimates tactical shape such as 4-3-3, 4-4-2, and 3-5-2 using player position data

- **Player Position Visualization**
  - Displays players on a soccer pitch with optional labels
  - Shows tactical role lines for defense, midfield, and attack

- **Heatmap View**
  - Visualizes team positional density using a smoothed heatmap

- **Team Comparison**
  - Compares Team A and Team B on the same pitch

- **Tactical Metrics**
  - Team width
  - Team depth
  - Compactness
  - Average X spacing
  - Average Y spacing

- **Passing Lane Analysis**
  - Draws likely passing connections between nearby players

- **AI Tactical Analysis**
  - Generates short tactical summaries using the OpenAI API

- **AI Coaching Feedback**
  - Produces coaching-style recommendations based on formation and spacing

- **PDF Report Export**
  - Generates a downloadable tactical report with key metrics and AI insights

## Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **SciPy**
- **Scikit-learn**
- **OpenAI API**
- **ReportLab**

## Project Structure

```text
soccer-tactics-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── data/
│   ├── 433.csv
│   ├── 442.csv
│   ├── 352.csv
│   └── team_b.csv
│
├── utils/
│   ├── field_plot.py
│   ├── formation.py
│   ├── metrics.py
│   ├── summary.py
│   ├── ai_analysis.py
│   ├── ai_coach.py
│   └── report.py