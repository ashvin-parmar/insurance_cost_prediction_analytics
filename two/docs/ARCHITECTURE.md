# System Architecture & Technical Specification

## Project Overview
**Title:** Medical Insurance Cost Prediction & Analytics Dashboard  
**Academic Target:** B.Tech IV Year E&TC (Session 2026–27) · Group No. 11 · IET DAVV  
**Architecture:** 100% Pure Python Machine Learning System  
**Objective:** Predict estimated medical insurance charges in USD using 6 individual demographic and lifestyle factors (`age`, `sex`, `bmi`, `children`, `smoker`, `region`), and deliver an interactive presentation dashboard with multi-model evaluation and what-if lifestyle scenario simulations.

---

## 1. High-Level Architecture

The system is organized into four distinct architectural layers with strict separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit UI Layer                       │
│      Overview · Interactive Predict · Insights · What-If    │
└──────────────────────────────┬──────────────────────────────┘
                               │ calls
┌──────────────────────────────▼──────────────────────────────┐
│                     Application Services                    │
│             PredictionService  ·  ScenarioService           │
└──────────────────────────────┬──────────────────────────────┘
                               │ loads
┌──────────────────────────────▼──────────────────────────────┐
│                    Python ML Pipeline                       │
│                 ColumnTransformer Factory                   │
│   Trained Pipelines: LinearRegression · RF · GradientBoost  │
│          Artifacts: models/*.joblib & metrics.json          │
└─────────────────────────────────────────────────────────────┘
```

### Architectural Principles
1. **Single Authoritative Source of Truth:** UI pages NEVER implement their own prediction formulas or transformations. All inference flows through `PredictionService`.
2. **Offline-First & Local:** Zero live API dependencies or external network requirements at runtime.
3. **Data Leakage Immunity:** All scalers and encoders are fitted solely on training data (80% split with fixed random seed 42) and bundled inside scikit-learn `Pipeline` objects.
4. **Clean Decoupling:** Business logic and data manipulation functions remain independent of Streamlit UI widgets, ensuring comprehensive pytest coverage.

---

## 2. Shared Data Contract: Feature Schema

All inputs adhere to the contract defined in `src/insurance_app/features/schema.py`:

| Feature | Role | Python Type | Permissible Range / Domain | Dataset Observed Range |
|---|---|---|---|---|
| `age` | Input Feature | `int` | 1 – 120 years | 18 – 64 years |
| `sex` | Input Feature | `str` | `{"female", "male"}` | `{"female", "male"}` |
| `bmi` | Input Feature | `float` | 10.0 – 70.0 | 15.96 – 53.13 |
| `children`| Input Feature | `int` | 0 – 10 dependents | 0 – 5 dependents |
| `smoker` | Input Feature | `str` | `{"no", "yes"}` | `{"no", "yes"}` |
| `region` | Input Feature | `str` | `{"northeast", "northwest", "southeast", "southwest"}` | `{"northeast", "northwest", "southeast", "southwest"}` |
| `charges`| Target Variable | `float` (USD $) | > 0 | $1,121.87 – $63,770.43 |

---

## 3. Machine Learning Algorithms & Pipeline Design

### Encapsulated `ColumnTransformer`
```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler() if scale_numeric else "passthrough", ["age", "bmi", "children"]),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), ["sex", "smoker", "region"]),
    ],
    remainder="drop",
)
```

### Evaluated Estimators
1. **Linear Regression:** Baseline parametric estimator with standardized numeric features.
2. **Random Forest Regressor:** Bagging ensemble of 100 decision trees (`n_estimators=100`, `random_state=42`).
3. **Gradient Boosting Regressor:** Sequential boosting ensemble (`n_estimators=100`, `learning_rate=0.1`, `max_depth=3`, `random_state=42`) optimizing squared-error loss.
