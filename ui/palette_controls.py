# ui/palette_controls.py

from palettes.palettes import (
    available_palettes
)


def build_palette_settings(
    st,
    settings
):

    st.sidebar.header(
        "Palette"
    )

    palettes = (
        available_palettes()
    )

    current_index = 0

    if settings.figure.palette in palettes:

        current_index = palettes.index(
            settings.figure.palette
        )

    settings.figure.palette = (

        st.sidebar.selectbox(

            "Palette",

            palettes,

            index=current_index

        )

    )

    return settings