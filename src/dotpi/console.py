from dotpi.distribution_installer.enums.distribution import Distribution
from .utilities.command_line_arguments import get_distribution
from .distribution_installer.distribution_installer_context import install
import click
from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """dotpi: The dotfile and package installer"""
    install(Distribution("ubuntu"))
