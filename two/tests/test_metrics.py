"""Unit tests for regression metrics calculations."""

import numpy as np
from insurance_app.ml.evaluate import compute_metrics


def test_compute_metrics_perfect_fit():
    y_true = np.array([1000.0, 2000.0, 3000.0, 4000.0])
    y_pred = np.array([1000.0, 2000.0, 3000.0, 4000.0])

    m = compute_metrics(y_true, y_pred)
    assert m["mae"] == 0.0
    assert m["rmse"] == 0.0
    assert m["r2"] == 1.0


def test_compute_metrics_known_error():
    y_true = np.array([10.0, 20.0, 30.0])
    y_pred = np.array([12.0, 18.0, 31.0])  # errors: +2, -2, +1 -> MAE = 5/3 = 1.67

    m = compute_metrics(y_true, y_pred)
    assert m["mae"] == 1.67
    assert m["rmse"] > 0
    assert 0.0 <= m["r2"] <= 1.0
