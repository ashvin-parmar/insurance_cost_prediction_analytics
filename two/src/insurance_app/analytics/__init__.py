"""Analytics, statistics, and visualization module."""

from .charts import (
    plot_charges_by_category,
    plot_charges_distribution,
    plot_correlation_heatmap,
    plot_feature_distribution,
    plot_scatter,
)
from .statistics import (
    compute_category_breakdowns,
    compute_correlation_matrix,
    compute_group_charges_summary,
    compute_numeric_summary,
)

__all__ = [
    "compute_numeric_summary",
    "compute_category_breakdowns",
    "compute_group_charges_summary",
    "compute_correlation_matrix",
    "plot_charges_distribution",
    "plot_feature_distribution",
    "plot_charges_by_category",
    "plot_scatter",
    "plot_correlation_heatmap",
]
