# Viva Voce Examination Preparation: Medical Insurance Cost Prediction

**B.Tech IV Year E&TC · Session 2026–27 · Group No. 11 · IET DAVV**

---

### Q1: Why is this problem formulated as regression rather than classification?
**Answer:** The prediction target (`charges`) is a continuous numerical variable measured in US Dollars ($ USD) ranging from ~$1,121 to ~$63,770, rather than a discrete categorical label (e.g., high/low risk). Therefore, it requires supervised regression algorithms capable of predicting real continuous values.

---

### Q2: What is Data Leakage and how did you prevent it in your project?
**Answer:** Data leakage occurs when information from outside the training dataset (specifically from the test set) is inadvertently used to train the model or fit preprocessing transformations. To prevent data leakage:
1. We split the raw dataset into 80% train and 20% test *before* any transformations.
2. All scalers (`StandardScaler`) and encoders (`OneHotEncoder`) were fitted *strictly on `X_train`* using scikit-learn `Pipeline` and `ColumnTransformer`.
3. The test set (`X_test`) was strictly reserved for the final unbiased evaluation.

---

### Q3: Why did you use One-Hot Encoding instead of Label Encoding for categorical features?
**Answer:** Features like `region` (`northeast`, `northwest`, `southeast`, `southwest`) and `sex` have no intrinsic mathematical order. Label encoding (e.g., assigning 1, 2, 3, 4) would falsely imply that `southwest (4)` is four times greater than `northeast (1)`. One-Hot Encoding creates binary indicator columns, avoiding artificial ordinal relationships that could distort linear regression models.

---

### Q4: Why did Gradient Boosting / Random Forest outperform Linear Regression?
**Answer:** Linear Regression assumes an additive linear relationship:
$$\hat{y} = w_0 + w_1 x_1 + \dots + w_m x_m$$
However, healthcare costs exhibit severe non-linear interactions. Specifically, there is a strong synergistic interaction between high BMI ($\ge 30$) and smoking status—smokers with obesity experience exponential cost increases that a simple linear sum cannot capture. Decision tree ensembles naturally split on feature interactions, allowing them to achieve significantly higher $R^2$ scores (~0.88 vs ~0.78).

---

### Q5: What is the mathematical difference between MAE and RMSE?
**Answer:**
- **MAE (Mean Absolute Error):** $\frac{1}{n}\sum |y_i - \hat{y}_i|$. It measures the average magnitude of errors with linear weight.
- **RMSE (Root Mean Squared Error):** $\sqrt{\frac{1}{n}\sum (y_i - \hat{y}_i)^2}$. Because errors are squared before averaging, RMSE penalizes large outlier errors much more severely than MAE.
In medical cost prediction, large unexpected claims cause RMSE to be notably higher than MAE.

---

### Q6: What does an $R^2$ score represent? Can it be negative?
**Answer:** The Coefficient of Determination ($R^2$) represents the proportion of variance in the target variable explained by the model:
$$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$$
An $R^2$ of 0.88 means the model explains ~88% of the variance in charges. Yes, on an unseen test set, $R^2$ can be negative if the model's predictions perform worse than simply predicting the historical mean of the target.

---

### Q7: Why does the application include a "non-causal" disclaimer?
**Answer:** The Kaggle dataset is observational, not derived from a randomized controlled clinical trial. While the model indicates that smokers have higher predicted charges, this reflects statistical correlation. Presenting the predictions as guaranteed financial savings or causal medical intervention guarantees would be scientifically invalid.
