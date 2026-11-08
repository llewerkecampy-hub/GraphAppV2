# tests/test_axes.py

import matplotlib.pyplot as plt

from core.settings import (
    get_default_settings
)

from axes.linear_axis import (
    apply_linear_axis
)

settings = (
    get_default_settings()
)

fig, ax = plt.subplots()

ax.plot(
    [1, 2, 3],
    [10, 20, 30]
)

apply_linear_axis(
    ax,
    settings.axis
)

plt.show()