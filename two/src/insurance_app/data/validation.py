"""Dataset validation and data quality auditing module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from insurance_app.features.schema import (
    ALL_COLUMNS,
    CATEGORICAL_FEATURES,
    NUMERIC_FEATURES,
    REGIONS,
    SEX_CATEGORIES,
    SMOKER_CATEGORIES,
    TARGET_COLUMN,
)


@dataclass
class DataValidationReport:
    """Detailed summary of data quality, completeness, and schema conformance."""

    is_valid: bool
    total_rows: int
    total_columns: int
    duplicate_rows_count: int
    missing_values_by_column: Dict[str, int]
    invalid_categories: Dict[str, List[str]]
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def has_duplicates(self) -> bool:
        return self.duplicate_rows_count > 0

    @property
    def has_missing_values(self) -> bool:
        return any(cnt > 0 for cnt in self.missing_values_by_column.values())


def validate_dataset(df: pd.DataFrame) -> DataValidationReport:
    """Performs a comprehensive audit on the input DataFrame.

    Checks:
    - Existence of all seven required columns.
    - Presence of missing (null / NaN / infinite) values.
    - Identification of duplicate records.
    - Numeric validity (age, bmi, children, charges must be non-negative numbers).
    - Categorical validity (sex, smoker, region match permissible domains).

    Returns:
        DataValidationReport: Complete validation assessment without altering data.
    """
    errors: List[str] = []
    warnings: List[str] = []

    # 1. Column existence check
    missing_cols = [c for c in ALL_COLUMNS if c not in df.columns]
    if missing_cols:
        errors.append(f"Missing required columns in dataset: {missing_cols}")

    extra_cols = [c for c in df.columns if c not in ALL_COLUMNS]
    if extra_cols:
        warnings.append(f"Dataset contains unexpected extra columns: {extra_cols}")

    total_rows = len(df)
    total_columns = len(df.columns)

    # 2. Duplicate rows check
    duplicates_count = int(df.duplicated().sum())
    if duplicates_count > 0:
        warnings.append(
            f"Dataset contains {duplicates_count} duplicate rows ({duplicates_count / total_rows * 100:.2f}%). "
            f"Retained for transparency as per academic guidelines."
        )

    # 3. Missing / Non-finite check
    missing_by_col = {col: int(df[col].isna().sum()) for col in df.columns}
    total_missing = sum(missing_by_col.values())
    if total_missing > 0:
        errors.append(f"Found {total_missing} missing values across columns: {missing_by_col}")

    # 4. Numeric validity
    for col in NUMERIC_FEATURES + [TARGET_COLUMN]:
        if col in df.columns:
            if not np.issubdtype(df[col].dtype, np.number):
                errors.append(f"Column '{col}' must be numeric, got dtype '{df[col].dtype}'.")
            else:
                negatives = int((df[col] < 0).sum())
                if negatives > 0:
                    errors.append(f"Column '{col}' contains {negatives} negative values.")
                inf_count = int(np.isinf(df[col]).sum())
                if inf_count > 0:
                    errors.append(f"Column '{col}' contains {inf_count} infinite values.")

    # 5. Categorical domain checks
    invalid_cats: Dict[str, List[str]] = {}

    def _check_domain(col: str, allowed: tuple):
        if col in df.columns:
            unique_vals = set(df[col].dropna().astype(str).str.strip().str.lower().unique())
            invalid = sorted(list(unique_vals - set(allowed)))
            if invalid:
                invalid_cats[col] = invalid
                errors.append(f"Column '{col}' contains invalid values: {invalid}. Allowed: {allowed}")

    _check_domain("sex", SEX_CATEGORIES)
    _check_domain("smoker", SMOKER_CATEGORIES)
    _check_domain("region", REGIONS)

    is_valid = len(errors) == 0

    return DataValidationReport(
        is_valid=is_valid,
        total_rows=total_rows,
        total_columns=total_columns,
        duplicate_rows_count=duplicates_count,
        missing_values_by_column=missing_by_col,
        invalid_categories=invalid_cats,
        errors=errors,
        warnings=warnings,
    )
