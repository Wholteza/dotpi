from pathlib import Path
import os


def read(file: Path):
    """Returns the content of a file as a list using newlines as separator

    Ignores lines consisting of only newlines or that starts with \"#\".
    """

    if not os.path.exists(file):
        raise FileNotFoundError("Packages file could not be found: % s" % file)

    opened_file = open(
        file, "rt")

    rows = []
    for row in opened_file:
        if row.startswith(("#", "\n")):
            continue
        rows.append(row.replace("\n", ""))

    return rows
