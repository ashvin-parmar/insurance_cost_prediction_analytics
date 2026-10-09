#!/usr/bin/env python3
"""CLI script to train, evaluate, and persist all regression models.

Usage:
    python scripts/train_models.py
"""

import sys
from pathlib import Path

# Add project root src to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from insurance_app.config import DATA_PATH, MODELS_DIR
from insurance_app.ml.train import train_all_models


def main():
    print("=" * 65)
    print("Medical Insurance Cost Prediction - Model Training Pipeline")
    print("=" * 65)
    print(f"Loading dataset: {DATA_PATH}")

    metrics_output, metadata = train_all_models(DATA_PATH, MODELS_DIR)

    print("\n--- Model Evaluation Summary (Held-Out Test Set: 20%, Seed: 42) ---")
    print(f"{'Model Name':<30} | {'MAE ($)':<10} | {'RMSE ($)':<10} | {'R² Score':<10}")
    print("-" * 68)

    for key, data in metrics_output.items():
        m = data["metrics"]
        print(f"{data['name']:<30} | ${m['mae']:<9.2f} | ${m['rmse']:<9.2f} | {m['r2']:<10.4f}")

    print("-" * 68)
    print(f"Best Performing Model: {metadata['best_model_name']} (selected as default)")
    print(f"Artifacts successfully saved to: {MODELS_DIR}/")
    print("=" * 65)


if __name__ == "__main__":
    main()
