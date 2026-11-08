import pandas as pd

from stats.ttests import (
    student_t_test,
    welch_t_test
)

df = pd.DataFrame(
    {
        "Control":
        [10,11,12,13,12],

        "Mutant":
        [20,21,22,23,22]
    }
)

student = student_t_test(
    df
)

welch = welch_t_test(
    df
)

print(student)
print()

print(welch)