"""Unit tests for dataset loading, schema validation, and statistical computations."""

import numpy as np
import pandas as pd
import pytest

from insurance_app.analytics.statistics import (
    compute_category_breakdowns,
    compute_correlation_matrix,
    compute_group_charges_summary,
    compute_numeric_summary,
)
from insurance_app.data.loader import load_dataset
from insurance_app.data.validation import validate_dataset


@pytest.fixture
def synthetic_clean_df():
    """Provides a synthetic 5-row valid dataset."""
    return pd.DataFrame({
        "age": [20, 30, 40, 50, 60],
        "sex": ["female", "male", "female", "male", "female"],
        "bmi": [21.5, 26.0, 30.2, 35.1, 28.4],
        "children": [0, 1, 2, 0, 3],
        "smoker": ["no", "no", "yes", "no", "yes"],
        "region": ["southwest", "southeast", "northwest", "northeast", "southwest"],
        "charges": [2000.0, 4500.0, 22000.0, 9000.0, 31000.0],
    })


@pytest.fixture
def synthetic_invalid_df():
    """Provides a synthetic dataset with intentional flaws."""
    return pd.DataFrame({
        "age": [25, -10],  # negative age
        "sex": ["male", "unknown"],  # invalid category
        "bmi": [25.0, np.nan],  # NaN value
        "children": [0, 1],
        "smoker": ["no", "yes"],
        "region": ["southwest", "midwest"],  # invalid region
        "charges": [3000.0, 4000.0],
    })


def test_validate_clean_dataset(synthetic_clean_df):
    report = validate_dataset(synthetic_clean_df)
    assert report.is_valid is True
    assert report.total_rows == 5
    assert report.total_columns == 7
    assert report.duplicate_rows_count == 0
    assert not report.has_missing_values
    assert len(report.errors) == 0


def test_validate_invalid_dataset(synthetic_invalid_df):
    report = validate_dataset(synthetic_invalid_df)
    assert report.is_valid is False
    assert len(report.errors) > 0
    # Check that negative age was caught
    assert any("negative" in err for err in report.errors)
    # Check that invalid categories were caught
    assert "sex" in report.invalid_categories
    assert "region" in report.invalid_categories
    # Check missing value was caught
    assert report.missing_values_by_column["bmi"] == 1


def test_duplicate_detection(synthetic_clean_df):
    duplicated_df = pd.concat([synthetic_clean_df, synthetic_clean_df.iloc[[0]]], ignore_index=True)
    report = validate_dataset(duplicated_df)
    assert report.duplicate_rows_count == 1
    assert any("duplicate" in w for w in report.warnings)


def test_compute_numeric_summary(synthetic_clean_df):
    summary = compute_numeric_summary(synthetic_clean_df)
    assert "mean" in summary.columns
    assert "median" in summary.columns
    assert "age" in summary.index
    assert "charges" in summary.index
    assert summary.loc["age", "mean"] == 40.0


def test_compute_category_breakdowns(synthetic_clean_df):
    breakdowns = compute_category_breakdowns(synthetic_clean_df)
    assert "sex" in breakdowns
    assert "smoker" in breakdowns
    assert "region" in breakdowns
    assert breakdowns["smoker"].loc["yes", "Count"] == 2


def test_compute_group_charges_summary(synthetic_clean_df):
    grouped = compute_group_charges_summary(synthetic_clean_df, "smoker")
    assert "mean" in grouped.columns
    assert "median" in grouped.columns
    # Smoker charges should be higher
    assert grouped.loc["yes", "mean"] > grouped.loc["no", "mean"]


def test_compute_correlation_matrix(synthetic_clean_df):
    corr = compute_correlation_matrix(synthetic_clean_df)
    assert corr.shape == (4, 4)
    assert corr.loc["age", "age"] == 1.0


def test_load_real_dataset():
    """Verifies that the actual local data/insurance.csv loads correctly."""
    df = load_dataset()
    assert len(df) == 1338
    report = validate_dataset(df)
    assert report.is_valid is True
