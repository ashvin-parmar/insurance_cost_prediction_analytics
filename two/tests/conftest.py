"""Pytest configuration and shared fixtures."""

import sys
from pathlib import Path
import pytest

# Ensure src/ is on sys.path during test execution
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from insurance_app.features.schema import InsuranceProfile


@pytest.fixture
def sample_valid_profile():
    """Provides a known valid profile fixture."""
    return InsuranceProfile(
        age=30,
        sex="male",
        bmi=25.5,
        children=1,
        smoker="no",
        region="southwest",
    )


@pytest.fixture
def sample_smoker_profile():
    """Provides a valid smoker profile fixture."""
    return InsuranceProfile(
        age=45,
        sex="female",
        bmi=32.0,
        children=2,
        smoker="yes",
        region="southeast",
    )
