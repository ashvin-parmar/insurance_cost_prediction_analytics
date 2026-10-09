"""Unit tests for ML preprocessing pipeline and ColumnTransformer."""

import numpy as np
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression

from insurance_app.ml.preprocessing import build_pipeline, build_preprocessor


@pytest.fixture
def sample_train_df():
    return pd.DataFrame({
        "age": [19, 28, 33, 45, 55],
        "sex": ["female", "male", "male", "female", "male"],
        "bmi": [27.9, 33.0, 22.7, 34.0, 29.5],
        "children": [0, 3, 0, 1, 2],
        "smoker": ["yes", "no", "no", "yes", "no"],
        "region": ["southwest", "southeast", "northwest", "northeast", "southwest"],
    })


def test_build_preprocessor_shape(sample_train_df):
    preprocessor = build_preprocessor(scale_numeric=True)
    transformed = preprocessor.fit_transform(sample_train_df)
    # 3 numeric + 2 sex + 2 smoker + 4 region = 11 one-hot encoded columns
    assert transformed.shape == (5, 11)


def test_build_pipeline_inference(sample_train_df):
    y = np.array([16884.0, 4449.0, 21984.0, 38000.0, 12000.0])
    pipeline = build_pipeline(LinearRegression(), scale_numeric=True)
    pipeline.fit(sample_train_df, y)

    # Inference on new profile
    test_sample = pd.DataFrame([{
        "age": 30,
        "sex": "male",
        "bmi": 26.0,
        "children": 1,
        "smoker": "no",
        "region": "southwest",
    }])
    pred = pipeline.predict(test_sample)
    assert len(pred) == 1
    assert np.isfinite(pred[0])
