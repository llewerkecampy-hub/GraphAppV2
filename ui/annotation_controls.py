# ui/annotation_controls.py

from core.annotation_engine import (
    available_comparison_labels,
    parse_selected_labels
)


def build_annotation_controls(
    st,
    statistics_result
):

    if (

        statistics_result is None

        or

        len(
            statistics_result.comparisons
        ) == 0

    ):

        return None

    st.sidebar.header(
        "Comparisons"
    )

    labels = (
        available_comparison_labels(
            statistics_result
        )
    )

    selected_labels = (

        st.sidebar.multiselect(

            "Display Comparisons",

            labels,

            default=labels

        )

    )

    return parse_selected_labels(
        selected_labels
    )