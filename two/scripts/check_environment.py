#!/usr/bin/env python3
"""Cross-platform environment check script for the Medical Insurance Cost Prediction application.

Inspects Python version, installed packages, dataset availability, and model artifacts
without altering any files or environment state.
"""

import importlib
import sys
from pathlib import Path

# Add project root to sys.path to resolve insurance_app package
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

try:
    from insurance_app.config import (
        DATA_PATH,
        GRADIENT_BOOSTING_MODEL_PATH,
        LINEAR_REGRESSION_MODEL_PATH,
        METADATA_PATH,
        METRICS_PATH,
        RANDOM_FOREST_MODEL_PATH,
    )
except ImportError:
    DATA_PATH = PROJECT_ROOT / "data" / "insurance.csv"
    METRICS_PATH = PROJECT_ROOT / "models" / "metrics.json"
    METADATA_PATH = PROJECT_ROOT / "models" / "metadata.json"
    LINEAR_REGRESSION_MODEL_PATH = PROJECT_ROOT / "models" / "linear_regression.joblib"
    RANDOM_FOREST_MODEL_PATH = PROJECT_ROOT / "models" / "random_forest.joblib"
    GRADIENT_BOOSTING_MODEL_PATH = PROJECT_ROOT / "models" / "gradient_boosting.joblib"


REQUIRED_PACKAGES = [
    "streamlit",
    "pandas",
    "numpy",
    "sklearn",  # scikit-learn
    "plotly",
    "joblib",
    "pytest",
]


def check_python_version() -> bool:
    print("--- 1. Python Runtime ---")
    version = sys.version_info
    print(f"Detected Python: {version.major}.{version.minor}.{version.micro}")
    if version.major == 3 and version.minor in (10, 11, 12):
        print("  [OK] Supported Python release.")
        return True
    elif version.major == 3 and version.minor >= 9:
        print("  [WARNING] Python release >= 3.9 detected, 3.11/3.12 recommended.")
        return True
    else:
        print("  [FAIL] Python 3.10+ required.")
        return False


def check_packages() -> bool:
    print("\n--- 2. Required Packages ---")
    all_ok = True
    for pkg in REQUIRED_PACKAGES:
        try:
            mod = importlib.import_module(pkg)
            ver = getattr(mod, "__version__", "installed")
            print(f"  [OK] {pkg:15} : {ver}")
        except ImportError:
            print(f"  [MISSING] {pkg:15} : Not installed")
            all_ok = False
    return all_ok


def check_dataset() -> bool:
    print("\n--- 3. Dataset Availability ---")
    if DATA_PATH.exists():
        size_kb = DATA_PATH.stat().st_size / 1024
        print(f"  [OK] Dataset located at: {DATA_PATH} ({size_kb:.1f} KB)")
        return True
    else:
        print(f"  [MISSING] Dataset not found at: {DATA_PATH}")
        return False


def check_models() -> bool:
    print("\n--- 4. Machine Learning Artifacts ---")
    artifacts = [
        ("Linear Regression", LINEAR_REGRESSION_MODEL_PATH),
        ("Random Forest", RANDOM_FOREST_MODEL_PATH),
        ("Gradient Boosting", GRADIENT_BOOSTING_MODEL_PATH),
        ("Evaluation Metrics", METRICS_PATH),
        ("Pipeline Metadata", METADATA_PATH),
    ]
    all_present = True
    for name, path in artifacts:
        if path.exists():
            print(f"  [OK] {name:20} : Found")
        else:
            print(f"  [PENDING] {name:20} : Not yet trained (Run scripts/train_models.py)")
            all_present = False
    return all_present


def main():
    print("=" * 60)
    print("Medical Insurance Application - Pure Python Diagnostics")
    print("=" * 60)
    py_ok = check_python_version()
    pkg_ok = check_packages()
    data_ok = check_dataset()
    models_ok = check_models()
    print("=" * 60)

    if py_ok and pkg_ok and data_ok and models_ok:
        print("System fully operational. Ready to run Streamlit app:")
        print("  python -m streamlit run app.py")
    else:
        print("Some prerequisites are pending. Check outputs above.")


if __name__ == "__main__":
    main()
