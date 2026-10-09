"""Statistical calculations and EDA metrics engine.

Calculates real summary statistics from loaded dataset without hardcoded numbers.
"""

from __future__ import annotations

from typing import Any, Dict

import numpy as np
import pandas as pd

from insurance_app.features.schema import (
    CATEGORICAL_FEATURES,
    NUMERIC_FEATURES,
    TARGET_COLUMN,
)


def compute_numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Computes descriptive statistics for numeric attributes and the target.

    Returns DataFrame with rows: count, mean, std, min, 25%, 50% (median), 75%, max.
    """
    cols = [c for c in NUMERIC_FEATURES + [TARGET_COLUMN] if c in df.columns]
    summary = df[cols].describe().T
    summary["median"] = df[cols].median()
    # Reorder columns
    ordered_cols = ["count", "mean", "std", "min", "25%", "median", "75%", "max"]
    return summary[ordered_cols]


def compute_category_breakdowns(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """Computes value counts and percentage proportions for each categorical variable."""
    breakdowns: Dict[str, pd.DataFrame] = {}
    for col in CATEGORICAL_FEATURES:
        if col in df.columns:
            counts = df[col].value_counts()
            pcts = (df[col].value_counts(normalize=True) * 100).round(2)
            summary_df = pd.DataFrame({"Count": counts, "Percentage (%)": pcts})
            breakdowns[col] = summary_df
    return breakdowns


def compute_group_charges_summary(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Computes charges summary (mean, median, min, max, count) segmented by group_col."""
    if group_col not in df.columns or TARGET_COLUMN not in df.columns:
        raise ValueError(f"Columns '{group_col}' and '{TARGET_COLUMN}' must both be in the DataFrame.")

    grouped = df.groupby(group_col)[TARGET_COLUMN].agg(
        count="count",
        mean="mean",
        median="median",
        std="std",
        min="min",
        max="max",
    ).round(2)
    return grouped


def compute_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Computes Pearson correlation matrix for numerical attributes and the target."""
    cols = [c for c in NUMERIC_FEATURES + [TARGET_COLUMN] if c in df.columns]
    return df[cols].corr().round(3)
