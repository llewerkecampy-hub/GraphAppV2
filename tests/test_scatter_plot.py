import pandas as pd
import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from graph_types.scatter_plot import (
    ScatterPlot
)

df = pd.DataFrame(

    [

        [0,  1,  2,  5,  6],
        [1,  2,  8,  7, 15],
        [2,  3,  4,  9, 10],
        [3,  4, 20, 11, 12]

    ],

    columns=[

        "Time",

        "WT",
        "WT",

        "MutA",
        "MutA"

    ]
)

settings = get_default_settings()

settings.figure.title = (
    "Scatter Test"
)

settings.figure.x_label = (
    "Time"
)

settings.figure.y_label = (
    "Value"
)

plot = ScatterPlot(
    df,
    settings
)

fig, ax = plot.build()

plt.show()