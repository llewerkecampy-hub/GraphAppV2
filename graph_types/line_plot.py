# graph_types/line_plot.py

import numpy as np

from graph_types.base_plot import (
    BasePlot
)

from core.data_manager import (
    get_xy_data,
    summarize_xy_data
)


class LinePlot(BasePlot):

    def build(self):

        self.create_figure()

        xy_data = get_xy_data(
            self.df
        )

        summaries = summarize_xy_data(
            xy_data
        )

        x = np.array(
            xy_data["x_values"]
        )

        for i, (condition, stats) in enumerate(
            summaries.items()
        ):

            mean = stats["mean"]

            if (
                self.settings.statistics.error_type
                ==
                "SD"
            ):

                replicates = np.array(

                    xy_data[
                        "conditions"
                    ][
                        condition
                    ]

                )

                error = np.std(
                    replicates,
                    axis=0,
                    ddof=1
                )

            else:

                error = stats["sem"]

            color = self.palette[i]

            # Mean line

            self.ax.errorbar(
                x,
                mean,
                yerr=error,
                color=color,
                linewidth=2.5,
                marker="o",
                capsize=4,
                label=condition
            )

        self.ax.legend()

        print("Y tick labels:")

        for label in self.ax.get_yticklabels():

            print(repr(label.get_text()))

        return self.finalize()