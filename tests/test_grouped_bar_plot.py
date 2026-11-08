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
        "Control":
        [10,11,12,13],

        "MutA":
        [20,21,22,23],

        "MutB":
        [15,16,17,18]
    }
)

settings = get_default_settings()

settings.figure.graph_type = (
    "Grouped Bar"
)

settings.figure.title = (
    "Grouped Bar Test"
)

fig, ax = build_graph(
    df,
    settings
)

plt.show()