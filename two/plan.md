Here are the complete guideline to make this project.


# Complete Project Blueprint: Medical Insurance Cost Prediction & Analytics Dashboard

Your project should be developed as a cross-platform Python web application with an interactive Streamlit dashboard, a machine-learning analytics pipeline, and a C-based inference engine for comparison.

The goal is not simply to build a webpage that predicts insurance costs. You want a complete college-project deliverable that demonstrates software engineering, machine learning, data analysis, model evaluation, cross-language integration, testing, documentation, and a professional viva presentation.

This guideline is structured so you can give it to Claude (Anthropic), Gemini, or another coding AI in separate phases. Each phase has explicit deliverables, acceptance criteria, and instructions to prevent the AI from generating disconnected code or inventing results.

## 1. Project definition

# Medical Insurance Cost Prediction Using Machine Learning

Project type: Final-year academic project · Software / Machine Learning

Proposed application: Insurance Cost Prediction & Analytics Dashboard

Primary objective: Predict estimated medical insurance charges from six demographic and lifestyle attributes, and provide an interactive interface for exploring the dataset, evaluating regression models, comparing scenarios, and explaining model behaviour.

Existing asset: A working C CLI inference application with a custom linear algebra framework, saved model weights and Min-Max scaling parameters.

Target stack: Python, Streamlit, Pandas, NumPy, scikit-learn, Plotly, pytest and optional integration with the existing C executable.

Deployment target: Local, cross-platform execution on Linux, Windows and macOS.

### The seven dataset columns

| Column     | Role              | Type         |
| ---------- | ----------------- | ------------ |
| `age`      | Input feature     | Numeric      |
| `sex`      | Input feature     | Categorical  |
| `bmi`      | Input feature     | Numeric      |
| `children` | Input feature     | Integer      |
| `smoker`   | Input feature     | Categorical  |
| `region`   | Input feature     | Categorical  |
| `charges`  | Prediction target | Numeric, USD |

The application must use the six input features to estimate `charges`. It must not use `charges` as an input to a prediction.

### What makes this project distinctive?

1. A working prediction interface rather than a terminal-only application.

2. Dataset exploration with interactive visualizations.

3. Training and comparison of multiple regression algorithms.

4. A what-if simulator for comparing hypothetical input profiles.

5. A bridge between your existing C implementation and Python predictions.

6. Reproducible model training, automated tests and complete project documentation.

One important academic distinction: the dataset's `charges` field represents insurance charges in the source data. Your output is an estimate produced by a model, not an official insurance quotation or a medical diagnosis.

## 2. Final technology decisions

Use the following stack as the default architecture. Avoid introducing additional frameworks unless a specific requirement justifies them.

| Layer             | Technology                       | Responsibility                                  |
| ----------------- | -------------------------------- | ----------------------------------------------- |
| Language          | Python 3.11 or 3.12              | Application and ML code                         |
| Web UI            | Streamlit                        | Pages, forms, controls and presentation         |
| Data processing   | Pandas, NumPy                    | Data validation and transformations             |
| ML                | scikit-learn                     | Training, preprocessing, metrics and inference  |
| Charts            | Plotly Express and Graph Objects | Interactive visualizations                      |
| Testing           | pytest                           | Unit, integration and regression tests          |
| Code quality      | Ruff                             | Linting and formatting                          |
| Model persistence | joblib                           | Saving fitted Python pipelines                  |
| C integration     | Existing C CLI/executable        | Independent prediction comparison               |
| Documentation     | Markdown                         | Setup, architecture, methodology and user guide |
| Version control   | Git and GitHub                   | Source management and reproducibility           |

Recommended compatibility policy: use a supported Python release consistently across development and CI, pin dependency versions in a lock or constraints file, and test the selected release on Linux, Windows and macOS. Do not assume that a package version tested on one platform will automatically work identically on every platform.

## 3. Required application features

Build the application in four main modules, with a separate project information and documentation area.

