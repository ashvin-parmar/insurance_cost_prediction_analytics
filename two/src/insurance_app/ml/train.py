"""Model training pipeline for Linear Regression, Random Forest, and Gradient Boosting."""

from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Tuple

import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from insurance_app.config import (
    DATA_PATH,
    GRADIENT_BOOSTING_MODEL_PATH,
    LINEAR_REGRESSION_MODEL_PATH,
    METADATA_PATH,
    METRICS_PATH,
    MODELS_DIR,
    RANDOM_FOREST_MODEL_PATH,
    RANDOM_SEED,
    TARGET_COLUMN,
    TEST_SIZE,
)
from insurance_app.data.loader import load_dataset
from insurance_app.features.schema import FEATURE_COLUMNS
from insurance_app.ml.evaluate import evaluate_regression_model
from insurance_app.ml.preprocessing import build_pipeline


def compute_file_hash(path: Path) -> str:
    """Computes SHA-256 fingerprint of the dataset file."""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()[:16]


def train_all_models(
    data_path: Path = DATA_PATH,
    models_dir: Path = MODELS_DIR,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Trains, evaluates, and persists the 3 regression models.

    Pipeline:
    1. Loads dataset from data_path.
    2. Performs reproducible train/test split (80/20, seed 42).
    3. Builds and fits pipelines (fitting scalers & encoders ONLY on X_train).
    4. Evaluates on held-out X_test.
    5. Saves fitted joblib pipelines, metrics.json, and metadata.json.

    Returns:
        (metrics_dict, metadata_dict)
    """
    models_dir.mkdir(parents=True, exist_ok=True)
    df = load_dataset(data_path)

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    # Strictly reproducible 80/20 train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED
    )

    # 1. Model Definitions
    model_configs = {
        "linear_regression": {
            "name": "Linear Regression",
            "model": LinearRegression(),
            "scale_numeric": True,
            "path": LINEAR_REGRESSION_MODEL_PATH,
            "description": "Baseline linear regression with standardized numeric features.",
        },
        "random_forest": {
            "name": "Random Forest Regressor",
            "model": RandomForestRegressor(n_estimators=100, random_state=RANDOM_SEED),
            "scale_numeric": False,
            "path": RANDOM_FOREST_MODEL_PATH,
            "description": "Ensemble of decision trees capturing nonlinear relationships and feature interactions.",
        },
        "gradient_boosting": {
            "name": "Gradient Boosting Regressor",
            "model": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=RANDOM_SEED),
            "scale_numeric": False,
            "path": GRADIENT_BOOSTING_MODEL_PATH,
            "description": "Sequential boosting ensemble minimizing squared error loss.",
        },
    }

    metrics_output: Dict[str, Any] = {}
    detailed_evaluations: Dict[str, Any] = {}

    for key, cfg in model_configs.items():
        pipeline = build_pipeline(cfg["model"], scale_numeric=cfg["scale_numeric"])
        pipeline.fit(X_train, y_train)

        # Evaluate on held-out test data
        eval_result = evaluate_regression_model(pipeline, X_test, y_test)
        metrics_output[key] = {
            "name": cfg["name"],
            "metrics": eval_result["metrics"],
            "feature_importance": eval_result["feature_importance"],
        }
        detailed_evaluations[key] = eval_result

        # Persist fitted pipeline
        joblib.dump(pipeline, cfg["path"])

    # Determine default model based on lowest test MAE
    best_model_key = min(metrics_output, key=lambda k: metrics_output[k]["metrics"]["mae"])

    # Construct Metadata
    metadata = {
        "project": "Medical Insurance Cost Prediction",
        "training_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "random_seed": RANDOM_SEED,
        "test_size": TEST_SIZE,
        "total_samples": len(df),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "dataset_hash": compute_file_hash(data_path),
        "features": FEATURE_COLUMNS,
        "target": TARGET_COLUMN,
        "target_units": "USD ($)",
        "best_model_key": best_model_key,
        "best_model_name": model_configs[best_model_key]["name"],
        "models": {
            k: {
                "name": cfg["name"],
                "description": cfg["description"],
                "file": cfg["path"].name,
            }
            for k, cfg in model_configs.items()
        },
    }

    # Save metrics and metadata JSON files
    with open(METRICS_PATH, "w", encoding="utf-8") as f:
        json.dump(metrics_output, f, indent=2)

    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    # Also save detailed residual & prediction points for dashboard charting
    eval_cache_path = models_dir / "evaluation_cache.json"
    with open(eval_cache_path, "w", encoding="utf-8") as f:
        json.dump(detailed_evaluations, f, indent=2)

    return metrics_output, metadata
