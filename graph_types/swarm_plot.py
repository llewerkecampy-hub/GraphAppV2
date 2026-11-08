# graph_types/swarm_plot.py

import seaborn as sns

from graph_types.base_plot import (
    BasePlot
)


class SwarmPlot(BasePlot):

    def build(self):

        self.create_figure()

        sns.swarmplot(
            data=self.df,
            palette=self.palette,
            size=7,
            ax=self.ax
        )

        return self.finalize()