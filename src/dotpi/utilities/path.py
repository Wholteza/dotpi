import pathlib

PACKAGES_PATH_RELATIVE_TO_HOME = ".config/wholteza/installer/package-definitions"
CONFIGURATION_BOOTSTRAPS_PATH_RELATIVE_TO_HOME = ".config/wholteza/installer/configuration-bootstraps"


def get_packages_definitions_directory_path():
    return pathlib.Path.home().joinpath(PACKAGES_PATH_RELATIVE_TO_HOME)


def get_bashrc_file_path():
    return pathlib.Path.home().joinpath(".bashrc")


def get_configuration_bootstrap_file_path(filename: str):
    return pathlib.Path.home().joinpath(CONFIGURATION_BOOTSTRAPS_PATH_RELATIVE_TO_HOME).joinpath(filename)
