# tests/test_settings_flow.py

import streamlit as st

from ui.sidebar import (
    build_sidebar
)

settings = build_sidebar(
    st
)

st.write("Graph Type")

st.write(
    settings.figure.graph_type
)

st.write("Statistics")

st.write(
    settings.statistics.method
)

st.write("Axis")

st.write(
    settings.axis.scale
)

st.write("Export")

st.write(
    settings.export.file_format
)