![KPI Dashboard Design :: Behance](https://images.openai.com/static-rsc-4/RrMEoHlSAvpfR257fUx56SCQGc-G8_RGU3ts6lS9msgU1PGX8XeHAgAiruDwYD6fuCPZCvJN8qWbGfdtvzr-7_rlVpIlcxCF1zjGwQb9gvBDBB53SloUjHhOKOsVUR8UeCREJeipFl4hNl-RmWVqltIjf4a_gsnUuV_2jYI-SLo?purpose=inline)

Add to Favorites

Module A — Overview & Data Analytics

Purpose: explain the dataset and the problem before showing predictions.

* Project introduction, objectives and methodology.

* Dataset row count, feature count, missing values and duplicate count.

* Summary statistics for numerical variables.

* Distribution of insurance charges, age and BMI.

* Charges by smoking status, sex and region.

* Age-versus-charges and BMI-versus-charges scatter plots.

* Correlation heatmap for numeric columns.

* Dataset validation warnings and preprocessing summary.

![Transforming Insurance Pricing with Machine Learning: From EDA to Deployment | by Dr. Vipula (Sri) Sharma | Medium](https://images.openai.com/static-rsc-4/LcUdmiBZ1tHEYHUS5N62OtI74E6VEZb8i5EO6PpW6XjqwJTnKJdfYB2NWodbbsfkWR2Wq682a4VKED_ccwywJhFntkMf0tZcrq-PFauMObePvlUmncZ9YVi54qluepfQDMv4Aw2cqPo1Qg-q4hM67OPrET3beIbsqIA-6O5JojE?purpose=inline)

Add to Favorites

Module B — Interactive Prediction

Purpose: let a user submit a profile and obtain a model estimate.

* Age slider, BMI input, children selector and categorical dropdowns.

* Input validation and understandable error messages.

* Predict button and currency-formatted result card.

* Selected profile summary.

* Selected model name and version.

* Optional comparison against the C inference engine.

* Clear explanation that the output is an estimate.

![PyCaret inside Streamlit - Using Streamlit - Streamlit](https://images.openai.com/static-rsc-4/8bwPUTzHvHzmq_tEY_r-u9y30G68EhBJkyuDHTnKees4788A7_1Yxa4YUfYsbf63DIgicJZb5PRKeISuCtWUpxmOSwxWpT7p2emTXva_8Kxl2gAH8UkvQ-iapqmI-0SmpbRRKNvnwApGjRAy6c_DdjZpClv9fJRAFCkOAQNJgAI?purpose=inline)

Add to Favorites

Module C — Model Insights & Comparisons

Purpose: demonstrate that the project evaluates models rather than merely producing predictions.

* Linear Regression baseline.

* Random Forest Regressor.

* Gradient Boosting Regressor.

* Consistent train/test split and evaluation metrics.

* MAE, RMSE and R² comparison table.

* Actual-versus-predicted scatter plots.

* Residual analysis.

* Feature importance or coefficients, depending on model.

* Training configuration and model selection explanation.

![What-If Analysis Dashboard | InetSoft Product Information](https://images.openai.com/static-rsc-4/F1IGZDAWRQYlLGzll7VRbvONZVOjtMkwEliPT5-a53fgKfkRo-_6-ek4FLA-i5ZyK3L53o1eBBGTnsns610V8g1jiTk63FrME3eQCF_J39CwX-l1J-BiVNPOl2polctRlDLErdSUhAjeY4LRwtT5OapALvO2R5LjF3u4W8xdWvo?purpose=inline)

Add to Favorites

Module D — What-If Comparison Engine

Purpose: compare model outputs for alternative hypothetical profiles.

* Baseline and alternative profile inputs.

* Side-by-side predicted charges.

* Absolute and percentage difference.

* Comparison chart and changed-feature summary.

* One-click scenarios such as changing smoking status or BMI.

* Reset and swap-profile controls.

* Clear warnings against interpreting model differences as causal effects.

### Additional pages

* About the Project: objectives, problem statement, dataset source, workflow and limitations.

* Model Information: chosen model, features, preprocessing, evaluation results and training date.

* Documentation & Credits: project instructions, dataset attribution, library licences and contributors.

The pages should be easy to navigate, work on laptop and mobile-sized screens, and have a consistent theme. Prefer a clean, restrained design with readable typography, a sidebar, informative charts, and no decorative elements that distract from the data.

## 4. Critical architecture decision: Python versus C

Your existing C application already performs a complete inference workflow. Preserve that achievement instead of rewriting it unnecessarily.

The architecture should distinguish between two different model paths.

Streamlit presentation layer

Overview · Prediction · Model evaluation · What-if

Python ML service

Preprocessing, scikit-learn pipelines, training, metrics and Python inference.

C inference adapter

Existing C implementation, trained weights, scaling parameters and prediction comparison.

The C path is an independent inference implementation, not a replacement for the Python model-comparison pipeline.

### 4.1 Python model path

Use a scikit-learn `Pipeline` and `ColumnTransformer` where appropriate, so preprocessing and prediction remain consistent. The Python models are trained and evaluated on a reproducible split of the dataset.

The Python app should load a persisted pipeline for normal prediction. It should not retrain every model each time a user opens the app.

### 4.2 C model path

The existing C implementation uses:

* A 12-element feature vector.

* One-hot encoding of `sex`, `smoker` and `region`.

* Min-Max scaling from `insurance_min_max.csv`.

* Trained linear-regression weights from `model.csv`.

* Inverse scaling to convert the output into USD charges.

The C model's exact preprocessing and weight order must be preserved. Do not assume it is equivalent to the Python `LinearRegression` pipeline merely because both use linear regression.

The Python interface may invoke the compiled C executable using Python's `subprocess` module, passing validated inputs and parsing a documented output format. This is the simplest initial integration if the C application can be adapted to support non-interactive input.

Important: do not compile C source code automatically at every Streamlit page render. Compilation should be a separate development/build step. At runtime, detect a missing executable and show a useful message.

If you want to keep the C CLI unchanged, the dashboard can still demonstrate its independent results through a separate integration script or documented terminal command. A non-interactive adapter is preferable for a polished live demo.

### 4.3 Model compatibility and data integrity

The project must never silently:

* Load a model with the wrong feature order.

* Use Python encodings for C inference.

* Apply a scaler twice.

* Mix target scaling with feature scaling.

* Replace the existing C parameters with newly trained Python parameters without documenting the change.

* Present predictions from two different models as if they were the same model.

Store metadata describing each model, its expected feature schema, preprocessing, training dataset and evaluation metrics.

## 5. Machine-learning methodology

The coding AI must implement this section carefully because it forms the core of your project report and viva.

### 5.1 Data source and validation

Use the dataset already selected for the project. If it is the commonly used medical insurance dataset from Kaggle, retain the original attribution and exact source URL in the documentation:

[Medical Insurance Cost Prediction dataset on Kaggle](https://www.kaggle.com/datasets/rahulvyasm/medical-insurance-cost-prediction)

The project must not depend on a live internet connection at application startup. The dataset should be stored locally or provided by the user.

Required validation:

* Confirm all seven expected columns exist.

* Check numeric columns are actually numeric.

* Check categorical values against the dataset's allowed categories.

* Detect missing values, duplicate rows and invalid values.

* Record the number of rows before and after any cleaning.

* Never silently drop rows or invent replacement values.

* Display a helpful error when the dataset is missing or invalid.

Possible UI input constraints should be based on the dataset and clearly documented. Do not claim that the observed dataset range defines every medically possible value.

### 5.2 Exploratory data analysis (EDA)

Include the following analyses:

| Analysis                 | Suggested visualization        |
| ------------------------ | ------------------------------ |
| Distribution of charges  | Histogram with adjustable bins |
| Age distribution         | Histogram                      |
| BMI distribution         | Histogram                      |
| Charges by smoker status | Box plot                       |
| Charges by sex           | Box plot                       |
| Charges by region        | Box plot                       |
| Age versus charges       | Scatter plot                   |
| BMI versus charges       | Scatter plot                   |
| Children versus charges  | Box plot or grouped summary    |
| Numerical correlation    | Correlation heatmap            |

Every chart must have a descriptive title, labelled axes, units where applicable, and readable tooltips.

Do not imply correlation proves causation. The dataset is observational, and any findings should be described accordingly.

### 5.3 Feature preprocessing

For Python models, use consistent preprocessing:

* Numeric features: `age`, `bmi`, `children`.

* Categorical features: `sex`, `smoker`, `region`.

* Target: `charges`.

Use `OneHotEncoder(handle_unknown="ignore")` or an equivalent carefully tested strategy for categorical features. Use a `ColumnTransformer` to keep preprocessing attached to the model pipeline.

For the C implementation, preserve its own existing feature vector and scaling logic. The two implementations can have different encodings internally, provided their inputs represent the same profile and their outputs are compared correctly.

### 5.4 Avoid data leakage

Split the dataset into training and test sets before fitting preprocessing or selecting hyperparameters.

Recommended initial configuration:

* Test size: 20%.

* Fixed random seed: `42`.

* Training split: 80%.

* Test split: 20%.

Fit transformations on training data only. Use cross-validation within the training set if model tuning is introduced. The held-out test set should be used for final evaluation, not repeated model selection.

For the C model, establish how its existing weights were trained. If the original training split or preprocessing statistics are unknown, document that limitation rather than claiming a fair test-set comparison.

### 5.5 Models to train and compare

Start with three regressors:

1. Linear Regression — baseline, easy to interpret.

2. Random Forest Regressor — captures nonlinear relationships and interactions.

3. Gradient Boosting Regressor — another tree-based regression model.

Start with sensible, documented defaults. Add hyperparameter tuning only after the baseline implementation and tests are working.

All models must use the same split and compatible preprocessing, with the same target scale, so that their metrics are comparable.

### 5.6 Evaluation metrics

Implement the following definitions:

MAE⁡=1n∑i=1n∣yi−y^i∣\operatorname{MAE}=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat y_i|MAE=n1i=1∑n∣yi−y^i∣

RMSE⁡=1n∑i=1n(yi−y^i)2\operatorname{RMSE}= \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2}RMSE=n1i=1∑n(yi−y^i)2

R2=1−∑i(yi−y^i)2∑i(yi−yˉ)2R^2=1-\frac{\sum_i(y_i-\hat y_i)^2} {\sum_i(y_i-\bar y)^2}R2=1−∑i(yi−yˉ)2∑i(yi−y^i)2

Explain these in plain language in the app:

* MAE: average absolute prediction error, in USD.

* RMSE: prediction error with a greater penalty for large errors, in USD.

* R²: how well the model explains variation in the target on the evaluated dataset. It can be negative on test data.

Do not put fabricated accuracy percentages in the UI or report. Calculate all metrics from actual model evaluation.

### 5.7 Model selection and feature explanations

Select a default model using a documented criterion, such as lowest test-set-independent validation MAE, rather than selecting whichever model looks best on the test set.

For explanations:

* Linear Regression: display coefficients with a clear explanation of feature encoding and units.

* Random Forest and Gradient Boosting: display model-specific feature importance.

* Optionally add permutation importance calculated on held-out data.

* If SHAP is introduced later, make it an optional enhancement with proper explanations.

Do not claim that feature importance demonstrates causality or that a coefficient necessarily describes a causal effect.

## 6. Detailed functional requirements

Give the coding AI these exact behavioural requirements.

### 6.1 Overview & analytics page

The page should:

* Display the project name, objective and brief workflow.

* Load the dataset through a shared data-loading module.

* Display dataset size, missing-value count, duplicate count and number of features.

* Show summary statistics.

* Render the EDA charts described earlier.

* Explain the main findings using computed statistics, not hard-coded observations.

* Display data-quality warnings when necessary.

* Offer a dataset preview with configurable row count.

* Keep charts responsive and allow filtering where appropriate.

All displayed counts and statistical summaries must be calculated from the active dataset.

### 6.2 Interactive prediction page

Provide these controls:

| Input    | UI control                     | Validation                                      |
| -------- | ------------------------------ | ----------------------------------------------- |
| Age      | Integer slider or number input | Positive integer within documented limits       |
| Sex      | Dropdown                       | Dataset-supported categories                    |
| BMI      | Numeric input or slider        | Positive finite number within documented limits |
| Children | Integer selector               | Non-negative integer                            |
| Smoker   | Dropdown                       | Dataset-supported categories                    |
| Region   | Dropdown                       | Dataset-supported categories                    |

The user must be able to change inputs and explicitly run a prediction.

After prediction, display:

* Estimated charges formatted as USD.

* The six selected input values.

* The selected model's name and version.

* A short explanation of how the estimate was generated.

* Any warnings about inputs outside the observed dataset range.

Use Streamlit session state only where necessary to preserve selections and results. Avoid storing sensitive user data or adding a database unless required.

If prediction fails, show an understandable error message. Never show an old result as though it belongs to the latest input profile.

### 6.3 Model comparison page

Display a comparison table with columns such as:

| Model             | MAE (USD)  | RMSE (USD) | R²         |
| ----------------- | ---------- | ---------- | ---------- |
| Linear Regression | Calculated | Calculated | Calculated |
| Random Forest     | Calculated | Calculated | Calculated |
| Gradient Boosting | Calculated | Calculated | Calculated |

These are placeholders for the table design only; the actual application must calculate the results.

Required charts:

* MAE comparison.

* RMSE comparison.

* R² comparison.

* Actual versus predicted values.

* Residuals versus predicted values.

* Feature importance or coefficient visualizations.

Include a training button only if interactive retraining is required. Prefer a separate training command for reproducible builds, with the dashboard reading saved evaluation results.

If the user trains a new model, record the configuration, dataset fingerprint, random seed, timestamp and metrics.

### 6.4 What-if comparison engine

Create two editable profiles:

* Baseline profile: original input values.

* Alternative profile: modified values.

Allow the user to copy the baseline, reset a profile, or change selected attributes.

Calculate:

Δ=y^alternative−y^baseline\Delta = \hat y_{\text{alternative}}-\hat y_{\text{baseline}}Δ=y^alternative−y^baseline

%Δ=y^alternative−y^baseliney^baseline×100\%\Delta = \frac{\hat y_{\text{alternative}}-\hat y_{\text{baseline}}} {\hat y_{\text{baseline}}}\times100%Δ=y^baseliney^alternative−y^baseline×100

Handle a baseline prediction of zero without dividing by zero; display percentage difference as unavailable in that case.

Display:

* Both predictions.

* Absolute difference in USD.

* Percentage difference where defined.

* Features that changed.

* A grouped bar chart or other clear comparison visualization.

Preset scenarios may include changing smoking status, BMI or age. Every scenario should be presented as a hypothetical model-input comparison, not a prediction of what would happen if someone changed their lifestyle. In particular, smoking status is an observational feature, not evidence of a causal cost reduction.

### 6.5 C versus Python comparison page or section

This is a strong differentiator for your project.

Provide an optional comparison interface with:

* Identical profile inputs sent to both implementations.

* Python prediction.

* C prediction.

* Absolute prediction difference.

* Relative difference when the denominator is nonzero.

* A clear statement of which model each output uses.

If the C executable is unavailable, the Python application must continue functioning normally and show the C comparison as unavailable.

Do not force the C executable to run on every page load. Invoke it only when requested or when a deliberate comparison is triggered.

## 7. Proposed repository and folder structure

Ask the coding AI to use a maintainable structure instead of putting the whole application into one giant `app.py` file.

```
medical-insurance-dashboard/
├── app.py
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Predict.py
│   ├── 3_Model_Insights.py
│   ├── 4_What_If.py
│   ├── 5_C_Comparison.py
│   └── 6_About.py
├── src/
│   └── insurance_app/
│       ├── __init__.py
│       ├── config.py
│       ├── data/
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   └── validation.py
│       ├── features/
│       │   ├── __init__.py
│       │   └── schema.py
│       ├── ml/
│       │   ├── __init__.py
│       │   ├── preprocessing.py
│       │   ├── train.py
│       │   ├── evaluate.py
│       │   ├── predict.py
│       │   └── registry.py
│       ├── analytics/
│       │   ├── __init__.py
│       │   ├── statistics.py
│       │   └── charts.py
│       ├── services/
│       │   ├── __init__.py
│       │   ├── prediction_service.py
│       │   ├── scenario_service.py
│       │   └── c_adapter.py
│       └── ui/
│           ├── __init__.py
│           ├── components.py
│           └── styling.py
├── c_engine/
│   ├── README.md
│   ├── src/
│   ├── include/
│   └── build/
├── data/
│   ├── README.md
│   └── .gitkeep
├── models/
│   ├── README.md
│   └── .gitkeep
├── reports/
│   ├── README.md
│   └── .gitkeep
├── tests/
│   ├── test_data_validation.py
│   ├── test_preprocessing.py
│   ├── test_prediction.py
│   ├── test_metrics.py
│   ├── test_scenarios.py
│   └── test_c_adapter.py
├── scripts/
│   ├── train_models.py
│   ├── evaluate_models.py
│   └── check_environment.py
├── docs/
│   ├── PROJECT_REPORT.md
│   ├── ARCHITECTURE.md
│   ├── DATASET.md
│   ├── ML_METHODOLOGY.md
│   ├── USER_GUIDE.md
│   ├── DEVELOPER_GUIDE.md
│   ├── TESTING.md
│   ├── VIVA_QUESTIONS.md
│   └── screenshots/
├── .streamlit/
│   └── config.toml
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── LICENSE
└── CITATION.cff
```

This is the proposed target, not a demand to create empty files for every feature on day one. The coding AI should create files when implementing the relevant module and remove unnecessary boilerplate.

Architecture rule: UI pages should call service functions; they should not independently implement preprocessing, model loading, or prediction formulas. There must be one authoritative prediction service per model path.

The C source code may remain in its existing repository or be included as a submodule if its dependencies and licensing permit. Do not duplicate a large custom C framework without a reason.

## 8. Data, configuration and model management

### Dataset location

The application should support a local CSV file, configured through an environment variable or a documented configuration option.

For example:

```
INSURANCE_DATA_PATH=data/insurance.csv
```

The app must show an actionable error if the file is missing. Do not automatically download a dataset on startup.

Do not commit the complete dataset unless the source licence and college requirements permit redistribution. Provide a download or acquisition instruction instead.

### Model files

Recommended artifacts:

```
models/
├── linear_regression.joblib
├── random_forest.joblib
├── gradient_boosting.joblib
├── metrics.json
└── metadata.json
```

These files should be generated by the training pipeline, not fabricated by the AI.

The metadata should identify:

* Model name and version.

* Training date and random seed.

* Input schema and expected types.

* Preprocessing pipeline.

* Dataset fingerprint.

* Training configuration.

* Evaluation split and metrics.

* Python and scikit-learn versions.

Only load trusted model files. Deserializing a malicious pickle or joblib file can execute code. Never load a model uploaded by an untrusted user.

### Existing C parameters

Keep the C engine's `model.csv` and `insurance_min_max.csv` in a clearly documented location. Treat these as C-engine artifacts and never confuse them with Python's joblib models.

The C adapter must verify that the expected parameter files exist before making a prediction.

## 9. Cross-platform initialization and development

The application should work on Linux, Windows and macOS. Python source files should not contain OS-specific paths or hard-coded commands.

### Recommended Python environment

Use a virtual environment and the `python -m pip` form of package installation. This reduces ambiguity when several Python installations are present.

For initial development, use Python 3.11 or 3.12 consistently across the team.

#### Linux and macOS

Bash

```
git clone <YOUR_FORK_URL>
cd medical-insurance-dashboard

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

#### Windows PowerShell

PowerShell

```
git clone <YOUR_FORK_URL>
Set-Location medical-insurance-dashboard

py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

If PowerShell blocks activation due to its execution policy, use the appropriate policy allowed by your machine or invoke the environment's Python executable directly. Do not require users to disable system-wide security controls.

### Starting the app

After placing the dataset at the documented path:

Bash

```
python -m streamlit run app.py
```

This command is intended to be the same on all three operating systems when the virtual environment is activated.

### Running the tests

Bash

```
python -m pytest -q
```

### Retraining the models

Bash

```
python scripts/train_models.py
```

### Checking the environment

Bash

```
python scripts/check_environment.py
```

The environment-check script should report Python version, dependency availability, dataset status, model artifact status and optional C-engine availability without modifying the user's system.

### Important cross-platform rules

* Use `pathlib.Path` for filesystem paths.

* Use `subprocess.run` with an argument list, not a shell-constructed command.

* Do not hard-code `/home/...`, Windows drive letters or macOS-specific directories.

* Avoid relying on a system-wide Python package installation.

* Keep platform-specific C build instructions in `c_engine/README.md`.

* Use a separate build step for the C executable.

* Test file encoding, path handling, model loading and chart rendering on all supported platforms.

* Provide Windows, Linux and macOS commands in the README.

For a college demonstration, local execution is sufficient. Cloud deployment can be a later enhancement, not a prerequisite.

## 10. Divide the work into independent phases

Do not ask Claude or Gemini to generate the entire application in a single response. Large one-shot generation often results in inconsistent imports, missing functions, duplicated preprocessing, fake metrics and modules that do not work together.

Use the following phase plan. Each phase should produce a working, testable increment.

## 01

Architecture and repository audit

Foundation

Inspect the existing C source, parameter files, dataset and any forked Python repository. Finalize the architecture, dependencies, file structure, feature schema and C/Python integration contract.

Deliverable: architecture document, project skeleton, setup instructions and an implementation checklist.

## 02

Data pipeline and exploratory analysis

Data

Implement dataset loading, schema validation, missing-value checks, statistical summaries and reusable Plotly charts.

Deliverable: reliable data module, EDA functions and tests.

## 03

ML training and evaluation

Machine learning

Implement the three regressors, consistent preprocessing, a reproducible split, evaluation metrics and model persistence.

Deliverable: trained model artifacts, metrics, metadata and automated tests.

## 04

Streamlit UI and prediction service

Application

Build the navigation, overview page, prediction form, result card and model selection logic.

Deliverable: an end-to-end working app that accepts a profile and returns a real model prediction.

## 05

Model insights and what-if engine

Analytics

Add metric comparisons, actual-versus-predicted charts, residual analysis, feature explanations and baseline/alternative profile comparison.

Deliverable: complete analytics and scenario modules using the same prediction service.

## 06

C integration and cross-platform testing

Integration

Connect the existing C inference engine, compare predictions where model compatibility is established, and test optional failure behaviour.

Deliverable: documented C adapter, integration tests and build instructions.

## 07

Final documentation, QA and presentation

Submission

Complete the README, report, methodology, test results, installation guide, viva preparation and screenshots.

Deliverable: reproducible final project, documented limitations and presentation-ready application.

Rule for every phase: do not start the next phase until the current phase's tests pass and its interfaces are stable. When multiple AIs are used, keep the architecture and interface contracts in one shared document.

## 11. Copy-ready master prompt for Claude or Gemini

Use this prompt first. It establishes the project requirements and tells the AI how to work in subsequent phases.

MASTER PROJECT INSTRUCTIONS — MEDICAL INSURANCE COST PREDICTION & ANALYTICS DASHBOARD

# MASTER PROJECT INSTRUCTIONS — MEDICAL INSURANCE COST PREDICTION & ANALYTICS DASHBOARD

## Your role

Act as a senior Python developer, machine-learning engineer, Streamlit developer, software architect, test engineer, and technical documentation writer.

Help me build a complete, working, cross-platform college project. Do not merely provide example snippets or a visual prototype. The final application must run locally, use real machine-learning models, pass automated tests, and include comprehensive documentation.

## 1. Project context

Project title: Medical Insurance Cost Prediction Using Machine Learning.

The project predicts medical insurance charges in USD from six input features:

* age

* sex

* bmi

* children

* smoker

* region

Target column: charges.

The dataset contains seven columns: age, sex, bmi, children, smoker, region, charges.

Dataset source:
[https://www.kaggle.com/datasets/rahulvyasm/medical-insurance-cost-prediction](https://www.kaggle.com/datasets/rahulvyasm/medical-insurance-cost-prediction)

Do not assume the dataset file exists until its location is confirmed. Do not download data automatically at application startup.

## 2. Existing C application

I already have a C-based CLI inference application using a custom linear algebra framework.

Its inference workflow:

1. Accept age, sex, BMI, children, smoker status, and region.

2. Build a 12-dimensional feature vector in this exact order:
   \(Bias, Age, Sex\_M, Sex\_F, BMI, Children, Smoker\_Y, Smoker\_N, Region\_SW, Region\_SE, Region\_NW, Region\_NE\).

3. Apply Min-Max normalization using insurance_min_max.csv.

4. Load linear-regression weights from model.csv.

5. Calculate the prediction using a dot product.

6. Inverse-scale the target into USD charges.

The existing C implementation is an important project asset. Preserve it and do not rewrite it unnecessarily.

The Python application will provide the interactive web interface, EDA, model training, evaluation, and Python inference.

The C engine will remain an independently documented inference implementation. Integrate it through a subprocess adapter only after confirming that its input/output protocol can be made reliable.

Never assume that the C and Python models have identical weights, preprocessing, or training data. Compare their outputs only with the appropriate compatibility caveats.

## 3. Technology stack

Use:

* Python 3.11 or 3.12

* Streamlit

* Pandas

* NumPy

* scikit-learn

* Plotly

* joblib

* pytest

* Ruff

* Git and GitHub

Use Python standard-library features where possible. Avoid unnecessary dependencies.

The application must work on Linux, Windows, and macOS.

## 4. Required modules

### A. Project Overview & Analytics

Include:

* Project objectives and workflow.

* Dataset shape, columns, missing values and duplicate counts.

* Numerical summary statistics.

* Charge, age and BMI distributions.

* Charges grouped by smoker status, sex and region.

* Age-versus-charges and BMI-versus-charges charts.

* Numerical correlation heatmap.

* Dataset preview and validation warnings.

Calculate statistics from the actual dataset. Do not invent observations.

### B. Interactive Prediction

Provide validated inputs for all six features.

Display:

* Estimated charges in USD.

* Input profile summary.

* Model name and version.

* Relevant validation warnings.

* An explicit estimation disclaimer.

Use a shared prediction service and persisted model pipeline. Do not duplicate prediction formulas across UI pages.

### C. Model Insights & Comparisons

Train and evaluate:

1. Linear Regression

2. Random Forest Regressor

3. Gradient Boosting Regressor

Use the same reproducible train/test split, seed, target units, and appropriate preprocessing strategy for fair comparison.

Report MAE, RMSE and R².

Provide actual-versus-predicted plots, residual analysis, and model-appropriate feature explanations.

Fit preprocessing on training data only. Do not use the held-out test set to select the final model.

### D. What-If Comparison

Allow users to compare two hypothetical profiles.

Show both predicted costs, absolute difference, percentage difference where defined, and the features changed.

Handle division by zero and invalid inputs. Explain that differences are model-based hypothetical comparisons, not causal effects or guaranteed savings.

### E. C Engine Comparison

Allow an optional comparison between Python inference and the existing C inference executable.

Use identical input profiles. Show both model identities and the difference between their outputs.

If the C executable or its parameter files are unavailable, the main Python application must continue working and clearly indicate that C comparison is unavailable.

### F. About & Documentation

Include project objectives, dataset attribution, model methodology, limitations, software versions and usage instructions.

## 5. Architecture requirements

Use a maintainable multi-module architecture. Keep UI, data loading, preprocessing, training, evaluation, prediction services, scenario comparison and C integration separate.

Use a shared feature schema and centralized validation.

Use scikit-learn pipelines and ColumnTransformer where appropriate. Use OneHotEncoder(handle_unknown="ignore") for categorical preprocessing unless a documented alternative is needed.

Keep C feature encoding and scaling separate from Python preprocessing.

Load trusted, previously trained model artifacts for normal application usage. Do not retrain on every page load.

Keep model metadata, training configuration and evaluation metrics with the generated artifacts.

Use pathlib for file paths and safe subprocess invocation for C integration. Never use shell string concatenation to construct executable commands.

## 6. Data and ML integrity

Validate the seven expected dataset columns.

Check types, missing values, duplicates, categorical values, and invalid numeric values.

Never fabricate model metrics, prediction results, data rows, model files, or feature importance values.

Do not silently remove data or substitute invented values.

Use a documented fixed random seed and record model configuration.

Explain that charges are the dataset target and that predictions are estimates.

Do not claim correlation or feature importance proves causation.

Do not describe the system as a clinically validated or officially approved insurance pricing tool.

## 7. Cross-platform support

Provide instructions for Linux, Windows PowerShell, and macOS.

Use a Python virtual environment and documented dependencies.

The main command should be:

python -m streamlit run app.py

Testing command:

python -m pytest -q

Training command:

python scripts/train_models.py

Do not require Linux-specific paths or commands in the Python source code.

Document any separate compiler requirements for the C executable.

## 8. Testing requirements

Create unit tests for data validation, preprocessing, predictions, metrics, scenario calculations, and model loading.

Create integration tests for application services and the optional C adapter.

Verify:

* The model accepts all valid profiles.

* Invalid inputs are rejected or handled safely.

* Predictions are finite numeric values.

* Preprocessing is consistent between training and inference.

* Scenario differences are calculated correctly.

* Model artifacts and dataset paths are validated.

* Missing C artifacts do not break the Python app.

* A clean environment can install dependencies and run tests.

Do not claim tests passed unless they were actually run.

## 9. Documentation deliverables

Create:

* README.md

* docs/ARCHITECTURE.md

* docs/DATASET.md

* docs/ML_METHODOLOGY.md

* docs/USER_GUIDE.md

* docs/DEVELOPER_GUIDE.md

* docs/TESTING.md

* docs/PROJECT_REPORT.md

* docs/VIVA_QUESTIONS.md

* docs/screenshots/

* C-engine integration documentation.

Include environment setup, dataset placement, training, running, testing, troubleshooting, model limitations, citations, and contribution instructions.

The project report must distinguish completed functionality from proposed or optional features. Include real evaluation results only after the model pipeline has run.

## 10. How you must work

Work in small, explicitly defined phases.

For every phase:

1. State its scope and dependencies.

2. Inspect existing files before modifying them.

3. List files to create or change.

4. Implement complete files with correct imports and compatible interfaces.

5. Provide exact commands to run.

6. Add and execute relevant tests whenever the environment permits.

7. Report actual test results and unresolved issues.

8. Update documentation.

9. Confirm the phase's acceptance criteria before continuing.

Do not generate the entire application in a single response.

Do not use fake functions, placeholder predictions, random metrics, hard-coded dataset findings, or fabricated successful test results.

Do not silently change the architecture, model feature order, model output units, or C integration contract.

If repository files or execution access are unavailable, clearly identify the missing information and provide complete, ready-to-create files rather than claiming the application was executed.

## 11. Start here

Begin with Phase 1: architecture and repository audit.

Ask me for the existing repository or folder structure, the dataset location, the C source and parameter files, and any selected GitHub fork.

Inspect what is actually available. Produce the architecture, final folder structure, dependency strategy, model integration contract, and Phase 1 acceptance checklist.

Do not start implementing all UI pages yet. First establish a reliable foundation for the complete application.

## 12. Phase-specific implementation prompts

After the master prompt, use the following prompts one at a time. They are designed to produce complete modules rather than disconnected examples.

### Phase 1 — Architecture and audit

Writing

Implement Phase 1 only.

Inspect the existing project files and the chosen GitHub fork if access is available. Inspect the C CLI source, model.csv, insurance_min_max.csv, dataset schema, dependency requirements and existing UI.

Do not assume that files exist if they have not been provided.

Produce:

1. A repository audit listing files inspected and important findings.

2. A final architecture and data-flow description.

3. A finalized folder structure.

4. A feature-schema contract shared by the Python services.

5. A separate specification for the C feature vector, scaling, input protocol, output protocol and error handling.

6. A dependency and supported-Python-version policy.

7. A configuration strategy for the dataset and model artifact paths.

8. A phased implementation checklist with explicit acceptance criteria.

9. Architecture and developer documentation.

10. A minimal runnable application skeleton only if it can be completed without guessing about unavailable project details.

Do not fabricate dataset metrics or C/Python model equivalence.

Stop after Phase 1. List missing inputs and exact next steps. Do not implement the full dashboard yet.

### Phase 2 — Data loading and EDA

Writing

Implement Phase 2 of the approved architecture.

Create the dataset-loading, validation, statistical-summary and exploratory-visualization modules.

Requirements:

* Validate all seven required columns.

* Handle missing files and malformed CSV files with useful errors.

* Check numeric and categorical types.

* Detect missing values, duplicate rows, invalid categories and non-finite values.

* Report data-quality issues without silently changing the dataset.

* Calculate summary statistics from the loaded data.

* Create reusable Plotly chart functions for charge distributions, age, BMI, smoker groups, sex groups, regions, scatter plots and numeric correlations.

* Add automated tests using small synthetic fixtures created specifically for tests.

* Ensure tests do not require downloading the real dataset.

* Avoid importing Streamlit into low-level data utilities unless necessary.

* Update DATASET.md and relevant developer documentation.

Integrate the module into the overview page only if the page skeleton is available.

Run the tests if execution is available. Report exact results and stop after Phase 2.

### Phase 3 — Training and evaluation

Writing

Implement Phase 3 of the approved architecture: the complete machine-learning pipeline.

Create:

* Centralized preprocessing.

* Linear Regression.

* Random Forest Regressor.

* Gradient Boosting Regressor.

* Reproducible train/test splitting.

* Optional training-only cross-validation.

* MAE, RMSE and R² calculations.

* Actual-versus-predicted data.

* Residual analysis data.

* Feature explanation data appropriate to each model.

* Model persistence using joblib.

* Metadata and evaluation reports.

* A training CLI script.

* Tests for preprocessing, metrics, model loading and prediction.

Fit all transformations only on the training data. Use a consistent held-out test set for final evaluation. Do not use the test set for tuning or model selection.

Do not generate fake metrics or dummy models as final artifacts. Do not train on application startup.

Record the random seed, feature schema, target units, dependency versions, dataset fingerprint, split configuration and model parameters.

Use a documented selection criterion, preferably validation performance, for selecting a default model.

Preserve the C model artifacts separately.

Run training and tests if the real dataset and execution environment are available. If not, state precisely what is blocked.

Update ML_METHODOLOGY.md. Stop after Phase 3.

### Phase 4 — Streamlit UI and prediction

Writing

Implement Phase 4: the functional Streamlit application and prediction service.

Use the existing architecture and trained model artifacts.

Create:

* App entry point and navigation.

* Overview page.

* Prediction page.

* Reusable UI components.

* Responsive layout and consistent styling.

* Input validation.

* Model loading and caching.

* A shared prediction service.

* A prediction result card.

* Input summary and estimation disclaimer.

* Friendly errors for missing data or model artifacts.

The prediction service must be independent of Streamlit widgets so it can be tested directly.

Use the actual saved preprocessing/model pipeline. Do not hard-code prediction results or duplicate model formulas in UI code.

The interface should have professional visual hierarchy, readable charts and clear navigation. Do not add decorative UI elements that obscure the project data.

Do not implement fake prediction behaviour while waiting for model artifacts. Show a clear configuration error instead.

Add tests for prediction input validation and output correctness. Update USER_GUIDE.md and README.md with exact run commands.

Start the app and run the tests if execution is available. Stop after Phase 4.

### Phase 5 — Model insights and what-if comparison

Writing

Implement Phase 5 using the existing prediction and model-evaluation services.

Create:

1. Model comparison table showing real MAE, RMSE and R².

2. Interactive metric comparison charts.

3. Actual-versus-predicted chart.

4. Residual analysis chart.

5. Feature coefficient or feature-importance visualization appropriate to each estimator.

6. A what-if comparison page with baseline and alternative profiles.

7. Absolute and percentage difference calculations, with zero-denominator handling.

8. Preset hypothetical scenarios and reset/copy controls.

9. Clear descriptions of the assumptions and limitations.

All predictions must come from the saved model pipeline. All evaluation metrics must come from the actual training/evaluation output.

Do not claim that feature importance or scenario differences establish causation.

Test scenario calculations, invalid profiles and missing evaluation artifacts. Update documentation and stop after Phase 5.

### Phase 6 — C engine integration

Writing

Implement Phase 6: optional integration with the existing C inference engine.

First inspect its actual interface and source code. Do not assume that it accepts command-line arguments or emits machine-readable output.

If needed, add a minimal non-interactive adapter that preserves the original CLI behaviour. Document its input/output contract and how it reports errors.

Use Python subprocess with a list of arguments, timeout handling, captured output and return-code validation. Do not use shell=True or concatenate user input into executable commands.

Check that the executable, model.csv and insurance_min_max.csv exist before running inference.

The dashboard must remain usable if the C executable is absent or fails.

Add a C comparison view showing the two model identities, predictions, absolute difference and relative difference when defined.

Only compare outputs directly if the input semantics, target units and intended model relationship are understood. Document any differences in training data, preprocessing or weights.

Provide separate Linux, Windows and macOS build instructions where the compiler and dependencies support them. Do not claim that the C build is portable until it has been tested on the relevant platforms.

Add adapter tests using a fake executable or controlled test fixture, plus integration tests when the actual C build is available.

Update C-engine documentation and stop after Phase 6.

### Phase 7 — Final QA, report and submission

Writing

Implement Phase 7: final quality assurance and documentation.

Inspect the complete repository and identify broken imports, inconsistent interfaces, duplicate logic, unused files, missing dependencies, incorrect model paths, misleading UI labels and undocumented assumptions.

Complete:

* README.md with project overview and complete setup/run/test/training instructions.

* ARCHITECTURE.md with diagrams and module responsibilities.

* DATASET.md with source, schema, validation and limitations.

* ML_METHODOLOGY.md with preprocessing, model training, evaluation and model selection.

* USER_GUIDE.md.

* DEVELOPER_GUIDE.md.

* TESTING.md.

* PROJECT_REPORT.md suitable for college submission.

* VIVA_QUESTIONS.md with questions and accurate answers.

* Screenshots of the actual working application.

* Dependency files, .gitignore, licence and citation information.

* Cross-platform CI tests for supported operating systems and Python versions where feasible.

The project report must include actual computed results only. If a test, screenshot, C build, or platform run has not been completed, identify it as pending.

Verify the app using a clean virtual environment where possible. Run the complete test suite and record the actual output.

Do not claim full platform compatibility based only on running on one operating system.

Provide a final checklist distinguishing completed, verified, pending and optional work. Stop after the final audit.

## 13. Complete documentation requirements

Documentation should be treated as part of the deliverable, not something written from memory at the end. Ask the AI to update documentation during every phase.

Here is the required content of each document.

`README.md` — Project entry point

Project description, features, architecture overview, prerequisites, installation instructions for Linux/Windows/macOS, dataset setup, model training, running the dashboard, testing, troubleshooting, screenshots and credits.

`docs/ARCHITECTURE.md`

Component diagram, data flow, folder structure, responsibilities, Python/C integration, artifact management, error handling and dependency relationships.

`docs/DATASET.md`

Dataset source, schema, target definition, data types, validation rules, missing data, duplicates, categorical encoding and limitations. Add actual dataset statistics only after inspection.

`docs/ML_METHODOLOGY.md`

Regression problem formulation, preprocessing, feature encoding, train/test split, model descriptions, evaluation formulas, model selection and reproducibility.

`docs/USER_GUIDE.md`

Page-by-page instructions, prediction workflow, model comparison, what-if scenarios, result interpretation and common user errors.

`docs/DEVELOPER_GUIDE.md`

Virtual environment setup, code organization, dependencies, adding models, changing the UI, rebuilding the C engine and development workflow.

`docs/TESTING.md`

Test strategy, unit/integration tests, commands, expected behaviours, recorded results, known failures and supported platform coverage.

`docs/PROJECT_REPORT.md`

College submission report: abstract, introduction, problem statement, objectives, literature review, requirements, methodology, system design, implementation, results, testing, limitations, conclusion and references.

`docs/VIVA_QUESTIONS.md`

Questions and answers covering regression, dataset preprocessing, one-hot encoding, Min-Max normalization, linear regression, tree models, evaluation metrics, leakage, Streamlit, C integration, cross-platform support and project limitations.

### College report outline

The report should be based on your institution's prescribed template if one exists. Otherwise, use this sequence:

1. Title page and certificate/declaration, if required.

2. Acknowledgement.

3. Abstract.

4. Table of contents.

5. Introduction and background.

6. Problem statement.

7. Objectives and scope.

8. Literature review and existing-system analysis.

9. Requirements analysis.

10. Proposed system and architecture.

11. Dataset description and preprocessing.

12. Machine-learning methodology.

13. System implementation.

14. User interface screenshots.

15. Experimental setup and actual model results.

16. Testing and verification.

17. Limitations and ethical considerations.

18. Conclusion and future enhancements.

19. References and appendices.

The C inference engine should be described as an existing implementation and an independent inference path. Be precise about which parts were completed earlier and which were developed during the Python dashboard work.

Do not fabricate a literature review, references, results, certificates or screenshots.

## 14. Testing and acceptance criteria

Before considering the application complete, use this checklist. Every item should be marked as verified, pending or not applicable.

## Project verification checklist

0/27 marked

Core functionality

The dashboard launches from a clean virtual environment.

The overview page loads and validates the real dataset.

All six inputs produce a prediction from the saved Python model.

Invalid or missing inputs produce understandable messages.

All three regression models can be trained and evaluated.

Model metrics shown in the UI match saved evaluation results.

The what-if engine calculates differences correctly.

The application remains usable when the C executable is unavailable.

ML correctness

Preprocessing is fitted on training data only.

All models use a reproducible split and documented seed.

The held-out test set is not used for model selection.

MAE, RMSE and R² are calculated correctly.

No target leakage occurs.

Python and C preprocessing are not accidentally mixed.

Predictions are finite values in the expected target units.

Quality and documentation

Unit and integration tests run successfully.

README includes setup, training, run and test instructions.

Dataset source and model limitations are documented.

C integration and build instructions are documented.

No fake metrics or invented test results are present.

Generated artifacts and dependencies are reproducible.

The repository does not contain secrets or unwanted local files.

Portability

Linux setup and execution are tested.

Windows setup and execution are tested.

macOS setup and execution are tested.

Filesystem paths use cross-platform handling.

Optional C integration handles missing executables gracefully.

Copy checklistReset

Mark an item only after verifying it in the actual project. This checklist records your selections in the current interface; it does not execute tests or verify the application automatically.

Passing the Linux tests alone does not prove Windows and macOS compatibility. If you cannot access those systems, use CI runners or mark the platform verification as pending.

## 15. Git and implementation workflow

Use small, reviewable commits so the project remains recoverable if a coding AI breaks an integration.

Suggested sequence:

```
docs: define architecture and implementation plan
chore: initialize cross-platform Python project
feat: add dataset validation and analytics
feat: implement regression training pipeline
feat: add Streamlit prediction page
feat: add model evaluation dashboard
feat: implement what-if comparisons
feat: integrate optional C inference adapter
test: add unit and integration coverage
docs: complete report and user documentation
```

For each phase:

1. Review the generated changes.

2. Run the relevant tests.

3. Check imports and dependency changes.

4. Verify the app starts.

5. Commit the working phase.

6. Continue only after the interfaces remain consistent.

If you fork an existing repository, preserve its licence and attribution. Inspect its existing structure before merging the proposed folder structure; do not overwrite working files just to match the blueprint exactly.

## 16. Final engineering requirements

These requirements should apply across every phase, regardless of which AI is generating the code.

### Code quality

* Use type hints for service interfaces where practical.

* Add docstrings to public functions and classes.

* Use meaningful names and small, testable functions.

* Keep configuration separate from business logic.

* Avoid circular imports and duplicated prediction logic.

* Use logging for debugging and actionable error messages for users.

* Do not suppress exceptions silently.

### Security and privacy

* Do not collect names, phone numbers, medical records or other personal details that are unnecessary for the prediction.

* Do not log users' full profiles by default.

* Never execute arbitrary commands derived from form input.

* Never load untrusted serialized model files.

* Keep credentials and private configuration out of Git.

* Do not present this academic estimator as a clinically validated system or a guaranteed insurance quote.

### Reproducibility

* Use fixed random seeds where applicable.

* Record the actual dependency versions.

* Document how to recreate trained model artifacts.

* Keep evaluation results linked to the corresponding model and dataset.

* Separate generated artifacts from source code.

* Preserve the C model parameters independently of the Python model artifacts.

### UI quality

* Use consistent navigation and visual styling.

* Display meaningful loading states and error messages.

* Cache immutable data and loaded models appropriately.

* Do not cache predictions without considering input and model identity.

* Avoid retraining on every page rerun.

* Ensure every visible button has a working action.

* Make charts responsive and readable.

* Do not use placeholder metrics in the final presentation.

## 17. Recommended order of execution

Here is the order I would follow for your actual project.

1. Start with the master prompt. Give the AI the C source code, model parameters, dataset schema and the GitHub fork you selected. Ask it to audit rather than immediately generate the entire app.

2. Complete data and ML work first. A professional UI is not useful if the prediction pipeline is unreliable. Get real training, evaluation and inference working before extensive styling.

3. Build the core Streamlit prediction page. Verify that a profile submitted through the UI produces the same result as the Python prediction service.

4. Add the EDA and model comparison pages. Use real dataset statistics and stored evaluation outputs.

5. Add what-if analysis and C comparison. These are the main features that differentiate your project from a basic prediction form.

6. Complete tests, documentation and the college report. Capture actual screenshots and metrics only after the application is working.

7. Run the final cross-platform verification. Test on Linux, Windows and macOS, or clearly document any unverified platform.

My most important recommendation: don't let Claude or Gemini rewrite the whole project from scratch or replace your completed C implementation. Have the AI inspect your existing assets first, then build the Python dashboard around a clean, tested prediction service.

That approach gives you a coherent final-year project: an interactive ML application, a reproducible model evaluation pipeline, an independent C inference implementation, and a complete set of technical documentation and testing evidence.

