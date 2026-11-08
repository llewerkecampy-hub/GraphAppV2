# tests/test_export_manager.py

import pandas as pd

from core.settings import (
    get_default_settings
)

from core.graph_builder import (
    build_graph
)

from core.export_manager import (
    export_figure
)

df = pd.DataFrame(
    {
        "Control":
        [10,11,12,13],

        "MutA":
        [20,21,22,23]
    }
)

settings = (
    get_default_settings()
)

settings.figure.graph_type = (
    "Bar"
)

settings.export.file_format = (
    "png"
)

settings.export.filename = (
    "test_export"
)

fig, ax = build_graph(
    df,
    settings
)

path = export_figure(
    fig,
    settings.export
)

print(path)