from typing import Iterable


def to_comma_separated_string(strings: Iterable[str]):
    """Convert an Iterable of strings into a comma separated string"""

    comma_separated_string = ""
    for str in strings:
        # if i:
        comma_separated_string += "% s, " % (str)
        # else:
        # comma_separated_string += "% s" % (str)
    return comma_separated_string
