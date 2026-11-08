# graph_types/dot_plot.py

import numpy as np

from graph_types.base_plot import (
    BasePlot
)


class DotPlot(BasePlot):

    def build(self):

        self.create_figure()

        for i, column in enumerate(
            self.df.columns
        ):

            values = (
                self.df[column]
                .dropna()
            )

            self.ax.scatter(

                np.full(
                    len(values),
                    i
                ),

                values,

                color=self.palette[i],

                s=60

            )

        self.ax.set_xticks(
            range(
                len(self.df.columns)
            )
        )

        self.ax.set_xticklabels(
            self.df.columns,
            rotation=45,
            ha="right"
        )

        return self.finalize()