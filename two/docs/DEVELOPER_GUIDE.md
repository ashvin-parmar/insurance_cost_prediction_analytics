# Developer & Setup Guide

## Prerequisites
- **Python:** 3.10, 3.11, or 3.12 (Python 3.11/3.12 recommended)
- **Git**
- **C Compiler (Optional):** GCC / Clang (for compiling the C inference CLI if desired)

---

## 1. Local Environment Setup

### Linux / macOS
```bash
# Navigate to the project directory
cd /media/ashvin/code/GitRepo/college-proj/two

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

### Windows (PowerShell)
```powershell
# Navigate to the project directory
Set-Location two

# Create and activate virtual environment
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

---

## 2. Environment Diagnostics

Verify that your Python runtime, dependencies, dataset, and artifacts are properly recognized:
```bash
python scripts/check_environment.py
```

---

## 3. Running Automated Tests

Run the test suite using pytest:
```bash
python -m pytest -q
```

---

## 4. Retraining Machine Learning Models

To re-run the ML training pipeline and regenerate all models and metrics:
```bash
python scripts/train_models.py
```

---

## 5. Launching the Streamlit Presentation Dashboard

To start the interactive presentation UI:
```bash
python -m streamlit run app.py
```
This starts the local web server at `http://localhost:8501`.
