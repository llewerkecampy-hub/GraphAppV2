import pandas as pd
import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from core.graph_builder import (
    build_graph
)

df = pd.DataFrame(
    {
        "A": [1,2,3],
        "B": [4,5,6],
        "C": [7,8,9]
    }
)

settings = get_default_settings()

settings.figure.graph_type = (
    "Heatmap"
)

settings.figure.palette = (
    "viridis"
)

settings.figure.title = (
    "Heatmap Test"
)

fig, ax = build_graph(
    df,
    settings
)

plt.show()