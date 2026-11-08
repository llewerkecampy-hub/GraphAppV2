import pandas as pd

from stats.anova import (
    one_way_anova
)

df = pd.DataFrame(
    {
        "Control":
        [10, 11, 12, 13, 12],

        "MutA":
        [20, 21, 22, 23, 22],

        "MutB":
        [14, 15, 16, 15, 17]
    }
)

result = one_way_anova(
    df
)

print()

print("Test:")
print(result.test_name)

print()

print("Statistic:")
print(result.statistic)

print()

print("P-value:")
print(result.pvalue)

print()

print("Stars:")
print(result.stars)

print()

print("Comparisons:")

for comparison in result.comparisons:

    print(comparison)

print()

print("Posthoc Table:")
print(result.posthoc)