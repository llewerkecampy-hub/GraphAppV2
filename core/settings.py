# core/settings.py

from core.models import (
    AxisSettings,
    FigureSettings,
    StatisticsSettings,
    ExportSettings,
    AppSettings
)


# =====================================================
# Default Settings Factory
# =====================================================

def get_default_settings():

    axis_settings = AxisSettings(

        scale="Linear",

        tick_format="Plain Numbers",

        auto_scale=True,

        major_tick_step=10.0,

        show_minor_ticks=True,

        minor_divisions=2,

        major_tick_length=8,

        major_tick_width=2,

        minor_tick_length=4,

        minor_tick_width=1
    )

    figure_settings = FigureSettings(

        graph_type="Bar",

        width=8,

        height=6,

        palette="deep",

        theme="Default",

        title="",

        x_label="Condition",

        y_label="Value",

        show_points=True
    )

    statistics_settings = StatisticsSettings(

        method="Auto",

        error_type="SEM",

        alpha=0.05
    )

    export_settings = ExportSettings(

        file_format="png",

        dpi=600,

        transparent=False,

        filename="Figure1"
    )

    return AppSettings(

        figure=figure_settings,

        axis=axis_settings,

        statistics=statistics_settings,

        export=export_settings
    )