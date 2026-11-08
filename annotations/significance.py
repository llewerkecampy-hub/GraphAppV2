# annotations/significance.py

from annotations.bracket_layout import (
    build_bracket_layout
)


# =====================================================
# Group Position Mapping
# =====================================================

def create_group_positions(
    group_names
):

    return {

        group: index

        for index, group

        in enumerate(group_names)

    }


# =====================================================
# Comparison Filtering
# =====================================================

def filter_comparisons(
    comparisons,
    selected_pairs
):

    if not selected_pairs:

        return comparisons

    filtered = []

    for comparison in comparisons:

        pair = (

            comparison.group1,
            comparison.group2

        )

        reverse_pair = (

            comparison.group2,
            comparison.group1

        )

        if (

            pair in selected_pairs

            or

            reverse_pair in selected_pairs

        ):

            filtered.append(
                comparison
            )

    return filtered


# =====================================================
# Build Annotation Layout
# =====================================================

def build_annotations(
    comparisons,
    group_names,
    y_max,
    selected_pairs=None
):

    comparisons = filter_comparisons(
        comparisons,
        selected_pairs
    )

    positions = (
        create_group_positions(
            group_names
        )
    )

    starting_height = (
        y_max * 1.10
    )

    step = (
        y_max * 0.10
    )

    return build_bracket_layout(

        comparisons=comparisons,

        group_positions=positions,

        starting_height=starting_height,

        height_step=step

    )