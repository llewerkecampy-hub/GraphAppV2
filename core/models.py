# core/models.py

from dataclasses import dataclass, field
from typing import Optional, List


# =====================================================
# Axis Settings
# =====================================================

@dataclass
class AxisSettings:

    scale: str = "Linear"

    tick_format: str = "Plain Numbers"

    auto_scale: bool = True

    y_min: float | None = None

    y_max: float | None = None

    major_tick_step: float = 10.0

    show_minor_ticks: bool = True

    minor_divisions: int = 2

    major_tick_length: float = 8.0

    major_tick_width: float = 2.0

    minor_tick_length: float = 4.0

    minor_tick_width: float = 1.0

    tick_direction: str = "out"



# =====================================================
# Figure Settings
# =====================================================

@dataclass
class FigureSettings:

    graph_type: str = "Bar"

    width: float = 8.0

    height: float = 6.0

    palette: str = "deep"

    theme: str = "Default"

    title: str = ""

    x_label: str = ""

    y_label: str = ""

    show_points: bool = True


# =====================================================
# Statistics Settings
# =====================================================

@dataclass
class StatisticsSettings:

    method: str = "Auto"

    error_type: str = "SEM"

    alpha: float = 0.05

    show_statistics: bool = True

    selected_comparisons: List[dict] = field(
        default_factory=list
    )


# =====================================================
# Export Settings
# =====================================================

@dataclass
class ExportSettings:

    file_format: str = "png"

    dpi: int = 600

    transparent: bool = False

    filename: str = "Figure1"


# =====================================================
# Complete Application Settings
# =====================================================

@dataclass
class AppSettings:

    figure: FigureSettings

    axis: AxisSettings

    statistics: StatisticsSettings

    export: ExportSettings



# =====================================================
# Pairwise Comparison Result
# =====================================================

@dataclass
class ComparisonResult:

    group1: str

    group2: str

    pvalue: float

    stars: str


# =====================================================
# Statistics Result
# =====================================================

@dataclass
class StatisticsResult:

    test_name: str = ""

    statistic: Optional[float] = None

    pvalue: Optional[float] = None

    stars: str = "ns"

    posthoc: Optional[object] = None

    comparisons: List[ComparisonResult] = field(
        default_factory=list
    )

@dataclass
class DataInfo:

    data_type: str

    x_column: str | None

    groups: list