import pandas as pd

import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from palettes import (
    get_palette
)

from core.graph_builder import (
    build_graph
)

data = {

    "Control": [
        10,
        12,
        13,
        11,
        14
    ],

    "Treatment": [
        18,
        19,
        20,
        17,
        21
    ]
}

df = pd.DataFrame(data)
settings = get_default_settings()

fig, ax = plt.subplots(
    figsize=(8, 6)
)

palette = get_palette(
    settings.figure.palette,
    len(df.columns)
)

build_graph(
    ax,
    df,
    settings,
    palette
)

build_graph(
    ax,
    df,
    settings,
    palette
)

plt.show()
