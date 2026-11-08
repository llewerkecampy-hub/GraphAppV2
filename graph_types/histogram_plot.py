# graph_types/histogram_plot.py

from graph_types.base_plot import (
    BasePlot
)


class HistogramPlot(BasePlot):

    def build(self):

        self.create_figure()

        for i, column in enumerate(
            self.df.columns
        ):

            values = (
                self.df[column]
                .dropna()
            )

            self.ax.hist(

                values,

                color=self.palette[i],

                alpha=0.5,

                label=column

            )

        self.ax.legend()

        return self.finalize()