"""
Purpose: Advent of Code challenge
Day: 18
Date created: 2020-12-17
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import itertools as ittr
from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """.#.
..#
###"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-18-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)




####################################
######### --- Part 1 --- ###########
####################################


