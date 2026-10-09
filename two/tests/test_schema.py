"""Unit tests for feature schema and validation rules."""

import pytest
from insurance_app.features.schema import (
    InsuranceProfile,
    validate_profile,
)


def test_valid_profile_creation(sample_valid_profile):
    assert sample_valid_profile.age == 30
    assert sample_valid_profile.sex == "male"
    assert sample_valid_profile.bmi == 25.5
    assert sample_valid_profile.children == 1
    assert sample_valid_profile.smoker == "no"
    assert sample_valid_profile.region == "southwest"

    df = sample_valid_profile.to_dataframe()
    assert df.shape == (1, 6)
    assert list(df.columns) == ["age", "bmi", "children", "sex", "smoker", "region"]


def test_validate_profile_success():
    profile, warnings = validate_profile(
        age=25,
        sex="FEMALE",
        bmi=22.4,
        children=0,
        smoker="no",
        region="northwest",
    )
    assert profile.sex == "female"
    assert profile.region == "northwest"
    assert len(warnings) == 0


def test_validate_profile_out_of_bounds_warning():
    profile, warnings = validate_profile(
        age=75,
        sex="male",
        bmi=24.0,
        children=0,
        smoker="no",
        region="southeast",
    )
    assert profile.age == 75
    assert len(warnings) >= 1
    assert "outside the training dataset range" in warnings[0]


def test_validate_profile_invalid_age():
    with pytest.raises(ValueError, match="Age must be an integer"):
        validate_profile(
            age=-5,
            sex="male",
            bmi=25.0,
            children=0,
            smoker="no",
            region="southwest",
        )


def test_validate_profile_invalid_category():
    with pytest.raises(ValueError, match="Smoker status must be one of"):
        validate_profile(
            age=30,
            sex="male",
            bmi=25.0,
            children=0,
            smoker="occasionally",
            region="southwest",
        )
