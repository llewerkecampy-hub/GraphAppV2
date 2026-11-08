# ui/theme_controls.py

from themes.themes import (
    available_themes
)


def build_theme_settings(
    st,
    settings
):

    st.sidebar.header(
        "Theme"
    )

    themes = (
        available_themes()
    )

    current_index = 0

    if settings.figure.theme in themes:

        current_index = themes.index(
            settings.figure.theme
        )

    settings.figure.theme = (

        st.sidebar.selectbox(

            "Theme",

            themes,

            index=current_index

        )

    )

    return settings