from dotpi.package_installer.utilities.packages_definition_file_reader import get_packages_from_file
from dotpi.utilities.iterable import to_comma_separated_string
import os


def ensure(path_to_apt_packages_definition: str):
    """Ensures that aptitude packages are installed"""

    apt_packages = get_packages_from_file(path_to_apt_packages_definition)
    print("Will install these apt packages: % s" %
          (to_comma_separated_string(apt_packages)))

    uninstallable_apt_packages = []
    os.system("sudo apt update")
    for apt in apt_packages:
        install_status = os.system("sudo apt install -y % s" % (apt))
        if install_status:
            uninstallable_apt_packages.append(apt)
    # os.system("sudo apt autoremove -y")

    return uninstallable_apt_packages
