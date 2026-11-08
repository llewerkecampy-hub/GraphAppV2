# tests/test_sidebar_app.py

import streamlit as st

from ui.sidebar import (
    build_sidebar
)

settings = build_sidebar(
    st
)

st.write(settings)