# graph_types/bar_plot.py

import numpy as np

from graph_types.base_plot import (
    BasePlot
)

from core.data_manager import (
    calculate_means,
    determine_error_values
)


class BarPlot(BasePlot):

    def build(self):

        self.create_figure()

        means = calculate_means(
            self.df
        )

        errors = determine_error_values(

            self.df,

            self.settings.statistics.error_type

        )

        x = np.arange(
            len(self.df.columns)
        )

        self.ax.bar(

            x,

            means.values,

            yerr=errors.values,

            capsize=8,

            color=self.palette,

            edgecolor="black",

            linewidth=2

        )

        self.ax.set_xticks(x)

        self.ax.set_xticklabels(

            self.df.columns,

            rotation=45,

            ha="right"

        )

        return self.finalize()