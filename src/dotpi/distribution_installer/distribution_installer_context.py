from dotpi.distribution_installer.enums.distribution import Distribution
from dotpi.distribution_installer.strategies.ubuntu_strategy import install as ubuntu_strategy

distribution_strategies = {Distribution.UBUNTU: ubuntu_strategy}


def install(distribution: Distribution):
    if distribution not in distribution_strategies:
        raise Exception(
            "No distribution strategy could be found for the selected distribution: % s" % (distribution))
    distribution_strategies[distribution]()
