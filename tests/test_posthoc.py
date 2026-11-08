import pandas as pd

from stats.posthoc import (
    dunn_posthoc,
    significant_comparisons
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

matrix, comparisons = dunn_posthoc(
    df
)

print()
print("Dunn Matrix")
print(matrix)

print()
print("All Comparisons")

for comp in comparisons:

    print(comp)

print()
print("Significant Only")

for comp in significant_comparisons(
    comparisons
):

    print(comp)