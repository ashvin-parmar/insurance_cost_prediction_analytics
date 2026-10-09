# Machine Learning Methodology & Experimental Design

## 1. Problem Formulation
Medical insurance cost prediction is framed as a **supervised regression task**:
$$\hat{y} = f(\mathbf{x})$$
where:
- Input feature vector $\mathbf{x} \in \mathbb{R}^d$ contains 6 individual attributes (`age`, `sex`, `bmi`, `children`, `smoker`, `region`).
- Target variable $y \in \mathbb{R}^+$ represents the continuous medical insurance charges billed in USD (`charges`).

---

## 2. Data Preprocessing & Leakage Prevention

To ensure strict academic rigor and prevent **data leakage**:
1. **Reproducible Split:** The dataset is split into **80% Training ($N=1070$)** and **20% Testing ($N=268$)** using a fixed random seed (`random_state=42`).
2. **Encapsulated Preprocessing (`ColumnTransformer`):**
   - **Numerical Features (`age`, `bmi`, `children`):** Standardized using `StandardScaler` ($\mu=0, \sigma=1$) for linear models, or passed through unmodified for tree models.
   - **Categorical Features (`sex`, `smoker`, `region`):** One-hot encoded using `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`.
   - **Strict Isolation:** All scalers and encoders are fitted **strictly on the training set (`X_train`)** only. The test set (`X_test`) is exclusively used for evaluation.

---

## 3. Evaluated Model Architectures

### 1. Multiple Linear Regression (Baseline)
- Serves as the interpretable parametric baseline.
- Linear equation:
  $$\hat{y} = w_0 + \sum_{j=1}^m w_j x_j$$
- Directly comparable in concept to the weights loaded in the project's C CLI application.

### 2. Random Forest Regressor
- Non-parametric ensemble consisting of 100 decorrelated decision trees (`n_estimators=100`, `random_state=42`).
- Aggregates predictions across trees via bootstrap aggregation (bagging) to model nonlinear thresholds and interactions (e.g., interaction between high BMI and smoking status).

### 3. Gradient Boosting Regressor
- Sequential ensemble of shallow decision trees (`n_estimators=100`, `learning_rate=0.1`, `max_depth=3`, `random_state=42`).
- Minimizes squared-error loss iteratively by fitting each new tree to the pseudo-residuals of previous trees.

---

## 4. Evaluation Metrics

Model performance is evaluated on the held-out test set using three standard regression metrics:

1. **Mean Absolute Error (MAE):**
   $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
   Represents average magnitude of prediction errors in actual currency ($ USD).

2. **Root Mean Squared Error (RMSE):**
   $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
   Penalizes larger outliers more heavily than MAE.

3. **Coefficient of Determination ($R^2$):**
   $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
   Quantifies the proportion of target variance explained by the model's features.

---

## 5. Model Selection Criterion
The default production model is chosen objectively based on the **lowest MAE on held-out test data**, ensuring optimal real-world error margins when presented in the interactive dashboard.
