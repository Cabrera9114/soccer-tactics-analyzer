# ⚽ Soccer Tactics Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)
![AI Powered](https://img.shields.io/badge/AI-OpenAI%20API-purple)

---

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How It Works](#️-how-it-works)
- [Sample CSV Format](#-sample-csv-format)
- [Installation](#-installation)
- [Challenges Solved](#-challenges-solved)
- [Author](#-author)

---

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
```

## ⚙️ How It Works

The app reads player position data from CSV files and computes key tactical metrics such as **width, depth, compactness, and spacing**. It then visualizes the data on a soccer pitch, optionally overlays passing lanes, and uses AI to generate tactical analysis and coaching suggestions.

### Users can:
- Choose a sample formation  
- Upload their own CSV file  
- Switch between player view and heatmap view  
- Compare with a second team  
- Generate AI tactical analysis  
- Export a PDF report  

---

## 📄 Sample CSV Format

Your CSV file should include the following columns:

```csv
player,x,y,team,role
GK,5,34,Team A,GK
LB,20,10,Team A,DEF
LCB,22,26,Team A,DEF
RCB,22,42,Team A,DEF
RB,20,58,Team A,DEF
LCM,40,20,Team A,MID
CM,42,34,Team A,MID
RCM,40,48,Team A,MID
LW,65,12,Team A,FWD
ST,70,34,Team A,FWD
RW,65,56,Team A,FWD
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Cabrera9114/soccer-tactics-analyzer.git
cd soccer-tactics-analyzer
```

### 2. Create and activate a virtual environment (Windows PowerShell)

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env file

Add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🧩 Challenges Solved

During development, the project addressed several real-world issues:

- Field direction normalization  
- Label overlap in tactical visualizations  
- Multi-team comparison on the same pitch  
- Smoothed heatmap generation  
- AI prompt integration for coaching feedback  
- Exportable PDF reporting  

---

## 👨‍💻 Author

**Eduardo Cabrera-Lopez**  
Bachelor’s in Artificial Intelligence  
Houston Community College  

**GitHub:** https://github.com/Cabrera9114  
**LinkedIn:** https://www.linkedin.com/in/eduardo-cabrera-lopez-9122b0322