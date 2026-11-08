# app.py

import streamlit as st

from core.data_manager import (
    load_file
)

from core.graph_builder import (
    build_graph
)

from core.statistics_engine import (
    run_statistics,
    get_assumption_report
)

from core.export_manager import (
    get_download_buffer,
    get_mime_type
)

from ui.sidebar import (
    build_sidebar
)

from ui.annotation_controls import (
    build_annotation_controls
)

from ui.data_preview import (
    show_data_preview
)

from ui.statistics_results import (
    show_statistics_results
)

from ui.assumption_results import (
    show_assumption_report
)


# =====================================================
# Page
# =====================================================

st.set_page_config(
    page_title="GraphAppV2",
    layout="wide"
)

st.title(
    "GraphAppV2"
)

st.caption(
    "Scientific Statistics and Figure Builder"
)


# =====================================================
# Data Upload
# =====================================================

uploaded_file = st.sidebar.file_uploader(
    "Upload Data",
    type=[
        "csv",
        "xlsx",
        "xls"
    ]
)

if uploaded_file is None:

    st.info(
        "Upload a CSV or Excel file to begin."
    )

    st.stop()


# =====================================================
# Load Data
# =====================================================

df = load_file(
    uploaded_file
)

show_data_preview(
    st,
    df
)


# =====================================================
# Sidebar
# =====================================================

settings = build_sidebar(
    st
)


# =====================================================
# Statistics
# =====================================================

statistics_result = None

assumption_report = None

if settings.statistics.show_statistics:

    try:

        statistics_result = run_statistics(

            df,

            settings.statistics

        )

        assumption_report = (

            get_assumption_report(

                df,

                settings.statistics

            )

        )

    except ValueError as error:

        st.error(
            str(error)
        )

        st.stop()

    show_statistics_results(

        st,

        statistics_result

    )

    show_assumption_report(

        st,

        assumption_report

    )

# =====================================================
# Annotation Selection
# =====================================================

selected_pairs = None

if (

    settings.statistics.show_statistics

    and

    statistics_result is not None

):

    selected_pairs = (

        build_annotation_controls(

            st,

            statistics_result

        )

    )

# =====================================================
# Build Graph
# =====================================================

fig, ax = build_graph(

    dataframe=df,

    settings=settings,

    statistics_result=statistics_result,

    selected_pairs=selected_pairs

)


# =====================================================
# Display
# =====================================================

st.subheader(
    "Figure"
)

st.pyplot(
    fig
)


# =====================================================
# Export
# =====================================================

st.subheader(
    "Export"
)

export_buffer = (
    get_download_buffer(

        fig,

        settings.export

    )
)

st.download_button(

    label=f"Download {settings.export.file_format.upper()}",

    data=export_buffer,

    file_name=(

        f"{settings.export.filename}."

        f"{settings.export.file_format}"

    ),

    mime=get_mime_type(
        settings.export.file_format
    )
)