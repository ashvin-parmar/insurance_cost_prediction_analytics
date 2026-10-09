# Testing Strategy & Test Case Documentation

## 1. Testing Philosophy
The testing strategy validates software engineering robustness, numerical precision, and edge-case resilience across the full application pipeline:
- **Unit Tests:** Validates isolated schema definitions, validation boundary checks, vector encoding, and statistical aggregations.
- **Integration Tests:** Validates complete pipeline fitting, model artifact persistence, and dual-engine subprocess execution.
- **Zero Mocking of Core Logic:** Formulas for MAE, RMSE, $R^2$, and Min-Max scaling are verified against standard scikit-learn implementations.

---

## 2. Test Suite Inventory

| Test Module | Test Functions | Scope & Verification Objective |
|---|---|---|
| `tests/test_schema.py` | `test_valid_profile_creation` | Verifies dataclass construction and DataFrame conversion. |
| | `test_validate_profile_success` | Validates allowable ranges and case-insensitive normalization. |
| | `test_validate_profile_out_of_bounds_warning` | Verifies warning flags for inputs exceeding observed data limits. |
| | `test_validate_profile_invalid_age` | Rejects negative or extreme ages with descriptive ValueError. |
| | `test_validate_profile_invalid_category` | Rejects non-domain categories (e.g., smoker='occasionally'). |
| `tests/test_data_validation.py` | `test_validate_clean_dataset` | Validates clean synthetic dataset and report generation. |
| | `test_validate_invalid_dataset` | Detects missing columns, null values, and negative numbers. |
| | `test_duplicate_detection` | Flags duplicate rows while preserving raw data integrity. |
| | `test_compute_numeric_summary` | Verifies statistical metrics (mean, std, IQR, median). |
| | `test_compute_category_breakdowns` | Verifies value counts and percentage shares. |
| | `test_compute_group_charges_summary` | Verifies grouped aggregations. |
| | `test_compute_correlation_matrix` | Computes Pearson correlation coefficients. |
| | `test_load_real_dataset` | Verifies that local `data/insurance.csv` loads with 1,338 records. |
| `tests/test_preprocessing.py` | `test_build_preprocessor_shape` | Verifies ColumnTransformer produces 11 one-hot encoded columns. |
| | `test_build_pipeline_inference` | Validates end-to-end fitting and inference on unseen profiles. |
| `tests/test_metrics.py` | `test_compute_metrics_perfect_fit` | Verifies MAE=0, RMSE=0, R²=1.0 on identical arrays. |
| | `test_compute_metrics_known_error` | Verifies mathematical error calculations against known baselines. |
| `tests/test_prediction.py` | `test_prediction_result_formatting` | Validates USD currency formatting and disclaimer attachment. |
| | `test_prediction_service_execution` | Tests prediction execution via service layer. |
| `tests/test_scenarios.py` | `test_scenario_comparison_delta` | Verifies absolute and percentage delta calculations. |
| | `test_scenario_comparison_identical_profiles` | Verifies zero delta when profiles match. |

---

## 3. Running Tests
To run the automated test suite:
```bash
# Run pytest with concise summary
python -m pytest -q

# Run with verbose output
python -m pytest -v
```
