
"""
Purpose: Advent of Code challenge
Day: 23
Date created: 2020-12-23

Contributor(s):
    Mark M.
"""

import re
from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    # raw_data = """32415"""
    raw_data = """389125467"""


else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-23-input.txt")

def extend_data(iterable, n_moves = 100):
    """Create additional list values."""
    n_values = len(iterable)
    return iterable * int(round((1 / (n_values / n_moves)) + 0.5, 0))


def cycler(iterable):
    """Unending cycles of mayhem!"""
    while True:
        tmp = iterable.copy()
        while tmp:
            yield tmp.pop(0)





data = list(map(int, list(raw_data)))
min_cup = min(data)
data_len = len(data)

stepsize = 3
N = 10
counter = 0
idx = 0

current_cup = data[idx]
dest_cup = current_cup - 1


for _ in range(N):
    start = idx + 1
    stop = start + stepsize

    if idx >= data_len - 1:
        idx = 0
    if stop > data_len:
        stop


    start = idx + 1
    stop = start + stepsize
    print(idx, start, stop)
    idx += 1

    rng = tuple(range(start, stop))

    three_aside = data[start:stop]

    tmp_data = [v for i, v in enumerate(data) if not i in rng]


    dest_cup = current_cup - 1
    while True:
        if not dest_cup in tmp_data[start:]:
            if dest_cup >= min_cup
                dest_cup -= 1
            else:
                idx = tmp_data.index(max(tmp_data))
                break
        else:
            idx = tmp_data.index(dest_cup)
            break

    print(data, tmp_data, dest_cup)

    data = [tmp_data[idx]] + three_aside + data[stop:]

    idx += 1




"""
m1
389125467

pu: 891
325467

dest: 2
328915467

pu: 891
325467

dest: 1 # Destination not in remaining cups, so highest cup is selected
dest: 7

"""




