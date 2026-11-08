# palettes/palettes.py

import seaborn as sns


SEABORN_PALETTES = [

    "deep",
    "muted",
    "pastel",
    "bright",
    "dark",
    "colorblind",

    "viridis",
    "magma",
    "plasma",
    "inferno",
    "cividis"
]

CUSTOM_PALETTES = {

    "Classic": [

        "#4C72B0",
        "#55A868",
        "#C44E52",
        "#8172B2",
        "#CCB974",
        "#64B5CD"
    ],

    "Nature": [

        "#E64B35",
        "#4DBBD5",
        "#00A087",
        "#3C5488",
        "#F39B7F",
        "#8491B4"
    ],

    "Science": [

        "#3B4992",
        "#EE0000",
        "#008B45",
        "#631879",
        "#008280",
        "#BB0021"
    ],

    "Microbiology": [

        "#1B9E77",
        "#D95F02",
        "#7570B3",
        "#E7298A",
        "#66A61E",
        "#E6AB02"
    ],

    "Colorblind Safe": [

        "#000000",
        "#E69F00",
        "#56B4E9",
        "#009E73",
        "#F0E442",
        "#0072B2",
        "#D55E00",
        "#CC79A7"
    ]
}

def get_palette(
    palette_name,
    n_colors
):

    if palette_name in CUSTOM_PALETTES:

        palette = CUSTOM_PALETTES[
            palette_name
        ]

        if n_colors <= len(palette):

            return palette[:n_colors]

        repeats = (
            n_colors // len(palette)
        ) + 1

        return (
            palette * repeats
        )[:n_colors]

    try:

        return sns.color_palette(
            palette_name,
            n_colors
        )

    except Exception:

        return sns.color_palette(
            "deep",
            n_colors
        )

# =====================================================
# Available Palettes
# =====================================================

def available_palettes():

    return (
        list(
            CUSTOM_PALETTES.keys()
        )
        +
        SEABORN_PALETTES
    )