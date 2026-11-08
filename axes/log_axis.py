# axes/log_axis.py

import numpy as np

from matplotlib.ticker import (
    LogLocator,
    LogFormatterSciNotation
)


# =====================================================
# Base Helper
# =====================================================

def apply_log_tick_style(
    ax
):

    ax.yaxis.set_major_locator(

        LogLocator(
            base=10
        )

    )

    ax.yaxis.set_major_formatter(

        LogFormatterSciNotation()

    )


# =====================================================
# Log10
# =====================================================

def apply_log10_axis(
    ax,
    axis_settings
):

    ax.set_yscale(
        "log",
        base=10
    )

    apply_log_tick_style(
        ax
    )

    if (

        not axis_settings.auto_scale

        and

        axis_settings.y_min is not None

        and

        axis_settings.y_max is not None

    ):

        ax.set_ylim(

            axis_settings.y_min,

            axis_settings.y_max

        )


# =====================================================
# Log2
# =====================================================

def apply_log2_axis(
    ax,
    axis_settings
):

    ax.set_yscale(
        "log",
        base=2
    )

    if (

        not axis_settings.auto_scale

        and

        axis_settings.y_min is not None

        and

        axis_settings.y_max is not None

    ):

        ax.set_ylim(

            axis_settings.y_min,

            axis_settings.y_max

        )


# =====================================================
# Natural Log
# =====================================================

def apply_ln_axis(
    ax,
    axis_settings
):

    ax.set_yscale(
        "log",
        base=np.e
    )

    if (

        not axis_settings.auto_scale

        and

        axis_settings.y_min is not None

        and

        axis_settings.y_max is not None

    ):

        ax.set_ylim(

            axis_settings.y_min,

            axis_settings.y_max

        )


# =====================================================
# Dispatcher
# =====================================================

def apply_log_axis(
    ax,
    axis_settings
):

    scale = (
        axis_settings.scale
        .strip()
    )

    if scale == "Log10":

        apply_log10_axis(
            ax,
            axis_settings
        )

    elif scale == "Log2":

        apply_log2_axis(
            ax,
            axis_settings
        )

    elif scale == "Natural Log":

        apply_ln_axis(
            ax,
            axis_settings
        )

    else:

        raise ValueError(
            f"Unsupported log scale: {scale}"
        )