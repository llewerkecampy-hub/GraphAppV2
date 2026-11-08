# tests/test_ui_graph.py

import streamlit as st
import pandas as pd

from ui.sidebar import (
    build_sidebar
)

from core.graph_builder import (
    build_graph
)

settings = build_sidebar(st)

df = pd.DataFrame(
    {
        "Control":[10,11,12],
        "MutA":[20,21,22]
    }
)

fig, ax = build_graph(
    df,
    settings
)

st.pyplot(fig)