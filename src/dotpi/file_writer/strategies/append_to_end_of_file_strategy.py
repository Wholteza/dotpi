from pathlib import Path
from typing import List
from dotpi.file_reader.utilities.file import ensure_exists


def write(lines: List[str], file: Path):
    ensure_exists(file)

    file = open(file, "a")

    for line in lines:
        file.write(line)

    file.close()
