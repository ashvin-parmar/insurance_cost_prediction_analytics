import sys
from pathlib import Path

# Ensure src/ is on sys.path for direct execution / cloud platforms
src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import streamlit as st

from insurance_app.ui.components import render_disclaimer
from insurance_app.ui.styling import apply_custom_css

apply_custom_css()

st.title("ℹ️ Module E: About the Project & Academic Proforma")
st.caption("Project Documentation, Academic Proforma-I, and Methodology Overview.")

render_disclaimer()

# Academic Information Card
st.subheader("🎓 Academic Institutional Context")
st.markdown("""
* **Institution:** Institute of Engineering & Technology (IET), Devi Ahilya Vishwavidyalaya (DAVV), Indore
* **Program:** Bachelor of Technology (B.Tech) IV Year, Electronics & Telecommunication (E&TC)
* **Academic Session:** 2026–2027
* **Section:** B · **Group No.:** 11
* **Project Title:** Medical Insurance Cost Prediction Using Machine Learning
* **Domain:** Software / Predictive Machine Learning
""")

st.markdown("---")

# Objectives
st.subheader("🎯 Project Objectives (Proforma-I Aligned)")
st.markdown("""
1. **Predictive System:** Develop a machine-learning-based predictive system for estimating the approximate medical insurance charges of an individual.
2. **Feature Relationship Identification:** Identify important demographic and lifestyle features that have a significant relationship with predicted medical costs.
3. **Categorical Transformation:** Transform categorical attributes into ML-compatible formats using robust one-hot encoding techniques.
4. **Multi-Model Comparison:** Train multiple regression algorithms (Linear Regression, Random Forest, Gradient Boosting) and systematically benchmark their predictive performance.
5. **Rigorous Metric Evaluation:** Evaluate models using industry-standard regression metrics: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Coefficient of Determination ($R^2$).
6. **Interactive Presentation Application:** Deliver an intuitive, user-friendly interactive web interface capable of profile submission, real-time prediction, and what-if scenario simulations.
""")

st.markdown("---")

# Methodology & System Architecture
st.subheader("🏗️ System Architecture & Workflow")
st.markdown("""
```
┌────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  Kaggle Insurance  │ ──> │ Data Preprocessing  │ ──> │ Multi-Model Training│
│ Dataset (1,338 rows│     │ (ColumnTransformer) │     │ (LR, RF, GBR)       │
└────────────────────┘     └─────────────────────┘     └──────────┬──────────┘
                                                                  │ saves
                                                                  ▼
┌────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  Streamlit Web UI  │ <── │  Prediction & What- │ <── │ Persisted Artifacts │
│ (Interactive App)  │     │  If Scenario Engine │     │ (.joblib & metrics) │
└────────────────────┘     └─────────────────────┘     └─────────────────────┘
```
""")

st.markdown("---")

# References & Attribution
st.subheader("📚 Dataset Attribution & Licenses")
st.markdown("""
* **Dataset Attribution:** Medical Insurance Cost Prediction Dataset, Kaggle (CC0 Public Domain).
  [Link to Kaggle Dataset](https://www.kaggle.com/datasets/rahulvyasm/medical-insurance-cost-prediction)
* **Core Libraries:** Python 3.12, Streamlit, Scikit-Learn, Pandas, NumPy, Plotly, Joblib, Pytest.
""")
