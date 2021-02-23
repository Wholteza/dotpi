from dotpi.file_writer.enums.file_writer_strategy import FileWriterStrategy
from dotpi.file_writer.file_writer_context import write
from pathlib import Path
from dotpi.file_reader.enums.file_reading_strategy import FileReadingStrategy
from dotpi.file_reader.file_reader_context import read


def bootstrap(sections_file: Path, target_file: Path):
    """Ensures that the specified file contains the sections specified in the sections file"""

    sections = read(sections_file, FileReadingStrategy.SECTIONS)
    target = read(target_file, FileReadingStrategy.PLAIN_TEXT)

    sections_to_append = []
    for section in sections:
        if not section in target:
            sections_to_append.append(section)

    write(sections_to_append, target_file,
          FileWriterStrategy.APPEND_TO_END_OF_FILE)
