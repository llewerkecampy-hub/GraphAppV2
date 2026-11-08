# graph_types/violin_plot.py

import seaborn as sns

from graph_types.base_plot import (
    BasePlot
)


class ViolinPlot(BasePlot):

    def build(self):

        self.create_figure()

        sns.violinplot(
            data=self.df,
            palette=self.palette,
            linewidth=2,
            ax=self.ax
        )

        return self.finalize()