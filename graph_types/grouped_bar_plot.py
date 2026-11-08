# graph_types/grouped_bar_plot.py

import numpy as np

from graph_types.base_plot import (
    BasePlot
)

from core.data_manager import (
    calculate_means,
    determine_error_values
)


class GroupedBarPlot(BasePlot):

    def build(self):

        self.create_figure()

        means = calculate_means(
            self.df
        )

        errors = determine_error_values(
            self.df,
            self.settings.statistics.error_type
        )

        n_groups = len(
            self.df.columns
        )

        width = 0.8 / n_groups

        x = np.array([0])

        for i, column in enumerate(
            self.df.columns
        ):

            self.ax.bar(

                x + i * width,

                means[column],

                yerr=errors[column],

                width=width,

                color=self.palette[i],

                edgecolor="black",

                linewidth=1.5,

                capsize=4,

                label=column

            )

        center = (
            x + (n_groups * width) / 2
        )

        self.ax.set_xticks(
            center
        )

        self.ax.set_xticklabels(
            ["Groups"]
        )

        self.ax.legend()

        return self.finalize()
