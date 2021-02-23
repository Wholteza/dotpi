import os
from pathlib import Path


def ensure_exists(file: Path):
    if not os.path.exists(file):
        raise FileNotFoundError("Packages file could not be found: % s" % file)
