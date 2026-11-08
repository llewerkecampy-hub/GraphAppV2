# axes/linear_axis.py

import numpy as np

from matplotlib.ticker import (
    AutoMinorLocator,
    ScalarFormatter
)


# =====================================================
# Tick Formatting
# =====================================================

def apply_tick_format(
    ax,
    tick_format
):

    if tick_format == "Plain Numbers":

        formatter = ScalarFormatter(
            useMathText=False
        )

        formatter.set_scientific(
            False
        )

        ax.yaxis.set_major_formatter(
            formatter
        )

    elif tick_format == "Scientific":

        ax.ticklabel_format(
            axis="y",
            style="scientific",
            scilimits=(0, 0)
        )

    elif tick_format == "10^n":

        ax.ticklabel_format(
            axis="y",
            style="scientific",
            scilimits=(0, 0)
        )


# =====================================================
# Manual Ticks
# =====================================================

def apply_major_ticks(
    ax,
    y_min,
    y_max,
    step
):

    ticks = np.arange(
        y_min,
        y_max + step,
        step
    )

    if len(ticks) > 25:

        ticks = np.linspace(
            y_min,
            y_max,
            10
        )

    if len(ticks) > 25:

        ticks = np.linspace(
            y_min,
            y_max,
            10
        )

    ax.set_yticks(
        ticks
    )


# =====================================================
# Minor Ticks
# =====================================================

def apply_minor_ticks(
    ax,
    divisions
):

    ax.yaxis.set_minor_locator(
        AutoMinorLocator(
            divisions
        )
    )


# =====================================================
# Linear Axis
# =====================================================

def apply_linear_axis(
    ax,
    axis_settings
):

    ax.set_yscale(
        "linear"
    )

    apply_tick_format(
        ax,
        axis_settings.tick_format
    )

    if not axis_settings.auto_scale:

        ax.set_ylim(

            axis_settings.y_min,

            axis_settings.y_max

        )

        apply_major_ticks(

            ax,

            axis_settings.y_min,

            axis_settings.y_max,

            axis_settings.major_tick_step

        )

    if axis_settings.show_minor_ticks:

        apply_minor_ticks(

            ax,

            axis_settings.minor_divisions

        )