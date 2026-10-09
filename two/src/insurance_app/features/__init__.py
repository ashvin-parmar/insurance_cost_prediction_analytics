"""Feature definitions and schema module."""

from .schema import (
    ALL_COLUMNS,
    CATEGORICAL_FEATURES,
    FEATURE_COLUMNS,
    INPUT_BOUNDS,
    NUMERIC_FEATURES,
    OBSERVED_LIMITS,
    REGIONS,
    SEX_CATEGORIES,
    SMOKER_CATEGORIES,
    TARGET_COLUMN,
    InsuranceProfile,
    validate_profile,
)

__all__ = [
    "ALL_COLUMNS",
    "CATEGORICAL_FEATURES",
    "FEATURE_COLUMNS",
    "NUMERIC_FEATURES",
    "REGIONS",
    "SEX_CATEGORIES",
    "SMOKER_CATEGORIES",
    "TARGET_COLUMN",
    "INPUT_BOUNDS",
    "OBSERVED_LIMITS",
    "InsuranceProfile",
    "validate_profile",
]
