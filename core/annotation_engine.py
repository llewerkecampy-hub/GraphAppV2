# core/annotation_engine.py

from annotations.significance import (
    build_annotations
)

from annotations.bracket_layout import (
    required_plot_height
)

from annotations.renderer import (
    render_annotations,
    expand_axis_for_annotations
)

# =====================================================
# Annotation Layout
# =====================================================

def build_annotation_layout(
    statistics_result,
    group_names,
    y_max,
    selected_pairs=None
):

    comparisons = (
        statistics_result.comparisons
    )

    if len(comparisons) == 0:

        return []

    return build_annotations(

        comparisons=comparisons,

        group_names=group_names,

        y_max=y_max,

        selected_pairs=selected_pairs

    )


# =====================================================
# Plot Height Helper
# =====================================================

def get_required_ymax(
    bracket_layout,
    bracket_height
):

    return required_plot_height(

        bracket_layout,

        bracket_height

    )


# =====================================================
# Pair Generation
# =====================================================

def available_comparisons(
    statistics_result
):

    pairs = []

    for comparison in (
        statistics_result.comparisons
    ):

        pairs.append(

            (
                comparison.group1,
                comparison.group2
            )

        )

    return pairs


# =====================================================
# Label Generation
# =====================================================

def available_comparison_labels(
    statistics_result
):

    labels = []

    for comparison in (
        statistics_result.comparisons
    ):

        labels.append(

            f"{comparison.group1} vs "
            f"{comparison.group2}"

        )

    return labels


# =====================================================
# Label Parser
# =====================================================

def parse_selected_labels(
    labels
):

    pairs = []

    for label in labels:

        if " vs " not in label:

            continue

        group1, group2 = (

            label.split(
                " vs "
            )

        )

        pairs.append(

            (
                group1,
                group2
            )

        )

    return pairs


def apply_annotations(
    ax,
    statistics_result,
    group_names,
    y_max,
    axis_settings,
    selected_pairs=None
):

    layout = build_annotation_layout(

        statistics_result,

        group_names,

        y_max,

        selected_pairs

    )

    if not layout:

        return

    bracket_height = y_max * 0.03

    if axis_settings.auto_scale:

        expand_axis_for_annotations(
            ax,
            layout,
            bracket_height
        )

    render_annotations(
        ax,
        layout,
        bracket_height
    )


    render_annotations(

        ax,

        layout,

        bracket_height

    )