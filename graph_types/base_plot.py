# graph_types/base_plot.py

import matplotlib.pyplot as plt

from themes.themes import (
    get_theme
)

from palettes.palettes import (
    get_palette
)

from axes.linear_axis import (
    apply_linear_axis
)

from axes.log_axis import (
    apply_log_axis
)


class BasePlot:

    def __init__(
        self,
        dataframe,
        settings
    ):

        self.df = dataframe
        self.settings = settings

        self.theme = get_theme(
            settings.figure.theme
        )

        self.palette = get_palette(
            settings.figure.palette,
            len(dataframe.columns)
        )

        self.fig = None
        self.ax = None

    # ==========================================
    # Figure
    # ==========================================

    def create_figure(self):

        self.fig, self.ax = plt.subplots(

            figsize=(

                self.settings.figure.width,

                self.settings.figure.height

            )

        )

    # ==========================================
    # Theme
    # ==========================================

    def apply_theme(self):

        self.ax.grid(
            self.theme.show_grid
        )

        self.ax.spines["top"].set_visible(
            False
        )

        self.ax.spines["right"].set_visible(
            False
        )

        self.ax.spines["left"].set_linewidth(
            self.theme.axis_linewidth
        )

        self.ax.spines["bottom"].set_linewidth(
            self.theme.axis_linewidth
        )

        self.ax.tick_params(

            axis="both",

            which="major",

            direction=self.settings.axis.tick_direction,

            length=self.settings.axis.major_tick_length,

            width=self.settings.axis.major_tick_width,

            labelsize=self.theme.tick_size

        )

        self.ax.tick_params(

            axis="both",

            which="minor",

            direction=self.settings.axis.tick_direction,

            length=self.settings.axis.minor_tick_length,

            width=self.settings.axis.minor_tick_width

        )

        if (

            self.settings.axis.scale

            ==

            "Linear"

        ):

            apply_linear_axis(

                self.ax,

                self.settings.axis

            )

        else:

            apply_log_axis(

                self.ax,

                self.settings.axis

            )

    # ==========================================
    # Labels
    # ==========================================

    def apply_labels(self):

        self.fig.suptitle(

            self.settings.figure.title,

            fontsize=self.theme.title_size,

            y=0.98

        )

        self.ax.set_xlabel(

            self.settings.figure.x_label,

            fontsize=self.theme.label_size

        )

        self.ax.set_ylabel(

            self.settings.figure.y_label,

            fontsize=self.theme.label_size

        )
    # ==========================================
    # Finalize
    # ==========================================

    def finalize(self):

        self.apply_theme()

        self.apply_labels()

        self.fig.tight_layout(
            rect=[0, 0, 1, 0.95]
        )

        return (

            self.fig,

            self.ax

        )