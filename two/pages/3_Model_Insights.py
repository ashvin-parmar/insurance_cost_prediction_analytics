"""Page 3: Model Evaluation Insights, Performance Comparisons & Residual Analysis."""

import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from insurance_app.ml.registry import ModelRegistry
from insurance_app.ui.components import render_metric_card
from insurance_app.ui.styling import apply_custom_css

apply_custom_css()

st.title("📈 Module C: Model Insights & Performance Comparisons")
st.caption("Quantitative comparison of regression algorithms evaluated on the held-out test split (20%, seed 42).")

registry = ModelRegistry()

if not registry.are_models_available():
    st.warning("⚠️ Models have not been trained yet.")
    st.info("Execute: `python scripts/train_models.py` in your terminal to generate evaluation artifacts.")
    st.stop()

metrics_data = registry.load_metrics()
metadata = registry.load_metadata()
eval_cache = registry.load_evaluation_cache()

# 1. Comparison Table
st.subheader("1. Comprehensive Model Performance Benchmark")

rows = []
for key, data in metrics_data.items():
    m = data["metrics"]
    rows.append({
        "Model Key": key,
        "Algorithm": data["name"],
        "MAE (USD $)": f"${m['mae']:,.2f}",
        "RMSE (USD $)": f"${m['rmse']:,.2f}",
        "R² Score": f"{m['r2']:.4f}",
        "_mae_raw": m["mae"],
        "_rmse_raw": m["rmse"],
        "_r2_raw": m["r2"],
    })

perf_df = pd.DataFrame(rows)
st.dataframe(perf_df[["Algorithm", "MAE (USD $)", "RMSE (USD $)", "R² Score"]], use_container_width=True)

# Best Model Card
best_model_name = metadata.get("best_model_name", "Gradient Boosting Regressor")
best_key = metadata.get("best_model_key", "gradient_boosting")
best_mae = metrics_data[best_key]["metrics"]["mae"]
best_r2 = metrics_data[best_key]["metrics"]["r2"]

c1, c2, c3 = st.columns(3)
with c1:
    render_metric_card("Top Ranked Model", best_model_name, "Lowest held-out validation MAE")
with c2:
    render_metric_card("Optimal Test MAE", f"${best_mae:,.2f}", "Average absolute error margin")
with c3:
    render_metric_card("Optimal R² Score", f"{best_r2:.4f}", f"Explains {best_r2*100:.1f}% of variance")

st.markdown("---")

# 2. Comparative Metric Charts
st.subheader("2. Metric Visual Comparison")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig_mae = px.bar(
        perf_df,
        x="Algorithm",
        y="_mae_raw",
        color="Algorithm",
        title="Mean Absolute Error (Lower is Better)",
        labels={"_mae_raw": "MAE ($ USD)", "Algorithm": "Model"},
        text_auto=".2f",
        template="plotly_white",
    )
    st.plotly_chart(fig_mae, use_container_width=True)

with chart_col2:
    fig_r2 = px.bar(
        perf_df,
        x="Algorithm",
        y="_r2_raw",
        color="Algorithm",
        title="R² Score (Higher is Better)",
        labels={"_r2_raw": "R² Score", "Algorithm": "Model"},
        text_auto=".4f",
        template="plotly_white",
    )
    st.plotly_chart(fig_r2, use_container_width=True)

st.markdown("---")

# 3. Actual vs. Predicted & Residual Analysis
st.subheader("3. Actual vs. Predicted & Residual Diagnostics")
chosen_eval_model = st.selectbox(
    "Select Model for Diagnostic Plots:",
    options=list(metrics_data.keys()),
    format_func=lambda k: metrics_data[k]["name"],
)

if chosen_eval_model in eval_cache:
    cache = eval_cache[chosen_eval_model]
    y_true = cache["y_true"]
    y_pred = cache["y_pred"]
    residuals = cache["residuals"]

    diag_df = pd.DataFrame({"Actual": y_true, "Predicted": y_pred, "Residual": residuals})

    p_col1, p_col2 = st.columns(2)

    with p_col1:
        fig_scatter = px.scatter(
            diag_df,
            x="Actual",
            y="Predicted",
            opacity=0.6,
            title="Actual vs. Predicted Charges",
            labels={"Actual": "Actual Charges ($ USD)", "Predicted": "Predicted ($ USD)"},
            template="plotly_white",
        )
        max_limit = max(max(y_true), max(y_pred))
        fig_scatter.add_trace(
            go.Scatter(
                x=[0, max_limit],
                y=[0, max_limit],
                mode="lines",
                name="Perfect Identity (y=x)",
                line=dict(dash="dash", color="red"),
            )
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    with p_col2:
        fig_res = px.scatter(
            diag_df,
            x="Predicted",
            y="Residual",
            opacity=0.6,
            title="Residuals vs. Predicted Charges",
            labels={"Predicted": "Predicted ($ USD)", "Residual": "Residual (Actual - Predicted)"},
            template="plotly_white",
        )
        fig_res.add_hline(y=0, line_dash="dash", line_color="red")
        st.plotly_chart(fig_res, use_container_width=True)

    # Residual Distribution Histogram
    fig_res_dist = px.histogram(
        diag_df,
        x="Residual",
        nbins=30,
        title="Distribution of Model Residuals (Errors)",
        labels={"Residual": "Residual Error ($ USD)"},
        color_discrete_sequence=["#6366F1"],
        marginal="box",
        template="plotly_white",
    )
    fig_res_dist.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Zero Error Line")
    st.plotly_chart(fig_res_dist, use_container_width=True)

st.markdown("---")

# 4. Feature Explanations / Importance
st.subheader("4. Feature Importance & Coefficients")
feat_imp = metrics_data[chosen_eval_model]["feature_importance"]
if feat_imp:
    imp_df = pd.DataFrame(list(feat_imp.items()), columns=["Feature", "Value"]).sort_values("Value", ascending=True)
    fig_imp = px.bar(
        imp_df,
        x="Value",
        y="Feature",
        orientation="h",
        title=f"Relative Feature Contributions ({metrics_data[chosen_eval_model]['name']})",
        labels={"Value": "Relative Importance / Coefficient", "Feature": "Input Feature"},
        template="plotly_white",
    )
    st.plotly_chart(fig_imp, use_container_width=True)

st.markdown("---")

# 5. Export Benchmark Report
st.subheader("5. Export Model Performance Benchmark")
st.download_button(
    "📥 Download Complete Benchmark Report (JSON)",
    data=json.dumps(metrics_data, indent=2),
    file_name="model_benchmark_report.json",
    mime="application/json",
    use_container_width=True,
)
