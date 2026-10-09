# Project Report: Medical Insurance Cost Prediction Using Machine Learning

**Institute of Engineering & Technology, Devi Ahilya Vishwavidyalaya (DAVV), Indore**  
**Department of Electronics & Telecommunication Engineering**  
**B.Tech IV Year E&TC — Session 2026–27 | Group No. 11**

---

## Abstract
Medical insurance plays a critical role in mitigating the catastrophic financial burdens associated with unexpected healthcare and hospitalization treatments. The cost of medical insurance premiums varies substantially among individuals based on demographic, lifestyle, and physiological parameters such as age, body mass index (BMI), smoking status, dependent count, and geographic region. Estimating insurance costs accurately is essential for financial planning, risk analysis, and automated decision-support systems.

This project presents an end-to-end, 100% pure Python machine learning system and interactive analytics dashboard capable of predicting individualized medical insurance charges. Formulated as a supervised regression task, historical data comprising 1,338 records from the Medical Insurance Cost dataset is audited, cleaned, and transformed via encapsulated scikit-learn pipelines. Three distinct regression algorithms—Multiple Linear Regression, Random Forest Regressor, and Gradient Boosting Regressor—are trained and compared using an 80/20 train-test split with fixed random seeds. Performance is evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the Coefficient of Determination ($R^2$).

To make the machine learning model accessible, a cross-platform interactive presentation dashboard is developed using Streamlit and Plotly. The application provides exploratory data analytics, real-time cost estimation, and what-if lifestyle scenario simulations.

---

## 1. Introduction & Background
Healthcare expenditure forecasting is an important domain of predictive analytics. Actuarial pricing models have historically relied on manual underwriting rules, demographic lookup tables, and aggregate risk pooling. However, non-linear interactions—such as the compounded financial impact of elevated BMI combined with regular tobacco smoking—are often difficult to capture through static linear formulas.

Machine learning enables automated, data-driven regression modeling where continuous financial outcomes can be predicted directly from structured personal attributes. This project bridges data science with practical software engineering by deploying trained pipelines into a modern web-based presentation dashboard.

---

## 2. Problem Statement
The primary objective of this project is to develop a reliable predictive system that accepts individual demographic and lifestyle attributes (`age`, `sex`, `bmi`, `children`, `smoker`, `region`) and outputs an accurate estimate of annual medical insurance charges in USD.

Key challenges include:
1. Handling mixed numeric and categorical data while preventing target leakage.
2. Training multiple regression algorithms and benchmarking their trade-offs.
3. Building an intuitive graphical interface suitable for academic presentation.
4. Ensuring complete reproducibility and automated test verification.

---

## 3. Objectives
As specified in Academic Proforma-I:
1. **Predictive System:** Develop a machine-learning-based system for estimating the approximate medical insurance cost of an individual.
2. **Feature Relationship Identification:** Identify significant features and their statistical relationships with predicted charges.
3. **Categorical Transformation:** Apply robust one-hot encoding without data leakage.
4. **Multi-Model Comparison:** Train and benchmark Multiple Linear Regression, Random Forest, and Gradient Boosting Regressors.
5. **Quantitative Evaluation:** Measure performance using MAE, MSE, RMSE, and $R^2$ scores.
6. **Interactive Presentation Interface:** Deliver a full-featured dashboard supporting EDA, real-time prediction, and what-if scenario simulations.

---

## 4. System Architecture & Methodology

### 4.1 Data Pipeline & Preprocessing
The dataset contains 1,338 records and 7 attributes.
- **Split Strategy:** 80% Training ($N=1,070$), 20% Held-Out Testing ($N=268$), `random_state=42`.
- **Numerical Pipeline:** Standard scaling for linear models; pass-through for tree ensembles.
- **Categorical Pipeline:** `OneHotEncoder(handle_unknown='ignore', sparse_output=False)` for `sex`, `smoker`, and `region`.
- **Leakage Prevention:** Transformers are fitted strictly on `X_train` and persisted inside scikit-learn `Pipeline` objects.

### 4.2 Evaluated Algorithms
1. **Multiple Linear Regression (Baseline):** Parametric baseline evaluating linear relationships.
2. **Random Forest Regressor:** Bagging ensemble of 100 decision trees capturing non-linear thresholds.
3. **Gradient Boosting Regressor:** Sequential boosting ensemble optimizing squared-error loss.

---

## 5. Experimental Results & Discussion

### 5.1 Model Performance Summary (Held-Out Test Set)
| Model | MAE ($ USD) | RMSE ($ USD) | $R^2$ Score | Rank |
|---|---|---|---|---|
| **Gradient Boosting Regressor** | **$2,401.61** | **$4,325.64** | **0.8795** | 🥇 Best Model |
| Random Forest Regressor | $2,552.04 | $4,590.28 | 0.8643 | 🥈 Second |
| Linear Regression (Baseline) | $4,181.19 | $5,796.28 | 0.7836 | 🥉 Baseline |

### 5.2 Key Analytical Insights
- **Smoking Status:** Smoking is by far the single most dominant factor influencing medical charges. Smokers exhibit average charges approximately 3.8 to 4 times higher than non-smokers.
- **BMI Threshold Interaction:** BMI exhibits a non-linear threshold effect: individuals with $\text{BMI} \ge 30$ who also smoke experience exponential increases in predicted charges (averaging >$35,000$).
- **Age:** Demonstrates a consistent positive linear slope with medical charges across all demographic subgroups.

---

## 6. Software Implementation
The software consists of:
- **`app.py`:** Dashboard entry point with KPI metrics and navigation.
- **`pages/1_Overview.py`:** Exploratory data analytics with interactive Plotly visualizations.
- **`pages/2_Predict.py`:** Profile input form and real-time cost estimation.
- **`pages/3_Model_Insights.py`:** Metric comparisons, actual vs. predicted plots, and residual diagnostics.
- **`pages/4_What_If.py`:** Side-by-side scenario simulator with absolute and percentage delta metrics.
- **`pages/5_About.py`:** Academic proforma details and documentation.

---

## 7. Conclusion & Future Enhancements
The project successfully achieves all six objectives of Academic Proforma-I. The combination of multi-model regression benchmarking, rigorous test suites, and an interactive Streamlit UI delivers a comprehensive final-year engineering deliverable.

### Future Work
- Integration of advanced explainability tools such as SHAP (SHapley Additive exPlanations).
- Cloud deployment on Streamlit Community Cloud or Docker containers.
