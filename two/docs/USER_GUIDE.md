# User Guide: Medical Insurance Cost Prediction Dashboard

## 1. Overview
The **Medical Insurance Cost Prediction & Analytics Dashboard** provides an interactive web interface for exploring healthcare cost data, calculating individualized predictions, benchmarking regression models, and simulating lifestyle scenarios.

---

## 2. Navigating the Dashboard

Use the **left-hand sidebar** to switch between modules:

### Module A: Overview & Data Analytics (`1_Overview.py`)
- **Key Metrics:** View total samples (1,338), missing values (0), and summary statistics.
- **Visualizations:**
  - Distribution of charges with median indicator.
  - Distribution histograms for Age and BMI.
  - Grouped box plots comparing charges across smoking status, region, and sex.
  - Scatter plots with interactive filters.
  - Annotated Pearson correlation matrix.

### Module B: Interactive Prediction (`2_Predict.py`)
- **Step 1:** Adjust sliders and dropdowns for Age (1–120), Sex, BMI, Children (0–10), Smoking status, and Region.
- **Step 2:** Choose a predictive algorithm (Gradient Boosting, Random Forest, or Linear Regression).
- **Step 3:** Click **Predict Insurance Charges** to view the estimated annual bill in USD, profile confirmation summary, and health indicator notes.

### Module C: Model Insights & Comparisons (`3_Model_Insights.py`)
- Inspect the comparative performance table displaying MAE, RMSE, and $R^2$ scores across all models.
- Review comparative bar charts and diagnostic scatter plots (Actual vs. Predicted and Residual analysis).
- Inspect relative feature importance rankings.

### Module D: What-If Comparison Simulator (`4_What_If.py`)
- Compare a **Baseline Profile** against an **Alternative Profile** side-by-side.
- Use one-click presets:
  - *Stop Smoking Scenario*
  - *Reduce BMI to Normal*
  - *10 Years Older*
- Inspect absolute dollar differences ($\Delta$) and relative percentage changes ($\% \Delta$).

### Module E: About & Proforma (`5_About.py`)
- Review academic project objectives, departmental information, methodology, and citations.
