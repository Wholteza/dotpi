from enum import Enum


class FileReadingStrategy(Enum):
    LINE_BY_LINE = "LINE_BY_LINE"
    SECTIONS = "SECTIONS"
    PLAIN_TEXT = "PLAIN_TEXT"
