import pandas as pd
import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from core.statistics_engine import (
    run_statistics
)

from core.graph_builder import (
    build_graph
)

df = pd.DataFrame(
    {
        "Control":
        [10,11,12,13,12],

        "MutA":
        [20,21,22,23,22],

        "MutB":
        [15,16,17,18,17]
    }
)

settings = get_default_settings()

settings.figure.graph_type = "Bar"

settings.statistics.method = (
    "One-Way ANOVA"
)

result = run_statistics(
    df,
    settings.statistics
)

fig, ax = build_graph(
    df,
    settings,
    statistics_result=result
)

plt.show()