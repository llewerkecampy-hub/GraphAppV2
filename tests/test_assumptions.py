import pandas as pd

from stats.assumptions import (
    build_assumption_report,
    recommend_test
)

df = pd.DataFrame(
    {
        "Control":
        [10,11,12,13,12],

        "MutA":
        [20,21,22,23,22],

        "MutB":
        [14,16,15,17,18]
    }
)

report = build_assumption_report(
    df
)

print(report)

print(
    recommend_test(df)
)