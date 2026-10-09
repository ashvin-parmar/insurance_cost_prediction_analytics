"""Reusable UI presentation components for Streamlit."""

from typing import Optional

import streamlit as st
from insurance_app.features.schema import InsuranceProfile


def render_metric_card(title: str, value: str, subtitle: Optional[str] = None):
    """Renders a styled KPI card."""
    sub_html = f'<div class="metric-card-subtitle">{subtitle}</div>' if subtitle else ""
    html = f"""
    <div class="metric-card">
        <div class="metric-card-title">{title}</div>
        <div class="metric-card-value">{value}</div>
        {sub_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_disclaimer():
    """Renders the standard academic non-causal estimation disclaimer."""
    html = """
    <div class="disclaimer-box">
        <strong>Academic & Clinical Disclaimer:</strong> This application generates regression estimates based on historical observational data.
        Predictions represent statistical model approximations and must not be interpreted as official actuarial insurance quotes, financial commitments, or clinical health assessments.
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_profile_summary(profile: InsuranceProfile):
    """Renders an organized summary of input profile attributes."""
    cols = st.columns(6)
    with cols[0]:
        st.caption("Age")
        st.write(f"**{profile.age}** yrs")
    with cols[1]:
        st.caption("Sex")
        st.write(f"**{profile.sex.capitalize()}**")
    with cols[2]:
        st.caption("BMI")
        st.write(f"**{profile.bmi:.1f}**")
    with cols[3]:
        st.caption("Children")
        st.write(f"**{profile.children}**")
    with cols[4]:
        st.caption("Smoker")
        st.write(f"**{profile.smoker.capitalize()}**")
    with cols[5]:
        st.caption("Region")
        st.write(f"**{profile.region.capitalize()}**")
