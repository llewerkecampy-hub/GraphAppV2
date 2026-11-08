from pathlib import Path


def write_markdown(
    filename,
    title,
    sections
):
    """
    Create a Markdown document.

    Parameters
    ----------
    filename : str
        Output markdown file

    title : str
        Document title

    sections : list[tuple]
        [
            ("Heading", "Content"),
            ...
        ]
    """

    lines = []

    lines.append(
        f"# {title}\n"
    )

    for heading, content in sections:

        lines.append(
            f"## {heading}\n"
        )

        lines.append(
            f"{content}\n"
        )

    output = Path(filename)

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Saved: {output}"
    )


if __name__ == "__main__":

    sections = [

        (
            "Project Vision",

            """
GraphAppV2 is a GraphPad Prism-inspired
statistical analysis and scientific
figure generation platform focused on
microbiology and experimental biology.
"""
        ),

        (
            "Architecture",

            """
core/
stats/
annotations/
axes/
graph_types/
themes/
palettes/
ui/
tests/
"""
        ),

        (
            "Data Models",

            """
Grouped Data:

Control | MutA | MutB

Used for:
- Bar
- Box
- Violin
- ANOVA
- T-tests

XY Data:

Time | WT | WT | MutA | MutA

Duplicate column names are treated
as biological replicates.
"""
        ),

        (
            "Future Features",

            """
- Box + Points
- Violin + Points
- True Grouped Bar Plot
- Two-Way ANOVA
- Repeated Measures ANOVA
- Growth Curve Analysis
- PCA
- Volcano Plots
- Tn-Seq Analysis
"""
        )
    ]

    write_markdown(
        "docs/architecture.md",
        "GraphAppV2 Architecture",
        sections
    )