"""Regression evaluation metrics and model explanation extraction."""

from __future__ import annotations

import math
from typing import Any, Dict, List

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Calculates regression performance metrics.

    Metrics:
    - MAE: Mean Absolute Error in USD ($)
    - RMSE: Root Mean Squared Error in USD ($)
    - R²: Coefficient of Determination

    Returns dict with rounded floating-point values.
    """
    y_true_arr = np.asarray(y_true, dtype=float)
    y_pred_arr = np.asarray(y_pred, dtype=float)

    mae = float(mean_absolute_error(y_true_arr, y_pred_arr))
    mse = float(mean_squared_error(y_true_arr, y_pred_arr))
    rmse = float(math.sqrt(mse))
    r2 = float(r2_score(y_true_arr, y_pred_arr))

    return {
        "mae": round(mae, 2),
        "rmse": round(rmse, 2),
        "r2": round(r2, 4),
    }


def get_feature_names_from_preprocessor(preprocessor: Any) -> List[str]:
    """Extracts output feature names from a fitted ColumnTransformer."""
    try:
        return list(preprocessor.get_feature_names_out())
    except Exception:
        # Fallback if scikit-learn version or named output fails
        return [
            "num__age", "num__bmi", "num__children",
            "cat__sex_female", "cat__sex_male",
            "cat__smoker_no", "cat__smoker_yes",
            "cat__region_northeast", "cat__region_northwest",
            "cat__region_southeast", "cat__region_southwest"
        ]


def extract_feature_importance(pipeline: Any) -> Dict[str, float]:
    """Extracts feature importance or coefficients depending on model architecture."""
    preprocessor = pipeline.named_steps["preprocessor"]
    regressor = pipeline.named_steps["regressor"]
    feature_names = get_feature_names_from_preprocessor(preprocessor)

    # Clean feature names for clean UI display (e.g. cat__smoker_yes -> smoker: yes)
    clean_names = []
    for f in feature_names:
        clean = f.replace("num__", "").replace("cat__", "").replace("_", ": ")
        clean_names.append(clean)

    importance_dict: Dict[str, float] = {}

    if hasattr(regressor, "coef_"):
        # Linear Regression coefficients
        coefs = regressor.coef_
        for name, coef in zip(clean_names, coefs):
            importance_dict[name] = round(float(coef), 2)
    elif hasattr(regressor, "feature_importances_"):
        # Tree ensembles feature importances (normalized 0 to 1)
        importances = regressor.feature_importances_
        for name, imp in zip(clean_names, importances):
            importance_dict[name] = round(float(imp), 4)

    return importance_dict


def evaluate_regression_model(
    pipeline: Any,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Dict[str, Any]:
    """Evaluates a fitted pipeline on held-out test data.

    Returns dict containing:
    - metrics: MAE, RMSE, R²
    - y_true: actual target values list
    - y_pred: predicted values list
    - residuals: y_true - y_pred list
    - feature_importance: coefficients or tree importance
    """
    preds = pipeline.predict(X_test)
    metrics = compute_metrics(y_test.values, preds)
    residuals = (y_test.values - preds).tolist()
    importance = extract_feature_importance(pipeline)

    return {
        "metrics": metrics,
        "y_true": [round(float(v), 2) for v in y_test.values],
        "y_pred": [round(float(v), 2) for v in preds],
        "residuals": [round(float(v), 2) for v in residuals],
        "feature_importance": importance,
    }
