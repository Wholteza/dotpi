from pathlib import Path
from dotpi.package_installer.utilities.packages_definition_file_reader import get_packages_from_file
from dotpi.utilities.iterable import to_comma_separated_string
import os


def ensure(path_to_snap_packages_definition: Path):
    """Ensures that snap packages are installed"""

    snap_packages = get_packages_from_file(path_to_snap_packages_definition)

    print("Will install these snap packages: % s" % (
        to_comma_separated_string(snap_packages)))

    uninstallable_snap_packages = []
    for snap in snap_packages:
        install_status = os.system("sudo snap install % s --classic" % (snap))
        if install_status:
            uninstallable_snap_packages.append(snap)

    if len(uninstallable_snap_packages):
        raise Exception("Following packages could not be installed using the snap package strategy: % s" % (
            to_comma_separated_string(uninstallable_snap_packages)))
