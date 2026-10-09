"""Authoritative prediction service for the Python ML pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from insurance_app.features.schema import InsuranceProfile
from insurance_app.ml.registry import ModelRegistry


@dataclass
class PredictionResult:
    """Represents the standardized output of a prediction request."""

    estimated_charges_usd: float
    model_name: str
    model_key: str
    profile: InsuranceProfile
    warnings: List[str]
    disclaimer: str = (
        "Notice: This prediction is a machine-learning statistical estimate based on "
        "historical observational data, not a certified actuarial insurance quote or medical risk diagnosis."
    )

    @property
    def formatted_charges(self) -> str:
        """Returns currency formatted as USD ($xx,xxx.xx)."""
        return f"${self.estimated_charges_usd:,.2f}"


class PredictionService:
    """Encapsulates the prediction pipeline, model loading, and business rules."""

    def __init__(self, registry: Optional[ModelRegistry] = None):
        self.registry = registry or ModelRegistry()

    def predict(
        self,
        profile: InsuranceProfile,
        model_key: Optional[str] = None,
        warnings: Optional[List[str]] = None,
    ) -> PredictionResult:
        """Executes prediction using the specified or default trained model pipeline.

        Args:
            profile: Validated InsuranceProfile.
            model_key: Specific model identifier or None for default.
            warnings: Any input boundary warnings to pass through.

        Returns:
            PredictionResult with estimated charges and metadata.
        """
        active_key = model_key or self.registry.get_default_model_key()
        pipeline = self.registry.load_model(active_key)

        # Convert profile to DataFrame conforming to feature schema
        input_df = profile.to_dataframe()

        # Run inference through fitted scikit-learn pipeline
        predicted_val = float(pipeline.predict(input_df)[0])

        # Floor charges at 0 (insurance charges cannot be negative)
        clamped_val = max(0.0, round(predicted_val, 2))

        # Model display name
        try:
            metrics = self.registry.load_metrics().get(active_key, {})
            display_name = metrics.get("name", active_key.replace("_", " ").title())
        except Exception:
            display_name = active_key.replace("_", " ").title()

        return PredictionResult(
            estimated_charges_usd=clamped_val,
            model_name=display_name,
            model_key=active_key,
            profile=profile,
            warnings=warnings or [],
        )
