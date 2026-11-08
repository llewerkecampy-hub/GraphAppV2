from core.models import (
    FigureSettings
)


def build_figure_settings(
    st,
    settings
):

    st.sidebar.header(
        "Figure"
    )

    settings.figure.graph_type = (
        st.sidebar.selectbox(
            "Graph Type",
            [
                "Bar",
                "Box",
                "Violin",

                "Dot",
                "Strip",
                "Swarm",

                "Histogram",

                "Scatter",
                "Line",

                "Grouped Bar",

                "Heatmap"
            ],

            index=0
        )
    )

    settings.figure.width = (
        st.sidebar.slider(
            "Width",
            4,
            20,
            int(
                settings.figure.width
            )
        )
    )

    settings.figure.height = (
        st.sidebar.slider(
            "Height",
            4,
            20,
            int(
                settings.figure.height
            )
        )
    )

    settings.figure.title = (
        st.sidebar.text_input(
            "Title",
            settings.figure.title
        )
    )

    settings.figure.x_label = (
        st.sidebar.text_input(
            "X Label",
            settings.figure.x_label
        )
    )

    settings.figure.y_label = (
        st.sidebar.text_input(
            "Y Label",
            settings.figure.y_label
        )
    )

    return settings