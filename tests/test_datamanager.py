# tests/test_data_manager.py

import pandas as pd

from core.data_manager import *

# ==========================================
# Grouped
# ==========================================

grouped_df = pd.DataFrame(
    {
        "Control": [10,11,12],
        "MutA": [20,21,22]
    }
)

print("Grouped:")
print(
    get_grouped_data(
        grouped_df
    )
)

# ==========================================
# XY
# ==========================================

xy_df = pd.DataFrame(

    [
        [0,1,2,5,6],
        [1,2,3,7,8],
        [2,3,4,9,10]
    ],

    columns=[
        "Time",
        "WT",
        "WT",
        "MutA",
        "MutA"
    ]
)

xy = get_xy_data(
    xy_df
)

print("\nXY:")

print(xy)

print("\nSummary:")

print(
    summarize_xy_data(
        xy
    )
)