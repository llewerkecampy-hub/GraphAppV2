# themes/themes.py

from dataclasses import dataclass


# =====================================================
# Theme Definition
# =====================================================

@dataclass
class Theme:

    name: str

    title_size: int
    label_size: int
    tick_size: int

    axis_linewidth: float

    major_tick_length: float
    major_tick_width: float

    minor_tick_length: float
    minor_tick_width: float

    show_grid: bool

    font_family: str


# =====================================================
# Theme Registry
# =====================================================

THEMES = {

    "Prism":

    Theme(

        name="Prism",

        title_size=18,
        label_size=16,
        tick_size=12,

        axis_linewidth=2.0,

        major_tick_length=8,
        major_tick_width=2,

        minor_tick_length=4,
        minor_tick_width=1,

        show_grid=False,

        font_family="Arial"
    ),

    "Publication":

    Theme(

        name="Publication",

        title_size=18,
        label_size=16,
        tick_size=14,

        axis_linewidth=2.5,

        major_tick_length=10,
        major_tick_width=2.5,

        minor_tick_length=5,
        minor_tick_width=1.5,

        show_grid=False,

        font_family="Arial"
    ),

    "Nature":

    Theme(

        name="Nature",

        title_size=16,
        label_size=14,
        tick_size=12,

        axis_linewidth=2,

        major_tick_length=7,
        major_tick_width=2,

        minor_tick_length=3,
        minor_tick_width=1,

        show_grid=False,

        font_family="Arial"
    ),

    "Science":

    Theme(

        name="Science",

        title_size=16,
        label_size=14,
        tick_size=12,

        axis_linewidth=2,

        major_tick_length=6,
        major_tick_width=2,

        minor_tick_length=3,
        minor_tick_width=1,

        show_grid=False,

        font_family="Arial"
    ),

    "Presentation":

    Theme(

        name="Presentation",

        title_size=24,
        label_size=20,
        tick_size=16,

        axis_linewidth=3,

        major_tick_length=12,
        major_tick_width=3,

        minor_tick_length=6,
        minor_tick_width=2,

        show_grid=True,

        font_family="Arial"
    )
}


# =====================================================
# Helpers
# =====================================================

def get_theme(name):

    return THEMES.get(
        name,
        THEMES["Prism"]
    )


def available_themes():

    return list(
        THEMES.keys()
    )
