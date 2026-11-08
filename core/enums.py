# core/enums.py

from enum import Enum


class AxisScale(str, Enum):

    LINEAR = "Linear"

    LOG10 = "Log10"

    LOG2 = "Log2"

    NATURAL_LOG = "Natural Log"


class TickFormat(str, Enum):

    PLAIN = "Plain Numbers"

    SCIENTIFIC = "Scientific"

    POWER = "10^n"
