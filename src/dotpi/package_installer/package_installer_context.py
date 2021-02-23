from pathlib import Path
from dotpi.package_installer.enums.package_type import PackageType
from dotpi.package_installer.strategies.snap_package_strategy import ensure as snap_strategy
from dotpi.package_installer.strategies.apt_package_strategy import ensure as apt_strategy

package_installer_strategies = {
    PackageType.SNAP: snap_strategy,
    PackageType.APT: apt_strategy
}


def ensure(package_type: PackageType, packages_definition_file_path: Path):
    """Ensures that packages are installed on the system

    package_type: The type of package that you want to install. Is used to select the proper installation strategy.

    packages_definition_file_path: Newline separated file containing the names of the packages you want to install.
    The file excludes lines containing only newlines or that starts with \"#\".
    """
    if package_type not in package_installer_strategies:
        raise Exception(
            "Package installer strategy for package type \"% s\" could not be found" % (package_type))
    package_installer_strategies[package_type](packages_definition_file_path)
