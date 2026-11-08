# annotations/bracket_layout.py

from dataclasses import dataclass


# =====================================================
# Bracket Model
# =====================================================

@dataclass
class Bracket:

    group1: str
    group2: str

    x1: int
    x2: int

    y: float

    stars: str

    pvalue: float


# =====================================================
# Overlap Detection
# =====================================================

def overlaps(
    bracket_a,
    bracket_b
):

    return not (

        bracket_a.x2 < bracket_b.x1

        or

        bracket_a.x1 > bracket_b.x2

    )


# =====================================================
# Layout Engine
# =====================================================

def build_bracket_layout(
    comparisons,
    group_positions,
    starting_height,
    height_step
):

    # ---------------------------------------------
    # Normalize group position keys
    # ---------------------------------------------

    normalized_positions = {

        str(group): position

        for group, position

        in group_positions.items()

    }

    # ---------------------------------------------
    # Filter invalid comparisons
    # ---------------------------------------------

    valid_comparisons = []

    for comparison in comparisons:

        group1 = str(
            comparison.group1
        )

        group2 = str(
            comparison.group2
        )

        if (

            group1 in normalized_positions

            and

            group2 in normalized_positions

        ):

            valid_comparisons.append(
                comparison
            )

        else:

            print(

                "Skipping comparison:",

                group1,

                group2

            )

    # ---------------------------------------------
    # Sort by span size
    # ---------------------------------------------

    sorted_comparisons = sorted(

        valid_comparisons,

        key=lambda c: abs(

            normalized_positions[
                str(c.group2)
            ]

            -

            normalized_positions[
                str(c.group1)
            ]

        )

    )

    layout = []

    used = []

    for comparison in sorted_comparisons:

        group1 = str(
            comparison.group1
        )

        group2 = str(
            comparison.group2
        )

        x1 = min(

            normalized_positions[
                group1
            ],

            normalized_positions[
                group2
            ]

        )

        x2 = max(

            normalized_positions[
                group1
            ],

            normalized_positions[
                group2
            ]

        )

        y = starting_height

        while True:

            candidate = Bracket(

                group1=group1,

                group2=group2,

                x1=x1,

                x2=x2,

                y=y,

                stars=comparison.stars,

                pvalue=comparison.pvalue

            )

            collision = False

            for existing in used:

                if (

                    overlaps(
                        candidate,
                        existing
                    )

                    and

                    abs(
                        existing.y
                        -
                        candidate.y
                    )

                    < 1e-9

                ):

                    collision = True

                    break

            if collision:

                y += height_step

            else:

                break

        layout.append(
            candidate
        )

        used.append(
            candidate
        )

    return layout


# =====================================================
# Layout Height
# =====================================================

def required_plot_height(
    layout,
    bracket_height
):

    if not layout:

        return None

    highest = max(

        bracket.y

        for bracket in layout

    )

    return (

        highest

        + bracket_height * 2

    )