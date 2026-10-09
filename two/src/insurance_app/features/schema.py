"""Authoritative feature schema contract shared across Python services.

Defines allowable inputs, validation boundaries, and transformation mappings.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Tuple

import pandas as pd

# Feature Definitions
NUMERIC_FEATURES: List[str] = ["age", "bmi", "children"]
CATEGORICAL_FEATURES: List[str] = ["sex", "smoker", "region"]
FEATURE_COLUMNS: List[str] = NUMERIC_FEATURES + CATEGORICAL_FEATURES
TARGET_COLUMN: str = "charges"
ALL_COLUMNS: List[str] = FEATURE_COLUMNS + [TARGET_COLUMN]

# Allowed Categorical Domains
SEX_CATEGORIES: Tuple[str, ...] = ("female", "male")
SMOKER_CATEGORIES: Tuple[str, ...] = ("no", "yes")
REGIONS: Tuple[str, ...] = ("northeast", "northwest", "southeast", "southwest")

# Dataset Observed Ranges (for warning flags vs hard validation bounds)
OBSERVED_LIMITS = {
    "age": {"min": 18, "max": 64},
    "bmi": {"min": 15.96, "max": 53.13},
    "children": {"min": 0, "max": 5},
    "charges": {"min": 1121.87, "max": 63770.43},
}

# Permissible UI Input Bounds
INPUT_BOUNDS = {
    "age": {"min": 1, "max": 120, "default": 30},
    "bmi": {"min": 10.0, "max": 70.0, "default": 25.0},
    "children": {"min": 0, "max": 10, "default": 0},
}


@dataclass(frozen=True)
class InsuranceProfile:
    """Represents a validated individual profile for insurance prediction."""

    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to standard dictionary."""
        return asdict(self)

    def to_dataframe(self) -> pd.DataFrame:
        """Convert to a 1-row Pandas DataFrame with exact column names."""
        return pd.DataFrame([self.to_dict()])[FEATURE_COLUMNS]


def validate_profile(
    age: int,
    sex: str,
    bmi: float,
    children: int,
    smoker: str,
    region: str,
) -> Tuple[InsuranceProfile, List[str]]:
    """Validates user inputs against allowed schemas.

    Returns:
        (InsuranceProfile, list_of_warning_messages)
    Raises:
        ValueError: If any input fails strict boundary or categorical requirements.
    """
    errors: List[str] = []
    warnings: List[str] = []

    # Age validation
    if not isinstance(age, int) or age < INPUT_BOUNDS["age"]["min"] or age > INPUT_BOUNDS["age"]["max"]:
        errors.append(f"Age must be an integer between {INPUT_BOUNDS['age']['min']} and {INPUT_BOUNDS['age']['max']}.")
    elif age < OBSERVED_LIMITS["age"]["min"] or age > OBSERVED_LIMITS["age"]["max"]:
        warnings.append(f"Age {age} is outside the training dataset range (18–64). Predictions may be extrapolated.")

    # BMI validation
    if not isinstance(bmi, (int, float)) or bmi < INPUT_BOUNDS["bmi"]["min"] or bmi > INPUT_BOUNDS["bmi"]["max"]:
        errors.append(f"BMI must be between {INPUT_BOUNDS['bmi']['min']} and {INPUT_BOUNDS['bmi']['max']}.")
    elif bmi < OBSERVED_LIMITS["bmi"]["min"] or bmi > OBSERVED_LIMITS["bmi"]["max"]:
        warnings.append(f"BMI {bmi:.2f} is outside the training dataset range (15.96–53.13).")

    # Children validation
    if not isinstance(children, int) or children < INPUT_BOUNDS["children"]["min"] or children > INPUT_BOUNDS["children"]["max"]:
        errors.append(f"Children count must be an integer between {INPUT_BOUNDS['children']['min']} and {INPUT_BOUNDS['children']['max']}.")
    elif children > OBSERVED_LIMITS["children"]["max"]:
        warnings.append(f"Children count {children} exceeds the training dataset max (5).")

    # Categorical validation
    sex_norm = str(sex).strip().lower()
    if sex_norm not in SEX_CATEGORIES:
        errors.append(f"Sex must be one of {SEX_CATEGORIES}, got '{sex}'.")

    smoker_norm = str(smoker).strip().lower()
    if smoker_norm not in SMOKER_CATEGORIES:
        errors.append(f"Smoker status must be one of {SMOKER_CATEGORIES}, got '{smoker}'.")

    region_norm = str(region).strip().lower()
    if region_norm not in REGIONS:
        errors.append(f"Region must be one of {REGIONS}, got '{region}'.")

    if errors:
        raise ValueError("; ".join(errors))

    profile = InsuranceProfile(
        age=int(age),
        sex=sex_norm,
        bmi=float(bmi),
        children=int(children),
        smoker=smoker_norm,
        region=region_norm,
    )
    return profile, warnings
