# core/graph_builder.py

from graph_types.bar_plot import (
    BarPlot
)

from graph_types.box_plot import (
    BoxPlot
)

from graph_types.violin_plot import (
    ViolinPlot
)

from graph_types.dot_plot import (
    DotPlot
)

from graph_types.strip_plot import (
    StripPlot
)

from graph_types.swarm_plot import (
    SwarmPlot
)

from graph_types.histogram_plot import (
    HistogramPlot
)

from graph_types.line_plot import (
    LinePlot
)

from graph_types.scatter_plot import (
    ScatterPlot
)

from graph_types.grouped_bar_plot import (
    GroupedBarPlot
)

from graph_types.heatmap_plot import (
    HeatmapPlot
)

from core.annotation_engine import (
    apply_annotations
)

# =====================================================
# Registry
# =====================================================

GRAPH_REGISTRY = {

    "Bar":
    BarPlot,

    "Box":
    BoxPlot,

    "Violin":
    ViolinPlot,

    "Dot":
    DotPlot,

    "Strip":
    StripPlot,

    "Swarm":
    SwarmPlot,

    "Histogram":
    HistogramPlot,

    "Line":
    LinePlot,

    "Scatter":
    ScatterPlot,

    "Grouped Bar":
    GroupedBarPlot,

    "Heatmap":
    HeatmapPlot
}

def graph_supports_annotations(
    graph_type
):

    return (
        graph_type
        in
        ANNOTATION_GRAPHS
    )

# =====================================================
# Helper
# =====================================================

def available_graphs():

    return list(
        GRAPH_REGISTRY.keys()
    )



# =====================================================
# Graphs Supporting Statistical Annotations
# =====================================================

ANNOTATION_GRAPHS = {

    "Bar",

    "Box",

    "Violin",

    "Dot",

    "Strip",

    "Swarm",

    "Grouped Bar"

}


# =====================================================
# Graph Builder
# =====================================================

def build_graph(
    dataframe,
    settings,
    statistics_result=None,
    selected_pairs=None
):

    graph_type = (
        settings.figure.graph_type
    )

    if graph_type not in GRAPH_REGISTRY:

        raise ValueError(
            f"Unsupported graph type: "
            f"{graph_type}"
        )

    graph_class = (
        GRAPH_REGISTRY[
            graph_type
        ]
    )

    graph = graph_class(
        dataframe,
        settings
    )

    fig, ax = graph.build()

    # =====================================
    # Statistical Annotations
    # =====================================

    should_annotate = (

        graph_type
        in
        ANNOTATION_GRAPHS

    )

    if (

        should_annotate

        and

        statistics_result is not None

        and

        len(
            statistics_result.comparisons
        ) > 0

    ):

        apply_annotations(

            ax,

            statistics_result,

            list(
                dataframe.columns
            ),

            y_max=ax.get_ylim()[1],

            axis_settings=settings.axis,

            selected_pairs=selected_pairs

        )

    return (
        fig,
        ax
    )