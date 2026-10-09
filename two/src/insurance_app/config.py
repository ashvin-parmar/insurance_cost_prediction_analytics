"""Central configuration management for the insurance application.

Uses pathlib for cross-platform path resolution across Linux, Windows, and macOS.
"""

from __future__ import annotations

import os
from pathlib import Path

# Base project root (two levels up from this file: src/insurance_app/ -> repository root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Data Paths
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "insurance.csv"
DATA_PATH = Path(os.getenv("INSURANCE_DATA_PATH", str(DEFAULT_DATA_PATH)))

# Model Artifacts
MODELS_DIR = PROJECT_ROOT / "models"
METRICS_PATH = MODELS_DIR / "metrics.json"
METADATA_PATH = MODELS_DIR / "metadata.json"
LINEAR_REGRESSION_MODEL_PATH = MODELS_DIR / "linear_regression.joblib"
RANDOM_FOREST_MODEL_PATH = MODELS_DIR / "random_forest.joblib"
GRADIENT_BOOSTING_MODEL_PATH = MODELS_DIR / "gradient_boosting.joblib"

# ML Pipeline Reproducibility Settings
RANDOM_SEED = 42
TEST_SIZE = 0.20
TARGET_COLUMN = "charges"
