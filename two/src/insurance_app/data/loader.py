"""Dataset loading utility with caching and path resolution."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

import pandas as pd
import streamlit as st

from insurance_app.config import DATA_PATH


@st.cache_data(show_spinner=False)
def load_dataset(path: Optional[Union[str, Path]] = None) -> pd.DataFrame:
    """Loads the medical insurance CSV dataset from disk.

    Args:
        path: Optional path to the CSV file. If None, defaults to DATA_PATH in config.

    Returns:
        pd.DataFrame: The loaded dataset.

    Raises:
        FileNotFoundError: If the CSV file does not exist at the target path.
        ValueError: If the file is empty or cannot be parsed as CSV.
    """
    target_path = Path(path) if path is not None else DATA_PATH

    if not target_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at: '{target_path}'. "
            f"Please verify the file exists or set INSURANCE_DATA_PATH."
        )

    try:
        df = pd.read_csv(target_path)
    except Exception as exc:
        raise ValueError(f"Failed to read dataset from '{target_path}': {exc}") from exc

    if df.empty:
        raise ValueError(f"The dataset at '{target_path}' is completely empty.")

    return df
