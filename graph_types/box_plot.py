# graph_types/box_plot.py

import seaborn as sns

from graph_types.base_plot import (
    BasePlot
)


class BoxPlot(BasePlot):

    def build(self):

        self.create_figure()

        sns.boxplot(
            data=self.df,
            palette=self.palette,
            linewidth=2,
            ax=self.ax
        )

        return self.finalize()