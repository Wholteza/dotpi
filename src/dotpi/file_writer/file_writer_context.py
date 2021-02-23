from pathlib import Path
from typing import List
from dotpi.exceptions.strategy_not_found_error import StrategyNotFoundError
from dotpi.file_writer.strategies.append_to_end_of_file_strategy import write as append_to_end_of_file_strategy
from dotpi.file_writer.enums.file_writer_strategy import FileWriterStrategy


strategies = {
    FileWriterStrategy.APPEND_TO_END_OF_FILE: append_to_end_of_file_strategy
}


def write(lines: List[str], file: Path, strategy: FileWriterStrategy):
    if not strategy in strategies:
        raise StrategyNotFoundError(strategy)
    strategies[strategy](lines, file)
