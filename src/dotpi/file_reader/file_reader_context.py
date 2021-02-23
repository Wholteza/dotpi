from dotpi.exceptions.strategy_not_found_error import StrategyNotFoundError
from dotpi.file_reader.enums.file_reading_strategy import FileReadingStrategy
from pathlib import Path
from dotpi.file_reader.strategies.line_by_line_strategy import read as line_by_line_strategy
from dotpi.file_reader.strategies.sections_strategy import read as sections_strategy
from dotpi.file_reader.strategies.plain_text_strategy import read as plain_text_strategy

strategies = {
    FileReadingStrategy.LINE_BY_LINE: line_by_line_strategy,
    FileReadingStrategy.SECTIONS: sections_strategy,
    FileReadingStrategy.PLAIN_TEXT: plain_text_strategy
}


def read(file: Path, strategy: FileReadingStrategy):
    if not strategy in strategies:
        raise StrategyNotFoundError(strategy)
    return strategies[strategy](file)
