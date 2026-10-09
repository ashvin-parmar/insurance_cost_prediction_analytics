"""Centralized preprocessing pipeline factory using scikit-learn ColumnTransformer."""

from __future__ import annotations

from typing import Any

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from insurance_app.features.schema import CATEGORICAL_FEATURES, NUMERIC_FEATURES


def build_preprocessor(scale_numeric: bool = True) -> ColumnTransformer:
    """Builds a scikit-learn ColumnTransformer for insurance feature preprocessing.

    Args:
        scale_numeric: If True, applies StandardScaler to numerical columns (recommended for Linear Regression).
                       If False, passes numerical features through unchanged (standard for tree ensembles).

    Returns:
        ColumnTransformer: Preprocessing transformer ready to fit on training data.
    """
    numeric_transformer = StandardScaler() if scale_numeric else "passthrough"

    categorical_transformer = OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False,
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, NUMERIC_FEATURES),
            ("cat", categorical_transformer, CATEGORICAL_FEATURES),
        ],
        remainder="drop",
    )
    return preprocessor


def build_pipeline(model: Any, scale_numeric: bool = True) -> Pipeline:
    """Combines preprocessing and an estimator into an integrated scikit-learn Pipeline.

    Encapsulating preprocessing prevents data leakage during training and guarantees
    identical transformations during real-time user inference.
    """
    preprocessor = build_preprocessor(scale_numeric=scale_numeric)
    return Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", model),
    ])
