import sys
from dotpi.utilities.iterable import to_comma_separated_string
from dotpi.distribution_installer.enums.distribution import Distribution


def get_distribution():
    if sys.argv.__len__() < 2:
        raise Exception(
            "No distribution was selected\nSelect one of the following: % s" % (to_comma_separated_string(Distribution)))
    return Distribution(sys.argv[1])
