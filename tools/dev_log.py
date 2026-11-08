from datetime import datetime
from pathlib import Path


def add_entry(
    title,
    notes
):

    logfile = Path(
        "docs/development_log.md"
    )

    logfile.parent.mkdir(
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )

    entry = f"""
## {timestamp}

### {title}

{notes}

"""

    with open(
        logfile,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(entry)

    print(
        "Entry added."
    )


if __name__ == "__main__":

    add_entry(

        "Statistics Engine Complete",

        """
Completed:

- assumptions.py
- ttests.py
- anova.py
- nonparametric.py
- posthoc.py

Auto statistical selection now working.
"""

    )
