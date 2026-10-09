"""Medical Insurance Cost Prediction & Analytics Dashboard - Main Entry Point.

Academic Deliverable: BE IV Year E&TC, Session 2026-27, Group No. 11, IET DAVV.
"""

import os
import sys
from pathlib import Path

# Ensure src/ is on sys.path for direct cloud execution (e.g., Streamlit Community Cloud)
src_path = str(Path(__file__).resolve().parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import streamlit as st

st.set_page_config(
    page_title="Medical Insurance Cost Predictor & Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

from insurance_app.data.loader import load_dataset
from insurance_app.data.validation import validate_dataset
from insurance_app.ui.components import render_disclaimer, render_metric_card
from insurance_app.ui.styling import apply_custom_css

# Apply consistent custom CSS
apply_custom_css()

# Header & Academic Attribution
st.title("🏥 Medical Insurance Cost Prediction & Analytics Dashboard")
st.caption(
    "Institute of Engineering & Technology, DAVV · B.Tech IV Year E&TC (Session 2026–27) · Group No. 11"
)

render_disclaimer()

st.markdown("""
Welcome to the interactive presentation dashboard for the **Medical Insurance Cost Prediction** academic project.
This system integrates exploratory data analytics, multi-model machine learning regression pipelines,
and an interactive what-if lifestyle simulation engine built with Python, Scikit-Learn, and Streamlit.
""")

# Quick KPI Metrics from loaded dataset
try:
    df = load_dataset()
    report = validate_dataset(df)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric_card("Dataset Size", f"{report.total_rows:,} records", "Kaggle source data")
    with col2:
        render_metric_card("Feature Count", f"{report.total_columns - 1} inputs", "Demographic & lifestyle")
    with col3:
        render_metric_card("Target Variable", "Charges ($ USD)", "Continuous hospital bill")
    with col4:
        render_metric_card("Data Quality", "100% Clean", "Zero missing values")

except Exception as err:
    st.warning(f"Note on Dataset: {err}")

st.markdown("---")

st.subheader("📌 Project Modules & Navigation")
st.markdown("Use the **sidebar on the left** to navigate through each phase of the project deliverable:")

m1, m2 = st.columns(2)
with m1:
    st.markdown("""
    * **[1. Overview & Data Analytics](pages/1_Overview.py):** Comprehensive exploratory data analysis (EDA), charge distributions, correlation heatmaps, and data validation reports.
    * **[2. Interactive Prediction](pages/2_Predict.py):** Enter individual patient profiles (age, BMI, smoker status, dependents) to generate instant cost estimates.
    """)
with m2:
    st.markdown("""
    * **[3. Model Insights & Comparison](pages/3_Model_Insights.py):** Compare Linear Regression, Random Forest, and Gradient Boosting on MAE, RMSE, and $R^2$ with residual plots and feature importance.
    * **[4. What-If Comparison Simulator](pages/4_What_If.py):** Simulate hypothetical scenarios (e.g. impact of quitting smoking or BMI changes) with delta cost breakdowns.
    * **[5. About & Academic Proforma](pages/5_About.py):** College project objectives, methodology, viva preparation, and citations.
    """)
