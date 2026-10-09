"""Unit tests for PredictionService and result formatting."""

import numpy as np
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression

from insurance_app.features.schema import InsuranceProfile
from insurance_app.ml.preprocessing import build_pipeline
from insurance_app.services.prediction_service import PredictionResult, PredictionService


class MockRegistry:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def get_default_model_key(self):
        return "linear_regression"

    def load_model(self, model_key):
        return self.pipeline

    def load_metrics(self):
        return {"linear_regression": {"name": "Mock Linear Regression"}}


def test_prediction_result_formatting():
    profile = InsuranceProfile(30, "male", 25.0, 1, "no", "southwest")
    result = PredictionResult(
        estimated_charges_usd=4523.50,
        model_name="Linear Regression",
        model_key="linear_regression",
        profile=profile,
        warnings=[],
    )
    assert result.formatted_charges == "$4,523.50"
    assert "Disclaimer" in result.disclaimer or "Notice" in result.disclaimer


def test_prediction_service_execution(sample_valid_profile):
    # Fit a small pipeline for mock testing
    df = pd.DataFrame([{
        "age": 30, "sex": "male", "bmi": 25.0, "children": 1, "smoker": "no", "region": "southwest"
    }])
    y = np.array([4500.0])
    pipeline = build_pipeline(LinearRegression())
    pipeline.fit(df, y)

    mock_reg = MockRegistry(pipeline)
    service = PredictionService(registry=mock_reg)

    res = service.predict(sample_valid_profile)
    assert res.estimated_charges_usd > 0
    assert res.model_name == "Mock Linear Regression"
    assert res.profile == sample_valid_profile
