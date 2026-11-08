import pandas as pd
import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from graph_types.box_plot import (
    BoxPlot
)

df = pd.DataFrame(
    {
        "Control":
        [10,11,12,13],

        "MutA":
        [20,21,22,23],

        "MutB":
        [15,16,17,18]
    }
)

settings = get_default_settings()

settings.figure.title = (
    "Box Plot Test"
)

plot = BoxPlot(
    df,
    settings
)

fig, ax = plot.build()

plt.show()