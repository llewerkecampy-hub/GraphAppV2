# tests/test_annotations.py

from core.models import (
    ComparisonResult
)

from annotations.significance import (
    build_annotations
)

comparisons = [

    ComparisonResult(

        group1="Control",

        group2="MutA",

        pvalue=0.0001,

        stars="***"
    ),

    ComparisonResult(

        group1="Control",

        group2="MutB",

        pvalue=0.0001,

        stars="***"
    ),

    ComparisonResult(

        group1="MutA",

        group2="MutB",

        pvalue=0.002,

        stars="**"
    )
]

layout = build_annotations(

    comparisons,

    group_names=[
        "Control",
        "MutA",
        "MutB"
    ],

    y_max=25

)

print()

for bracket in layout:

    print(bracket)