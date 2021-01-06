
"""
Purpose: Advent of Code challenge
Day: 25
Date created: 2020-12-25

Contributor(s):
    Mark M.
"""


try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache

import re
from array import array
import itertools as ittr
# import more_itertools as mittr # https://more-itertools.readthedocs.io/en/stable/
from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True



# Import data
if DEBUG:
    # raw_data = """32415"""
    raw_data = """5764801
    17807724"""

    raw_data = raw_data.strip().replace("\r", "")
else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")
    raw_data = raw_data.strip().replace("\r", "")



# raw_data = read_data(f"day-25-input.txt")
# raw_data = raw_data.strip().replace("\r", "")

# Keys (aka - subject numbers)
card_key, door_key = map(int, re.split(r"\n\s*", raw_data))
keys = card_key, door_key
keys_arr = array("Q", keys)

# def ok(*args):
#     return sum([1 if i > 0 else 0 for i in args]) == len(args)
DIVISOR = 20201227
SUBJECT_NUMBER = 7
results = []
for k in keys_arr:
    value = 1
    loops = 0
    while value != k:
        value = (value * SUBJECT_NUMBER) % DIVISOR
        loops += 1
    results.append([k, loops])


print(f"Part 1:\n\t" + "\n\t".join([f"Key: {el[1]}\tLoops: {el[1]}" for el in results]))


keyvalue = min(keys_arr)
rangevalue = [i[1] for i in results if not i[0] == keyvalue][0]
value = 1
for i in range(rangevalue):
    value = (value * keyvalue) % DIVISOR
result = value
print(f"Part 1: Final result: {result}")




