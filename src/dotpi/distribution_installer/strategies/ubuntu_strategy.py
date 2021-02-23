from dotpi.configuration_bootstrapper.configuration_bootstrapper_context import bootstrap
from dotpi.configuration_bootstrapper.enums.configuration_bootstrap_strategy import ConfigurationBootstrapStrategy
from dotpi.utilities.path import get_bashrc_file_path, get_configuration_bootstrap_file_path, get_packages_definitions_directory_path
from dotpi.package_installer.enums.package_type import PackageType
from dotpi.package_installer.package_installer_context import ensure as ensure_packages

SNAP_PACKAGES_FILENAME = "ubuntu-snap-packages"
APT_PACKAGES_FILENAME = "ubuntu-apt-packages"

BASHRC_BOOTSTRAP_FILENAME = "ubuntu-bashrc"

package_definitions_directory = get_packages_definitions_directory_path()


package_types = {
    PackageType.SNAP: package_definitions_directory.joinpath(SNAP_PACKAGES_FILENAME),
    PackageType.APT: package_definitions_directory.joinpath(
        APT_PACKAGES_FILENAME)
}

bootstraps = [
    [
        ConfigurationBootstrapStrategy.ENSURE_FILE_CONTAINS_SECTIONS,
        get_configuration_bootstrap_file_path(BASHRC_BOOTSTRAP_FILENAME),
        get_bashrc_file_path()
    ]
]


def install():
    """Ensures neccesary packages and configurations on ubuntu"""

    for package_type in package_types:
        ensure_packages(package_type, package_types[package_type])

    for strategy_boot_target in bootstraps:
        bootstrap(
            strategy_boot_target[2], strategy_boot_target[1], strategy_boot_target[0])

    # Print information about what repositories to clone
