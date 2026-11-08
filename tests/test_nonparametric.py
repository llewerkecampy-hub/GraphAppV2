import pandas as pd

from stats.nonparametric import (
    mann_whitney_u,
    kruskal_wallis
)

# ===========================================
# Mann-Whitney U
# ===========================================

df_two = pd.DataFrame(
    {
        "Control":
        [10,11,12,13,12],

        "Mutant":
        [20,21,22,23,22]
    }
)

result = mann_whitney_u(
    df_two
)

print()
print("Mann-Whitney")
print(result)

# ===========================================
# Kruskal-Wallis
# ===========================================

df_three = pd.DataFrame(
    {
        "Control":
        [10,11,12,13,12],

        "MutA":
        [20,21,22,23,22],

        "MutB":
        [15,16,17,18,17]
    }
)

result = kruskal_wallis(
    df_three
)

print()
print("Kruskal-Wallis")
print(result)