"""What-If scenario simulation and profile comparison service."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from insurance_app.features.schema import InsuranceProfile
from insurance_app.services.prediction_service import PredictionService


@dataclass
class ScenarioComparison:
    """Represents the comparative difference between two hypothetical profiles."""

    baseline_profile: InsuranceProfile
    alternative_profile: InsuranceProfile
    baseline_charges: float
    alternative_charges: float
    absolute_delta: float
    percentage_delta: Optional[float]
    changed_features: Dict[str, Dict[str, Any]]
    model_name: str
    disclaimer: str = (
        "Hypothetical Scenario Notice: Differences reflect observational model estimations across profiles, "
        "not medical interventions, causal effects, or guaranteed individual cost changes."
    )

    @property
    def is_increase(self) -> bool:
        return self.absolute_delta > 0

    @property
    def formatted_delta(self) -> str:
        sign = "+" if self.absolute_delta > 0 else ""
        return f"{sign}${self.absolute_delta:,.2f}"

    @property
    def formatted_percentage(self) -> str:
        if self.percentage_delta is None:
            return "N/A"
        sign = "+" if self.percentage_delta > 0 else ""
        return f"{sign}{self.percentage_delta:.1f}%"


class ScenarioService:
    """Computes comparative differences between baseline and alternative profiles."""

    def __init__(self, prediction_service: Optional[PredictionService] = None):
        self.prediction_service = prediction_service or PredictionService()

    def compare_profiles(
        self,
        baseline: InsuranceProfile,
        alternative: InsuranceProfile,
        model_key: Optional[str] = None,
    ) -> ScenarioComparison:
        """Compares baseline and alternative profiles through the same prediction pipeline."""
        res_base = self.prediction_service.predict(baseline, model_key=model_key)
        res_alt = self.prediction_service.predict(alternative, model_key=model_key)

        base_cost = res_base.estimated_charges_usd
        alt_cost = res_alt.estimated_charges_usd
        abs_delta = round(alt_cost - base_cost, 2)

        # Percentage change with zero-division handling
        if base_cost > 0:
            pct_delta = round((abs_delta / base_cost) * 100.0, 2)
        else:
            pct_delta = None

        # Identify changed attributes
        changed: Dict[str, Dict[str, Any]] = {}
        base_dict = baseline.to_dict()
        alt_dict = alternative.to_dict()

        for feat, b_val in base_dict.items():
            a_val = alt_dict[feat]
            if b_val != a_val:
                changed[feat] = {"baseline": b_val, "alternative": a_val}

        return ScenarioComparison(
            baseline_profile=baseline,
            alternative_profile=alternative,
            baseline_charges=base_cost,
            alternative_charges=alt_cost,
            absolute_delta=abs_delta,
            percentage_delta=pct_delta,
            changed_features=changed,
            model_name=res_base.model_name,
        )
