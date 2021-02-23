import os
from pathlib import Path


def get_packages_from_file(packages_definition_file_path: Path):
    """Returns a list of the names of the packages in the provided file"""

    if not os.path.exists(packages_definition_file_path):
        raise FileNotFoundError("Packages file could not be found: % s" % (
            packages_definition_file_path))

    packages_file = open(
        packages_definition_file_path, "rt")

    package_names = []
    for package in packages_file:
        if package.startswith(("#", "\n")):
            continue
        package_names.append(package.replace("\n", ""))

    return package_names
