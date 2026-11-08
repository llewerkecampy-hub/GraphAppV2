from core.settings import (
    get_default_settings
)

from ui.figure_controls import (
    build_figure_settings
)

from ui.statistics_controls import (
    build_statistics_settings
)

from ui.axis_controls import (
    build_axis_settings
)

from ui.export_controls import (
    build_export_settings
)

from ui.theme_controls import (
    build_theme_settings
)

from ui.palette_controls import (
    build_palette_settings
)


def build_sidebar(st):

    settings = (
        get_default_settings()
    )

    settings = (
        build_figure_settings(
            st,
            settings
        )
    )

    settings = (
        build_theme_settings(
            st,
            settings
        )
    )

    settings = (
        build_palette_settings(
            st,
            settings
        )
    )

    settings = (
        build_statistics_settings(
            st,
            settings
        )
    )

    settings = (
        build_axis_settings(
            st,
            settings
        )
    )

    settings = (
        build_export_settings(
            st,
            settings
        )
    )

    return settings