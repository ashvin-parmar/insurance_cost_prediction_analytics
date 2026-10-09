"""Model artifact registry and safe loader."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import joblib

from insurance_app.config import (
    GRADIENT_BOOSTING_MODEL_PATH,
    LINEAR_REGRESSION_MODEL_PATH,
    METADATA_PATH,
    METRICS_PATH,
    MODELS_DIR,
    RANDOM_FOREST_MODEL_PATH,
)


class ModelRegistry:
    """Manages loading and querying of persisted machine learning models and metadata."""

    MODEL_PATHS = {
        "linear_regression": LINEAR_REGRESSION_MODEL_PATH,
        "random_forest": RANDOM_FOREST_MODEL_PATH,
        "gradient_boosting": GRADIENT_BOOSTING_MODEL_PATH,
    }

    def __init__(self, models_dir: Path = MODELS_DIR):
        self.models_dir = models_dir
        self._cache: Dict[str, Any] = {}
        self._metrics: Optional[Dict[str, Any]] = None
        self._metadata: Optional[Dict[str, Any]] = None

    def are_models_available(self) -> bool:
        """Checks if all required model artifacts and metrics exist."""
        return (
            METRICS_PATH.exists()
            and METADATA_PATH.exists()
            and all(p.exists() for p in self.MODEL_PATHS.values())
        )

    def load_metrics(self) -> Dict[str, Any]:
        """Loads evaluation metrics dictionary."""
        if self._metrics is not None:
            return self._metrics
        if not METRICS_PATH.exists():
            raise FileNotFoundError(
                f"Metrics file not found at '{METRICS_PATH}'. Run 'python scripts/train_models.py' first."
            )
        with open(METRICS_PATH, "r", encoding="utf-8") as f:
            self._metrics = json.load(f)
        return self._metrics

    def load_metadata(self) -> Dict[str, Any]:
        """Loads training metadata dictionary."""
        if self._metadata is not None:
            return self._metadata
        if not METADATA_PATH.exists():
            raise FileNotFoundError(
                f"Metadata file not found at '{METADATA_PATH}'. Run 'python scripts/train_models.py' first."
            )
        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            self._metadata = json.load(f)
        return self._metadata

    def load_model(self, model_key: str = "gradient_boosting") -> Any:
        """Loads a persisted scikit-learn pipeline by key."""
        if model_key not in self.MODEL_PATHS:
            raise KeyError(f"Unknown model key '{model_key}'. Available: {list(self.MODEL_PATHS.keys())}")

        if model_key in self._cache:
            return self._cache[model_key]

        model_path = self.MODEL_PATHS[model_key]
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model artifact not found at '{model_path}'. "
                f"Please train the models by running 'python scripts/train_models.py'."
            )

        model = joblib.load(model_path)
        self._cache[model_key] = model
        return model

    def load_evaluation_cache(self) -> Dict[str, Any]:
        """Loads test-set predictions and residuals for charting."""
        cache_path = self.models_dir / "evaluation_cache.json"
        if not cache_path.exists():
            return {}
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_default_model_key(self) -> str:
        """Returns the key of the best performing model based on metadata."""
        try:
            metadata = self.load_metadata()
            return metadata.get("best_model_key", "gradient_boosting")
        except Exception:
            return "gradient_boosting"


_global_registry = ModelRegistry()


def load_active_model(model_key: Optional[str] = None) -> Tuple[Any, str, Dict[str, Any]]:
    """Helper to retrieve a model, its display name, and its metrics."""
    registry = _global_registry
    chosen_key = model_key if model_key else registry.get_default_model_key()
    model = registry.load_model(chosen_key)
    metrics = registry.load_metrics().get(chosen_key, {})
    name = metrics.get("name", chosen_key.replace("_", " ").title())
    return model, name, metrics
