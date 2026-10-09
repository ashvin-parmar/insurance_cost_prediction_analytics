import sys
from pathlib import Path

# Ensure src/ is on sys.path for direct execution / cloud platforms
src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import streamlit as st

from insurance_app.ui.components import render_disclaimer
from insurance_app.ui.styling import apply_custom_css

apply_custom_css()

st.title("📚 Module E: Project Documentation & Tool Operations")
st.caption("Interactive Reference Manual, System Operations, and Technical Documentation.")

render_disclaimer()

# Document Map
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
PLANNING_DIR = Path(__file__).resolve().parent.parent / "planning"

DOC_MAPPING = {
    "📖 User Guide (Operation Manual)": ("USER_GUIDE.md", "How to navigate and use each dashboard feature"),
    "🛠️ Developer & Setup Guide": ("DEVELOPER_GUIDE.md", "Step-by-step installation for Windows, Linux, and macOS"),
    "🏗️ System Architecture": ("ARCHITECTURE.md", "Modular system design, data flows, and pipeline contracts"),
    "📊 Dataset Specification": ("DATASET.md", "Dataset dictionary, feature schemas, and statistical properties"),
    "🤖 ML Methodology & Modeling": ("ML_METHODOLOGY.md", "Preprocessing pipelines, regression models, and selection criteria"),
    "🧪 Testing Strategy & Inventory": ("TESTING.md", "Automated test suite documentation and quality assertions"),
    "🎓 Project Submission Report": ("PROJECT_REPORT.md", "Comprehensive academic report aligned with Proforma-I"),
    "🎤 Viva Voce Examination Guide": ("VIVA_QUESTIONS.md", "Key theoretical and practical viva questions with model answers"),
}

# Sidebar/Top Selector
st.markdown("### 🗂️ Browse Project Documentation")
doc_choice = st.selectbox(
    "Select a document to read in-app:",
    list(DOC_MAPPING.keys()),
    index=0,
)

filename, description = DOC_MAPPING[doc_choice]
file_path = DOCS_DIR / filename

st.caption(f"**Description:** {description} · *Source file: `docs/{filename}`*")

# Download options
col_dl1, col_dl2 = st.columns([1, 1])

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    with col_dl1:
        st.download_button(
            label=f"⬇️ Download {filename}",
            data=file_content,
            file_name=filename,
            mime="text/markdown",
            use_container_width=True,
        )

# Download Viva PDF if available
pdf_path = PLANNING_DIR / "Viva_and_Project_Presentation_Guide.pdf"
if pdf_path.exists():
    with open(pdf_path, "rb") as pf:
        pdf_bytes = pf.read()
    with col_dl2:
        st.download_button(
            label="🎓 Download Complete Viva PDF Guide",
            data=pdf_bytes,
            file_name="Viva_and_Project_Presentation_Guide.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

st.markdown("---")

# Render Document Content in Expandable / Formatted View
if file_path.exists():
    with st.container():
        st.markdown(file_content)
else:
    st.error(f"File `{filename}` could not be located in the `docs/` folder.")

st.markdown("---")

# Operational Guide to Application Modules
st.subheader("💡 Interactive Tool Guide: How Each Dashboard Module Works")

with st.expander("📊 Module A: Overview & Exploratory Data Analysis (EDA)", expanded=False):
    st.markdown("""
    **Purpose:** Uncover statistical trends, relationships, and distributions across 1,338 patient records.
    - **Key Metrics Row:** Instant display of dataset size, missing count (0), mean charge, and smoker proportion.
    - **Interactive Filters:** Filter dataset by Region, Sex, and Smoking status in the sidebar to dynamically inspect subsets.
    - **Visual Tools:**
      - *Histogram & KDE:* Visualizes the heavy right skew of medical charges.
      - *Grouped Box Plots:* Visualizes charge variations across smoker status, sex, and regions.
      - *Scatter Plot with Trendlines:* Dynamic scatter exploration between Age, BMI, and Charges.
      - *Correlation Heatmap:* Annotated Pearson correlation coefficients.
    - **Data Export:** Download filtered data in CSV format directly.
    """)

with st.expander("🔮 Module B: Predict - Real-Time Cost Estimation Form", expanded=False):
    st.markdown("""
    **Purpose:** Input personalized demographics and calculate real-time estimated annual insurance premiums.
    - **Input Form:**
      - **Age:** Slider (18 to 64 years standard, bounds up to 120).
      - **BMI:** Number input (15.0 to 55.0 kg/m²). Real-time WHO classification tag (Underweight, Normal, Overweight, Obese).
      - **Children:** Dependent selector (0 to 5 dependents).
      - **Smoking Status:** High-impact lifestyle indicator (No / Yes).
      - **Sex & Region:** Demographic classification inputs.
    - **Algorithm Choice:** Select between **Gradient Boosting (Best Model)**, **Random Forest**, or **Linear Regression**.
    - **Population Benchmark Cards:** Compare the calculated estimate against the historical cohort median and general population averages.
    - **Prediction Breakdown:** Compare outputs from all 3 regression algorithms simultaneously on the same submitted profile.
    - **Export:** Export profile and predicted charge in JSON format.
    """)

with st.expander("📈 Module C: Model Insights & Performance Comparisons", expanded=False):
    st.markdown("""
    **Purpose:** Academic benchmarking and evaluation diagnostics on the held-out test set (20% split, $N=268$).
    - **Performance Metrics Table:** Direct comparison of MAE, RMSE, and $R^2$ across all three trained models.
    - **Actual vs. Predicted Scatter Plots:** Visual assessment of regression fit along the ideal 45-degree parity line ($y = x$).
    - **Residual Distribution Diagnostics:** Inspect error histograms and verify centered zero-mean residual distributions.
    - **Feature Importance Chart:** Decision tree feature ranking showing **smoker**, **bmi**, and **age** as leading predictors.
    """)

with st.expander("⚖️ Module D: What-If Comparison Simulator", expanded=False):
    st.markdown("""
    **Purpose:** Understand the exact dollar impact of individual lifestyle changes through counterfactual analysis.
    - **Side-by-Side Dual Profiles:** Maintain a Baseline Profile on the left and adjust an Alternative Profile on the right.
    - **1-Click Counterfactual Presets:**
      - *Quit Smoking Preset:* Instant counterfactual demonstrating average cost savings (~$23,000+).
      - *Normalize BMI Preset:* Demonstrates savings achieved by lowering BMI into normal weight range (<25.0).
      - *Age Progression (+10 Years):* Visualizes aging impact on medical costs.
    - **Delta Cards:** Computes absolute dollar difference ($\Delta$) and relative percentage difference ($\% \Delta$).
    """)
