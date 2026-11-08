# graph_types/strip_plot.py

import seaborn as sns

from graph_types.base_plot import (
    BasePlot
)


class StripPlot(BasePlot):

    def build(self):

        self.create_figure()

        sns.stripplot(
            data=self.df,
            palette=self.palette,
            size=7,
            ax=self.ax
        )

        return self.finalize()