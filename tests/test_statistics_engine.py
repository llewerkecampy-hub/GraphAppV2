import pandas as pd

from core.settings import (
    get_default_settings
)

from core.statistics_engine import (
    run_statistics,
    get_assumption_report,
    get_recommended_test
)

# =====================================
# Sample Data
# =====================================

df = pd.DataFrame(
    {
        "Control":
        [10,11,12,13,12],

        "MutA":
        [20,21,22,23,22],

        "MutB":
        [14,15,16,17,18]
    }
)

settings = (
    get_default_settings()
)

# =====================================
# Auto
# =====================================

settings.statistics.method = "Auto"

result = run_statistics(
    df,
    settings.statistics
)

print()
print("AUTO")
print(result)

# =====================================
# Recommendation
# =====================================

print()
print("RECOMMENDED")

print(
    get_recommended_test(
        df,
        settings.statistics
    )
)

# =====================================
# Assumptions
# =====================================

print()
print("ASSUMPTIONS")

print(
    get_assumption_report(
        df,
        settings.statistics
    )
)