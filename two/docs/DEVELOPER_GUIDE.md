# Developer & Cross-Platform Installation Guide

This guide covers step-by-step installation, dependency configuration, diagnostics, and execution instructions for **Windows**, **Linux**, and **macOS**.

---

## 💻 System Prerequisites

| Component | Minimum Requirement | Recommended | Notes |
| :--- | :--- | :--- | :--- |
| **Python** | Python 3.10+ | Python 3.11 or 3.12 | Ensure Python is added to system PATH |
| **Pip** | 23.0+ | Latest | Bundled with modern Python distributions |
| **Git** | 2.25+ | Latest | For cloning and version control |
| **RAM** | 2 GB | 4 GB+ | Lightweight regression models |
| **Disk Space** | 200 MB | 500 MB | Includes packages, dataset & artifacts |

---

## 🛠️ Step-by-Step Installation

### 1. Windows (Command Prompt or PowerShell)

#### Prerequisites on Windows:
- Download Python from [python.org](https://www.python.org/downloads/).
- **Important:** During installation, check the box: `[x] Add python.exe to PATH`.

#### Setup Commands:
```powershell
# 1. Open PowerShell or Command Prompt and clone / navigate to repository
cd path\to\medical_insurance_cost_prediction_and_analytics

# 2. Create a virtual environment (using Python launcher)
py -3.12 -m venv .venv
# (Or if using standard python command: python -m venv .venv)

# 3. Activate the virtual environment
# In PowerShell:
.\.venv\Scripts\Activate.ps1
# (Note: If script execution is restricted in PowerShell, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)

# Or in classic Command Prompt (cmd.exe):
.\.venv\Scripts\activate.bat

# 4. Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

---

### 2. Linux (Ubuntu / Debian / Fedora / Arch)

#### Prerequisites on Linux:
```bash
# Ubuntu / Debian:
sudo apt update
sudo apt install python3 python3-venv python3-pip git -y

# Fedora:
sudo dnf install python3 python3-pip git -y
```

#### Setup Commands:
```bash
# 1. Navigate to repository root
cd /path/to/medical_insurance_cost_prediction_and_analytics

# 2. Create virtual environment
python3 -m venv .venv

# 3. Activate virtual environment
source .venv/bin/activate

# 4. Upgrade pip and install project dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

---

### 3. macOS (Apple Silicon M1/M2/M3 & Intel)

#### Prerequisites on macOS:
- Ensure Command Line Tools or Homebrew is installed:
```bash
# If Homebrew is installed:
brew install python@3.12 git
```

#### Setup Commands:
```bash
# 1. Navigate to repository root
cd /path/to/medical_insurance_cost_prediction_and_analytics

# 2. Create virtual environment
python3 -m venv .venv

# 3. Activate virtual environment
source .venv/bin/activate

# 4. Upgrade pip and install project dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

---

## 🔍 Verification & Diagnostics

Once installed and activated on any operating system, verify all dependencies and dataset files:

```bash
python scripts/check_environment.py
```
**Expected Output:**
```
============================================================
Medical Insurance Application - Pure Python Diagnostics
============================================================
--- 1. Python Runtime ---
Detected Python: 3.12.x
  [OK] Supported Python release.
--- 2. Required Packages ---
  [OK] streamlit, pandas, numpy, sklearn, plotly, joblib, pytest
--- 3. Dataset Availability ---
  [OK] Dataset located at: .../data/insurance.csv
--- 4. Machine Learning Artifacts ---
  [OK] Linear Regression, Random Forest, Gradient Boosting
============================================================
System fully operational.
```

---

## 🧪 Automated Testing

Execute the comprehensive 21-test pytest suite:
```bash
pytest -v
```
All unit tests, validation assertions, and scenario tests will pass across Windows, Linux, and macOS.

---

## 🤖 Re-training Machine Learning Pipelines

To re-fit all three regression algorithms (Linear Regression, Random Forest, Gradient Boosting) and generate fresh serialized `.joblib` models and JSON metrics:
```bash
python scripts/train_models.py
```

---

## 🚀 Launching the Interactive Web Dashboard

To launch the multi-page Streamlit application:
```bash
python -m streamlit run app.py
```
Open your web browser at:
`http://localhost:8501`
