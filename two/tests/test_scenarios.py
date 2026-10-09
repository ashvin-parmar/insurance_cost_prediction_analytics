"""Unit tests for ScenarioService and what-if simulation."""

from insurance_app.features.schema import InsuranceProfile
from insurance_app.services.scenario_service import ScenarioComparison, ScenarioService


class MockPredService:
    def predict(self, profile, model_key=None):
        # Deterministic cost function for unit tests
        # Baseline smoker costs $20,000 more
        base_cost = 5000.0 + (profile.age * 100.0) + (profile.bmi * 50.0)
        if profile.smoker == "yes":
            base_cost += 20000.0
        from insurance_app.services.prediction_service import PredictionResult
        return PredictionResult(
            estimated_charges_usd=round(base_cost, 2),
            model_name="Mock Predictor",
            model_key="mock",
            profile=profile,
            warnings=[],
        )


def test_scenario_comparison_delta():
    base = InsuranceProfile(30, "male", 25.0, 1, "yes", "southwest")
    alt = InsuranceProfile(30, "male", 25.0, 1, "no", "southwest")

    svc = ScenarioService(prediction_service=MockPredService())
    comp = svc.compare_profiles(base, alt)

    assert comp.baseline_charges > comp.alternative_charges
    assert comp.absolute_delta == -20000.0
    assert comp.is_increase is False
    assert "smoker" in comp.changed_features
    assert comp.changed_features["smoker"]["baseline"] == "yes"
    assert comp.changed_features["smoker"]["alternative"] == "no"
    assert comp.percentage_delta is not None
    assert comp.percentage_delta < 0


def test_scenario_comparison_identical_profiles():
    prof = InsuranceProfile(30, "female", 24.0, 0, "no", "northwest")
    svc = ScenarioService(prediction_service=MockPredService())
    comp = svc.compare_profiles(prof, prof)

    assert comp.absolute_delta == 0.0
    assert comp.percentage_delta == 0.0
    assert len(comp.changed_features) == 0
