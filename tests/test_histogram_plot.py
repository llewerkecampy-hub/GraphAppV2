import pandas as pd
import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from graph_types.histogram_plot import (
    HistogramPlot
)

df = pd.DataFrame(
    {
        "Control": [
            10,10,10,11,11,11,
            12,12,12,13,13,13
        ],

        "MutA": [
            20,20,21,21,21,22,
            22,22,23,23,23,23
        ]
    }
)

settings = get_default_settings()

plot = HistogramPlot(
    df,
    settings
)

fig, ax = plot.build()

plt.show()