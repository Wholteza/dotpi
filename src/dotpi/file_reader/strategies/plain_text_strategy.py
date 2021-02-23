from pathlib import Path
import os


def read(file: Path):
    """Returns the content of a file as a string"""

    if not os.path.exists(file):
        raise FileNotFoundError("Packages file could not be found: % s" % file)

    opened_file = open(
        file, "rt")

    text = ""
    for row in opened_file:
        text += row

    return text
