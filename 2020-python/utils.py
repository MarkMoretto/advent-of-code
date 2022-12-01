
__all__ = [
    "read_data",
    "get_lines",
    "current_file",
    "day_number",
]

import re
import os.path
from os import linesep
from pathlib import Path

from config import DATA_FOLDER


def read_data(filename: str, aoc_year: int = 2020, return_bytes: bool = False):
    """Function to read data file based on filename and AoC competition year."""
    subpath = os.path.join(str(aoc_year), filename)
    with open(DATA_FOLDER.joinpath(subpath), "rb") as f:
        data = f.read()
        if not return_bytes:
            data = data.decode("utf-8")
    return data


def get_lines(string: str, newline: str = "\n"):
    """Simple function to parse text document and split sections by newline."""
    string = string.replace(linesep, newline)
    return [i.strip() for i in string.split(newline) if len(i.strip()) > 0]


def current_file(specification):
    """Return the current filepath with filename as pathlib.Path object."""
    return Path(os.path.abspath(specification))


def day_number(filename: str):
    """Return day number from a filepath string (e.g. - Path.stem, os.path.abspath()).
    
    >>> day_number(Path(r"C:\\Users\day_1.txt").stem)
    '1'
    """
    return re.sub(r"\D", "", filename)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(current_file())