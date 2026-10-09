import sys
from pathlib import Path

# Ensure src/ is on sys.path for direct execution / cloud platforms
src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from insurance_app.features.schema import (
    INPUT_BOUNDS,
    REGIONS,
    SEX_CATEGORIES,
    SMOKER_CATEGORIES,
    validate_profile,
)
from insurance_app.services.prediction_service import PredictionService
from insurance_app.ui.components import (
    render_disclaimer,
    render_metric_card,
    render_profile_summary,
)
from insurance_app.ui.styling import apply_custom_css

apply_custom_css()

st.title("🎯 Module B: Interactive Insurance Cost Prediction")
st.markdown("Provide individual demographic and lifestyle attributes to estimate expected medical charges.")

service = PredictionService()

# Check model availability
if not service.registry.are_models_available():
    st.warning("⚠️ Machine learning models have not been trained yet.")
    st.info("Please train the models by running: `python scripts/train_models.py` in your terminal.")

# Input Form
with st.form("prediction_form"):
    st.subheader("1. Enter Patient Profile")
    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.slider(
            "Age (years)",
            min_value=INPUT_BOUNDS["age"]["min"],
            max_value=INPUT_BOUNDS["age"]["max"],
            value=INPUT_BOUNDS["age"]["default"],
            help="Beneficiary age in years.",
        )
        sex = st.selectbox(
            "Sex",
            options=SEX_CATEGORIES,
            index=1,
            format_func=lambda s: s.capitalize(),
        )

    with c2:
        bmi = st.number_input(
            "Body Mass Index (BMI)",
            min_value=float(INPUT_BOUNDS["bmi"]["min"]),
            max_value=float(INPUT_BOUNDS["bmi"]["max"]),
            value=float(INPUT_BOUNDS["bmi"]["default"]),
            step=0.1,
            format="%.1f",
            help="Normal: 18.5–24.9 | Overweight: 25.0–29.9 | Obese: 30.0+",
        )
        children = st.number_input(
            "Dependents / Children",
            min_value=INPUT_BOUNDS["children"]["min"],
            max_value=INPUT_BOUNDS["children"]["max"],
            value=INPUT_BOUNDS["children"]["default"],
            step=1,
            help="Number of dependent children covered.",
        )

    with c3:
        smoker = st.selectbox(
            "Smoking Status",
            options=SMOKER_CATEGORIES,
            index=0,
            format_func=lambda s: "Non-Smoker (No)" if s == "no" else "Smoker (Yes)",
            help="Tobacco smoker status.",
        )
        region = st.selectbox(
            "Residential Region",
            options=REGIONS,
            index=3,
            format_func=lambda r: r.capitalize(),
            help="US Geographic territory.",
        )

    st.subheader("2. Select Predictive Model")
    model_options = {
        "gradient_boosting": "Gradient Boosting Regressor (Recommended)",
        "random_forest": "Random Forest Regressor",
        "linear_regression": "Linear Regression (Baseline)",
    }
    selected_model_key = st.selectbox(
        "Choose Primary Model:",
        options=list(model_options.keys()),
        format_func=lambda k: model_options[k],
    )

    submitted = st.form_submit_button("⚡ Predict Insurance Charges", use_container_width=True)

if submitted:
    try:
        profile, warnings = validate_profile(
            age=int(age),
            sex=sex,
            bmi=float(bmi),
            children=int(children),
            smoker=smoker,
            region=region,
        )

        for w in warnings:
            st.warning(f"⚠️ {w}")

        # Run Primary Prediction
        result = service.predict(profile, model_key=selected_model_key, warnings=warnings)

        # Result Display Banner
        st.markdown(
            f"""
            <div class="result-banner">
                <h3>Estimated Annual Charges ({result.model_name})</h3>
                <h1>{result.formatted_charges}</h1>
                <p style="margin-top: 8px; color: #E0E7FF; font-size: 0.9rem;">Currency: USD ($)</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Profile Summary
        st.subheader("Profile Confirmation")
        render_profile_summary(profile)

        # BMI Category helper
        bmi_val = profile.bmi
        if bmi_val < 18.5:
            bmi_cat = "Underweight (< 18.5)"
        elif bmi_val < 25.0:
            bmi_cat = "Normal Weight (18.5–24.9)"
        elif bmi_val < 30.0:
            bmi_cat = "Overweight (25.0–29.9)"
        else:
            bmi_cat = "Obese (30.0+)"
        st.info(f"**Health Indicator Note:** Body Mass Index of {bmi_val:.1f} classifies as **{bmi_cat}**.")

        # Benchmark Comparisons
        st.markdown("---")
        st.subheader("3. Benchmark Against Historical Dataset")
        DATASET_MEAN = 13270.42
        DATASET_MEDIAN = 9382.03

        bench_col1, bench_col2, bench_col3 = st.columns(3)
        with bench_col1:
            render_metric_card("Estimated Charge", result.formatted_charges, f"Model: {result.model_name}")
        with bench_col2:
            diff_mean = result.estimated_charges_usd - DATASET_MEAN
            diff_pct = (diff_mean / DATASET_MEAN) * 100.0
            render_metric_card(
                "vs. Population Mean ($13,270)",
                f"{diff_pct:+.1f}%",
                f"{'+' if diff_mean > 0 else ''}${diff_mean:,.2f}",
            )
        with bench_col3:
            diff_med = result.estimated_charges_usd - DATASET_MEDIAN
            med_pct = (diff_med / DATASET_MEDIAN) * 100.0
            render_metric_card(
                "vs. Population Median ($9,382)",
                f"{med_pct:+.1f}%",
                f"{'+' if diff_med > 0 else ''}${diff_med:,.2f}",
            )

        # Multi-Model Estimate Comparison for this exact profile
        st.markdown("---")
        st.subheader("4. Multi-Model Estimate Comparison for this Profile")
        all_estimates = []
        for m_key, m_name in [
            ("gradient_boosting", "Gradient Boosting"),
            ("random_forest", "Random Forest"),
            ("linear_regression", "Linear Regression"),
        ]:
            try:
                res_m = service.predict(profile, model_key=m_key)
                all_estimates.append({
                    "Algorithm": m_name,
                    "Estimated Charges ($ USD)": res_m.estimated_charges_usd,
                    "Selected": "Yes" if m_key == selected_model_key else "No",
                })
            except Exception:
                pass

        if all_estimates:
            est_df = pd.DataFrame(all_estimates)
            fig_est = px.bar(
                est_df,
                x="Algorithm",
                y="Estimated Charges ($ USD)",
                color="Algorithm",
                text_auto="$,.2f",
                title="Model Estimates for Current Profile",
                template="plotly_white",
            )
            st.plotly_chart(fig_est, use_container_width=True)

        # Download Prediction Card
        report_data = {
            "profile": profile.to_dict(),
            "model_used": result.model_name,
            "estimated_charges_usd": result.estimated_charges_usd,
            "all_model_estimates": {row["Algorithm"]: row["Estimated Charges ($ USD)"] for row in all_estimates},
        }
        st.download_button(
            "📥 Download Prediction Summary (JSON)",
            data=json.dumps(report_data, indent=2),
            file_name="insurance_prediction_summary.json",
            mime="application/json",
            use_container_width=True,
        )

        render_disclaimer()

    except Exception as err:
        st.error(f"Prediction Error: {err}")
