import sys
from pathlib import Path

# Ensure src/ is on sys.path for direct execution / cloud platforms
src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import json
import pandas as pd
import plotly.express as px
import streamlit as st

from insurance_app.features.schema import (
    INPUT_BOUNDS,
    REGIONS,
    SEX_CATEGORIES,
    SMOKER_CATEGORIES,
    validate_profile,
)
from insurance_app.services.scenario_service import ScenarioService
from insurance_app.ui.components import render_disclaimer, render_metric_card
from insurance_app.ui.styling import apply_custom_css

apply_custom_css()

st.title("⚖️ Module D: What-If Comparison Engine")
st.markdown(
    "Explore how hypothetical modifications to lifestyle, demographic, or dependent factors "
    "affect estimated insurance charges."
)

render_disclaimer()

scenario_svc = ScenarioService()

# Default profile values
DEFAULTS = {
    "b_age": 40,
    "b_sex": "male",
    "b_bmi": 32.5,
    "b_children": 1,
    "b_smoker": "yes",
    "b_region": "southeast",
    "a_age": 40,
    "a_sex": "male",
    "a_bmi": 26.0,
    "a_children": 1,
    "a_smoker": "no",
    "a_region": "southeast",
}

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# One-Click Scenario Presets
st.subheader("⚡ Quick Scenario Presets")
preset_cols = st.columns(4)

with preset_cols[0]:
    if st.button("🚭 Stop Smoking Scenario", use_container_width=True):
        st.session_state["b_smoker"] = "yes"
        st.session_state["a_smoker"] = "no"
        st.rerun()

with preset_cols[1]:
    if st.button("⚖️ Reduce BMI to Normal", use_container_width=True):
        st.session_state["b_bmi"] = 33.0
        st.session_state["a_bmi"] = 24.5
        st.rerun()

with preset_cols[2]:
    if st.button("🎂 10 Years Older", use_container_width=True):
        st.session_state["a_age"] = min(int(st.session_state["b_age"]) + 10, 64)
        st.rerun()

with preset_cols[3]:
    if st.button("🔄 Copy Base to Alt", use_container_width=True):
        st.session_state["a_age"] = st.session_state["b_age"]
        st.session_state["a_sex"] = st.session_state["b_sex"]
        st.session_state["a_bmi"] = st.session_state["b_bmi"]
        st.session_state["a_children"] = st.session_state["b_children"]
        st.session_state["a_smoker"] = st.session_state["b_smoker"]
        st.session_state["a_region"] = st.session_state["b_region"]
        st.rerun()

st.markdown("---")

# Model Choice for Simulation
sim_models = {
    "gradient_boosting": "Gradient Boosting Regressor (Recommended)",
    "random_forest": "Random Forest Regressor",
    "linear_regression": "Linear Regression (Baseline)",
}
selected_sim_model = st.selectbox(
    "Select Model for Simulation Engine:",
    options=list(sim_models.keys()),
    format_func=lambda k: sim_models[k],
)

# Profile Input Columns
col_base, col_alt = st.columns(2)

with col_base:
    st.subheader("🔵 Baseline Profile")
    b_age = st.slider("Age (Baseline)", 1, 100, key="b_age")
    b_sex = st.selectbox("Sex (Baseline)", SEX_CATEGORIES, key="b_sex")
    b_bmi = st.number_input("BMI (Baseline)", 10.0, 70.0, step=0.1, key="b_bmi")
    b_children = st.number_input("Children (Baseline)", 0, 10, step=1, key="b_children")
    b_smoker = st.selectbox("Smoker (Baseline)", SMOKER_CATEGORIES, key="b_smoker")
    b_region = st.selectbox("Region (Baseline)", REGIONS, key="b_region")

with col_alt:
    st.subheader("🟢 Alternative Profile")
    a_age = st.slider("Age (Alternative)", 1, 100, key="a_age")
    a_sex = st.selectbox("Sex (Alternative)", SEX_CATEGORIES, key="a_sex")
    a_bmi = st.number_input("BMI (Alternative)", 10.0, 70.0, step=0.1, key="a_bmi")
    a_children = st.number_input("Children (Alternative)", 0, 10, step=1, key="a_children")
    a_smoker = st.selectbox("Smoker (Alternative)", SMOKER_CATEGORIES, key="a_smoker")
    a_region = st.selectbox("Region (Alternative)", REGIONS, key="a_region")

# Run Comparison
try:
    base_prof, _ = validate_profile(int(b_age), b_sex, float(b_bmi), int(b_children), b_smoker, b_region)
    alt_prof, _ = validate_profile(int(a_age), a_sex, float(a_bmi), int(a_children), a_smoker, a_region)

    comparison = scenario_svc.compare_profiles(base_prof, alt_prof, model_key=selected_sim_model)

    st.markdown("---")
    st.subheader("🔍 Scenario Comparison Results")

    res_c1, res_c2, res_c3, res_c4 = st.columns(4)
    with res_c1:
        render_metric_card("Baseline Charges", f"${comparison.baseline_charges:,.2f}", "Initial Profile")
    with res_c2:
        render_metric_card("Alternative Charges", f"${comparison.alternative_charges:,.2f}", "Hypothetical Profile")
    with res_c3:
        render_metric_card("Absolute Difference", comparison.formatted_delta, f"Direction: {'Higher' if comparison.is_increase else 'Lower'}")
    with res_c4:
        render_metric_card("Relative Change", comparison.formatted_percentage, "Percent difference")

    # Bar chart comparison
    chart_df = pd.DataFrame({
        "Profile": ["Baseline", "Alternative"],
        "Estimated Charges ($ USD)": [comparison.baseline_charges, comparison.alternative_charges],
    })
    fig_comp = px.bar(
        chart_df,
        x="Profile",
        y="Estimated Charges ($ USD)",
        color="Profile",
        color_discrete_sequence=["#2563EB", "#10B981"],
        text_auto="$,.2f",
        title=f"Comparative Estimated Charges ({comparison.model_name})",
        template="plotly_white",
    )
    st.plotly_chart(fig_comp, use_container_width=True)

    # Changed attributes breakdown
    st.subheader("Changed Attributes Breakdown")
    if comparison.changed_features:
        diff_rows = []
        for feat, vals in comparison.changed_features.items():
            diff_rows.append({
                "Attribute": feat.capitalize(),
                "Baseline Value": str(vals["baseline"]),
                "Alternative Value": str(vals["alternative"]),
            })
        st.dataframe(pd.DataFrame(diff_rows), use_container_width=True)
    else:
        st.info("Profiles are identical. Modify any attribute in the Alternative Profile to observe differences.")

    # Export Scenario Report
    scenario_report = {
        "model_used": comparison.model_name,
        "baseline_profile": base_prof.to_dict(),
        "alternative_profile": alt_prof.to_dict(),
        "baseline_charges_usd": comparison.baseline_charges,
        "alternative_charges_usd": comparison.alternative_charges,
        "absolute_delta_usd": comparison.absolute_delta,
        "percentage_delta": comparison.percentage_delta,
        "changed_features": comparison.changed_features,
    }
    st.download_button(
        "📥 Download Scenario Comparison (JSON)",
        data=json.dumps(scenario_report, indent=2),
        file_name="scenario_comparison_report.json",
        mime="application/json",
        use_container_width=True,
    )

except Exception as err:
    st.error(f"Comparison Error: {err}")
