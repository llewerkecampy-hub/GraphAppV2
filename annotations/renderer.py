# annotations/renderer.py

def draw_bracket(
    ax,
    x1,
    x2,
    y,
    height,
    text
):

    ax.plot(
        [
            x1,
            x1,
            x2,
            x2
        ],
        [
            y,
            y + height,
            y + height,
            y
        ],
        color="black",
        linewidth=1.5,
        clip_on=False
    )

    ax.text(
        (x1 + x2) / 2,
        y + height,
        text,
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold"
    )

# =====================================================
# Render Layout
# =====================================================

def render_annotations(
    ax,
    layout,
    bracket_height
):

    if not layout:

        return

    for bracket in layout:

        draw_bracket(

            ax,

            bracket.x1,
            bracket.x2,

            bracket.y,

            bracket_height,

            bracket.stars

        )

# =====================================================
# Axis Expansion
# =====================================================

def expand_axis_for_annotations(
    ax,
    layout,
    bracket_height
):

    if not layout:

        return

    highest = max(

        bracket.y

        for bracket in layout

    )

    current_min, current_max = (
        ax.get_ylim()
    )

    needed_max = (

        highest

        + bracket_height * 3

    )

    if needed_max > current_max:

        ax.set_ylim(
            current_min,
            needed_max
        )
