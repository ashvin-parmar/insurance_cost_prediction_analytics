"""Interactive visualization builders using Plotly Express and Graph Objects.

Pure plotting functions: no Streamlit imports here to ensure modularity and testability.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from insurance_app.features.schema import TARGET_COLUMN

# Clean theme palette
COLOR_SEQUENCE = ["#2563EB", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6"]


def plot_charges_distribution(df: pd.DataFrame, nbins: int = 30) -> go.Figure:
    """Builds an interactive histogram of insurance charges with median annotation."""
    fig = px.histogram(
        df,
        x=TARGET_COLUMN,
        nbins=nbins,
        title="Distribution of Medical Insurance Charges (Target)",
        labels={TARGET_COLUMN: "Insurance Charges ($ USD)"},
        marginal="box",
        color_discrete_sequence=["#2563EB"],
    )
    median_val = df[TARGET_COLUMN].median()
    fig.add_vline(
        x=median_val,
        line_dash="dash",
        line_color="#EF4444",
        annotation_text=f"Median: ${median_val:,.2f}",
        annotation_position="top right",
    )
    fig.update_layout(
        xaxis_title="Insurance Charges ($ USD)",
        yaxis_title="Count of Individuals",
        template="plotly_white",
    )
    return fig


def plot_feature_distribution(df: pd.DataFrame, feature: str, nbins: int = 25) -> go.Figure:
    """Builds a distribution histogram for continuous features (age or bmi)."""
    fig = px.histogram(
        df,
        x=feature,
        nbins=nbins,
        title=f"Distribution of {feature.upper()}",
        labels={feature: feature.capitalize()},
        marginal="box",
        color_discrete_sequence=["#10B981"],
    )
    fig.update_layout(
        xaxis_title=feature.capitalize(),
        yaxis_title="Count of Individuals",
        template="plotly_white",
    )
    return fig


def plot_charges_by_category(df: pd.DataFrame, category_col: str) -> go.Figure:
    """Builds a box plot of insurance charges grouped by a categorical attribute."""
    fig = px.box(
        df,
        x=category_col,
        y=TARGET_COLUMN,
        color=category_col,
        title=f"Medical Insurance Charges by {category_col.capitalize()}",
        labels={
            category_col: category_col.capitalize(),
            TARGET_COLUMN: "Charges ($ USD)",
        },
        points="outliers",
        color_discrete_sequence=COLOR_SEQUENCE,
    )
    fig.update_layout(
        xaxis_title=category_col.capitalize(),
        yaxis_title="Charges ($ USD)",
        showlegend=False,
        template="plotly_white",
    )
    return fig


def plot_scatter(
    df: pd.DataFrame,
    x_col: str,
    y_col: str = TARGET_COLUMN,
    color_col: Optional[str] = "smoker",
) -> go.Figure:
    """Builds a scatter plot examining relationship between continuous feature and charges."""
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        title=f"{x_col.upper()} vs {y_col.capitalize()} (Stratified by {color_col.capitalize() if color_col else 'None'})",
        labels={
            x_col: x_col.capitalize(),
            y_col: f"{y_col.capitalize()} ($ USD)",
            color_col: color_col.capitalize() if color_col else "",
        },
        opacity=0.75,
        color_discrete_sequence=["#2563EB", "#EF4444", "#10B981"],
    )
    fig.update_layout(
        xaxis_title=x_col.capitalize(),
        yaxis_title=f"{y_col.capitalize()} ($ USD)",
        template="plotly_white",
    )
    return fig


def plot_correlation_heatmap(corr_matrix: pd.DataFrame) -> go.Figure:
    """Builds an annotated correlation heatmap for numerical attributes."""
    fig = px.imshow(
        corr_matrix,
        text_auto=".2f",
        aspect="auto",
        title="Pearson Correlation Heatmap (Numeric Attributes & Charges)",
        color_continuous_scale="RdBu_r",
        zmin=-1.0,
        zmax=1.0,
    )
    fig.update_layout(template="plotly_white")
    return fig
