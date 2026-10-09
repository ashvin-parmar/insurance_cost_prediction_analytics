# Medical Insurance Cost Prediction & Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.65%2B-FF4B4B)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9%2B-orange)](https://scikit-learn.org/)
[![Tests](https://img.shields.io/badge/pytest-21%20passed-brightgreen)](https://pytest.org/)

> **Academic Final-Year Project Deliverable**  
> **Institution:** Institute of Engineering & Technology (IET), Devi Ahilya Vishwavidyalaya (DAVV), Indore  
> **Department:** Electronics & Telecommunication Engineering (B.Tech IV Year E&TC, Session 2026–27)  
> **Group No.:** 11

---

## 📌 Project Overview
This project delivers a **100% pure Python** machine-learning regression system and interactive presentation dashboard to estimate annual **medical insurance charges ($ USD)** from individual demographic and lifestyle attributes (`age`, `sex`, `bmi`, `children`, `smoker`, `region`).

The solution incorporates:
1. **Interactive Presentation Dashboard (Streamlit & Plotly):** Visual exploratory data analysis, real-time prediction forms, model evaluation diagnostics, and what-if lifestyle scenario simulations.
2. **Multi-Model Regression Benchmarking:** Comparative training and evaluation of **Multiple Linear Regression**, **Random Forest Regressor**, and **Gradient Boosting Regressor** using MAE, RMSE, and $R^2$ scores.
3. **Strict Data Leakage Protection:** Encapsulated Scikit-Learn `ColumnTransformer` pipelines fitted strictly on training data (80/20 split, seed 42).
4. **Comprehensive Test Suite:** 21 automated pytest unit and integration tests passing with 100% success rate.

---

## 🚀 Quick Start & Installation Guide

### 1. Installation by Operating System

#### 🐧 Linux (Ubuntu / Debian / Fedora)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

#### 🪟 Windows (PowerShell or Command Prompt)
```powershell
# In PowerShell:
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
# (Or in CMD: .\.venv\Scripts\activate.bat)
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

#### 🍎 macOS (Apple Silicon / Intel)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

---

### 2. Check Environment Diagnostics
```bash
python scripts/check_environment.py
```

### 3. Train Machine Learning Models
```bash
python scripts/train_models.py
```

### 4. Run Automated Tests
```bash
pytest -v
```

### 5. Launch the Streamlit Dashboard
```bash
python -m streamlit run app.py
```
Open your browser at: `http://localhost:8501`

---

## 📂 Repository Structure
```
medical_insurance_cost_prediction_and_analytics/
├── app.py                      # Streamlit main entry point
├── pages/                      # Multi-page dashboard modules
│   ├── 1_Overview.py           # Module A: Exploratory Data Analysis & Quality Audit
│   ├── 2_Predict.py            # Module B: Interactive Single-Profile Prediction Form
│   ├── 3_Model_Insights.py     # Module C: Multi-Model Evaluation & Residual Plots
│   ├── 4_What_If.py            # Module D: Lifestyle What-If Scenario Simulator
│   ├── 5_Docs.py               # Module E: Project Documentation & Tool Operations
│   └── 6_About.py              # Module F: Academic Proforma & Project Attribution
├── src/insurance_app/          # Core modular application package
│   ├── config.py               # Cross-platform path management (pathlib)
│   ├── features/schema.py      # Feature contract, dataclasses, and boundary rules
│   ├── data/                   # Data loader and comprehensive validation engine
│   ├── ml/                     # ML pipelines, preprocessing, training, and registry
│   ├── analytics/              # Summary statistics and Plotly chart builders
│   ├── services/               # Prediction and Scenario simulation services
│   └── ui/                     # UI styling and reusable presentation components
├── data/                       # Kaggle Dataset storage (insurance.csv)
├── models/                     # Saved joblib pipelines, metadata, and evaluation metrics
├── scripts/                    # CLI scripts (train_models.py, check_environment.py)
├── tests/                      # Pytest automated test suite (21 passed tests)
├── docs/                       # Complete academic project deliverables
│   ├── PROJECT_REPORT.md       # Final college project submission report
│   ├── VIVA_QUESTIONS.md       # Viva voce examination preparation guide
│   ├── ARCHITECTURE.md         # Technical architecture specification
│   ├── DATASET.md              # Dataset specification and dictionary
│   ├── ML_METHODOLOGY.md       # Machine learning methodology
│   ├── USER_GUIDE.md           # User manual and navigation guide
│   └── TESTING.md              # Test strategy and test inventory
├── planning/                   # Project planning guidelines and checklists
│   ├── python_implementation_guidelines.md
│   ├── implementation_plan.md
│   └── checklist.md
└── requirements.txt            # Pinned dependencies
```

---

## 📊 Summary of Model Performance (Held-Out Test Set: 20%, Seed 42)
| Algorithm | MAE ($ USD) | RMSE ($ USD) | $R^2$ Score | Rank |
|---|---|---|---|---|
| **Gradient Boosting Regressor** | **$2,401.61** | **$4,325.64** | **0.8795** | 🥇 Best Model |
| Random Forest Regressor | $2,552.04 | $4,590.28 | 0.8643 | 🥈 Second |
| Linear Regression (Baseline) | $4,181.19 | $5,796.28 | 0.7836 | 🥉 Baseline |

---

## 📜 Academic Attribution & Disclaimer
- **Dataset:** Medical Insurance Cost Prediction dataset from Kaggle (CC0 Public Domain).
- **Disclaimer:** All outputs generated by this system are statistical approximations based on historical observational data. They do not constitute certified insurance quotations, financial guarantees, or clinical risk assessments.
