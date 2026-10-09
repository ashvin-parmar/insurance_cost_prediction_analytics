# Pure Python Project Verification & Acceptance Checklist

## Phase Progress Tracker

- [x] **Phase 1: Architecture, Skeleton & Environment Setup** (Completed)
- [x] **Phase 2: Data Pipeline, Validation & Exploratory Data Analysis** (Completed)
- [x] **Phase 3: Machine Learning Training, Evaluation & Artifact Persistence** (Completed)
- [x] **Phase 4: Streamlit UI & Core Prediction Service** (Completed)
- [x] **Phase 5: Model Insights, Residuals & What-If Comparison Engine** (Completed)
- [x] **Phase 6: Pure Python Stack Consolidation & Navigation Refactoring** (Completed)
- [x] **Phase 7: Final QA, College Project Report & Viva Preparation** (Completed)

---

## Acceptance Criteria (100% Pure Python)

### Core Functionality
- [x] 1. The dashboard launches cleanly from `.venv` (`python -m streamlit run app.py`).
- [x] 2. The overview page loads and validates the real dataset (`insurance.csv`).
- [x] 3. All six inputs produce predictions from the saved Python models (`.joblib`).
- [x] 4. Invalid or missing inputs produce understandable messages.
- [x] 5. All three regression models (Linear Regression, Random Forest, Gradient Boosting) are trained and benchmarked.
- [x] 6. Model metrics shown in the UI match saved evaluation results (`metrics.json`).
- [x] 7. The what-if engine calculates differences correctly ($\Delta$ and $\%\Delta$).
- [x] 8. Clean navigation between Overview, Predict, Insights, What-If, and About.

### ML Correctness & Integrity
- [x] 9. Preprocessing is fitted on training data only (no data leakage).
- [x] 10. All models use a reproducible split and documented seed (`test_size=0.2, random_state=42`).
- [x] 11. The held-out test set is not used for model selection.
- [x] 12. MAE, RMSE, and $R^2$ are calculated correctly from real test-set predictions.
- [x] 13. No target leakage occurs (`charges` is never used as input).
- [x] 14. Predictions are finite values in the expected target units (USD $).

### Quality & Documentation
- [x] 15. Automated test suite passes (`pytest`).
- [x] 16. README includes setup, training, run, and test instructions.
- [x] 17. Dataset source and model limitations are clearly documented.
- [x] 18. Formal college project report ready for submission (`docs/PROJECT_REPORT.md`).
- [x] 19. Complete viva voce examination preparation guide (`docs/VIVA_QUESTIONS.md`).
- [x] 20. Generated artifacts and dependencies are reproducible.
