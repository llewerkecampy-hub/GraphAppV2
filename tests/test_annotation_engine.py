# tests/test_annotation_engine.py

import pandas as pd

from core.settings import (
    get_default_settings
)

from core.statistics_engine import (
    run_statistics
)

from core.annotation_engine import (
    build_annotation_layout,
    available_comparison_labels
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

settings = (
    get_default_settings()
)

settings.statistics.method = (
    "One-Way ANOVA"
)

result = run_statistics(
    df,
    settings.statistics
)

print()

print(
    available_comparison_labels(
        result
    )
)

layout = build_annotation_layout(

    statistics_result=result,

    group_names=list(
        df.columns
    ),

    y_max=25

)

print()

for bracket in layout:

    print(bracket)