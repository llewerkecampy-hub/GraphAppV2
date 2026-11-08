# core/axis_manager.py

import numpy as np

from matplotlib.ticker import (

    AutoMinorLocator,

    LogLocator,

    LogFormatterMathtext,

    FuncFormatter,

    NullFormatter
)

def apply_tick_format(
    ax,
    tick_format
):

    if tick_format == "10^n":

        ax.yaxis.set_major_formatter(
            LogFormatterMathtext()
        )

    elif tick_format == "Scientific":

        ax.yaxis.set_major_formatter(
            FuncFormatter(
                lambda x, pos: f"{x:.0e}"
            )
        )

    elif tick_format == "Plain Numbers":

        ax.yaxis.set_major_formatter(
            FuncFormatter(
                lambda x, pos: f"{x:g}"
            )
        )

def apply_linear_axis(
    ax,
    settings
):

    ax.set_yscale(
        "linear"
    )

    if settings.show_minor_ticks:

        ax.yaxis.set_minor_locator(
            AutoMinorLocator(
                settings.minor_divisions
            )
        )

def apply_log10_axis(
    ax,
    settings
):

    ax.set_yscale(
        "log"
    )

    ax.yaxis.set_major_locator(
        LogLocator(
            base=10
        )
    )

    if settings.show_minor_ticks:

        ax.yaxis.set_minor_locator(
            LogLocator(
                base=10,
                subs=np.arange(2, 10)
            )
        )

        ax.yaxis.set_minor_formatter(
            NullFormatter()
        )

    apply_tick_format(
        ax,
        settings.tick_format
    )

def apply_log2_axis(
    ax,
    settings
):

    ax.set_yscale(
        "log",
        base=2
    )

    ax.yaxis.set_major_locator(
        LogLocator(
            base=2
        )
    )

    apply_tick_format(
        ax,
        settings.tick_format
    )

def apply_ln_axis(
    ax,
    settings
):

    ax.set_yscale(
        "log",
        base=np.e
    )

    ax.yaxis.set_major_locator(
        LogLocator(
            base=np.e
        )
    )

    apply_tick_format(
        ax,
        settings.tick_format
    )

def apply_axis_limits(
    ax,
    settings
):

    if settings.auto_scale:

        return

    ymin = settings.y_min
    ymax = settings.y_max

    if settings.scale != "Linear":

        if ymin is not None:

            ymin = max(
                ymin,
                1e-10
            )

    ax.set_ylim(
        ymin,
        ymax
    )

def validate_axis_data(
    data,
    settings
):

    if settings.scale == "Linear":

        return

    values = np.asarray(
        data
    ).flatten()

    values = values[
        ~np.isnan(values)
    ]

    if np.any(
        values <= 0
    ):

        raise ValueError(
            "Logarithmic axes require all values to be greater than zero."
        )

def apply_axis_settings(
    ax,
    data,
    settings
):

    validate_axis_data(
        data,
        settings
    )

    if settings.scale == "Linear":

        apply_linear_axis(
            ax,
            settings
        )

    elif settings.scale == "Log10":

        apply_log10_axis(
            ax,
            settings
        )

    elif settings.scale == "Log2":

        apply_log2_axis(
            ax,
            settings
        )

    elif settings.scale == "Natural Log":

        apply_ln_axis(
            ax,
            settings
        )

    apply_axis_limits(
        ax,
        settings
    )


