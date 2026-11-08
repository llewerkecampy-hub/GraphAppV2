import pandas as pd
import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from graph_types.line_plot import (
    LinePlot
)

df = pd.DataFrame(

    [

        [0,1,2,5,6],
        [1,2,3,7,8],
        [2,3,4,9,10],
        [3,4,5,11,12]

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
    "Growth Curve"
)

settings.figure.x_label = (
    "Time"
)

settings.figure.y_label = (
    "OD600"
)

settings.statistics.error_type = (
    "SEM"
)

plot = LinePlot(
    df,
    settings
)

fig, ax = plot.build()

plt.show()