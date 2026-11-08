# graph_types/heatmap_plot.py

import seaborn as sns

from graph_types.base_plot import (
    BasePlot
)


class HeatmapPlot(BasePlot):

    def build(self):

        self.create_figure()

        cmap = (
            self.settings.figure.palette
        )

        try:

            sns.heatmap(

                self.df,

                cmap=cmap,

                annot=True,

                fmt=".2f",

                linewidths=0.5,

                ax=self.ax

            )

        except Exception:

            sns.heatmap(

                self.df,

                cmap="viridis",

                annot=True,

                fmt=".2f",

                linewidths=0.5,

                ax=self.ax

            )

        return self.finalize()