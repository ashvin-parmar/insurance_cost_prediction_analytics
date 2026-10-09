"""Streamlit UI styling definitions and layout helpers."""

import streamlit as st


def apply_custom_css():
    """Injects refined CSS styling for clean academic dashboard presentation."""
    custom_css = """
    <style>
    /* Global Typography */
    .main {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Metric Cards */
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-bottom: 12px;
    }
    .metric-card-title {
        font-size: 0.875rem;
        color: #6B7280;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .metric-card-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: #111827;
    }
    .metric-card-subtitle {
        font-size: 0.75rem;
        color: #9CA3AF;
        margin-top: 4px;
    }

    /* Result Banner */
    .result-banner {
        background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%);
        color: #FFFFFF;
        border-radius: 10px;
        padding: 24px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .result-banner h3 {
        color: #E0E7FF;
        font-size: 1rem;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .result-banner h1 {
        color: #FFFFFF;
        font-size: 2.75rem;
        font-weight: 800;
        margin: 0;
    }

    /* Disclaimer Box */
    .disclaimer-box {
        background-color: #FEF3C7;
        border-left: 4px solid #F59E0B;
        color: #92400E;
        padding: 12px 16px;
        border-radius: 4px;
        font-size: 0.85rem;
        margin: 16px 0;
        line-height: 1.4;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
