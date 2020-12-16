
"""
Purpose: Advent of Code challenge
Day: 14
Date created: 2020-12-13
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

from collections import deque
from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = False

# Target number of spoken values to find.
TARGET_NUM = 2020


# Import data
if DEBUG:
    raw_data = """0,3,6"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-15-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)




def index_adj(n):
    return n + 1

def get_indices(to_find, iterable):
    return [index_adj(i) for i in range(len(iterable)) if iterable[i] == to_find]



            
seed_values = list(map(int, data[0].split(",")))

spoken = seed_values.copy()
num_map = {}
for i, n in enumerate(spoken, start=1):
    num_map[n] = deque([i], maxlen=2)

def find_nth_value(iterable, target_count, verbose = False):
    length = len(iterable)
    while length < TARGET_NUM:
        prev_turn = len(iterable) - 1
        prev_value = iterable[prev_turn]
        curr_count = iterable.count(prev_value)
        if curr_count == 1:
            iterable.append(0)
            length += 1
            new_idx = len(iterable)
            if not prev_value in num_map:
                num_map[prev_value] = deque([new_idx], maxlen=2)
            else:
                num_map[0].extendleft([new_idx])
        else:
            curr_value = num_map[prev_value][0] - num_map[prev_value][1]
            iterable.append(curr_value)
            length += 1
            new_idx = len(iterable)
            if not curr_value in num_map:
                num_map[curr_value] = deque([new_idx], maxlen=2)
            else:
                num_map[curr_value].extendleft([new_idx])
        prev_turn += 1
    return iterable[-1]

result = find_nth_value(spoken, TARGET_NUM)
print(f"Part 1: The 2020th result is: {result}")

# Part 2
# A different approach

TARGET_NUM = int(3e7)
# TARGET_NUM = 2020

spoken = [n for n in seed_values]
idx_map = {}
for i, n in enumerate(spoken, start=1):
    idx_map[n] = i

# spoken.extend([0] * (TARGET_NUM - len(spoken)))

curr_num = 0
curr_idx = len(seed_values)
for i in range(len(seed_values)  + 1, TARGET_NUM):
    if curr_num in idx_map:
        last_idx = idx_map.get(curr_num) # Get last index of number
        
        idx_map[curr_num] = i
        curr_num = i - last_idx
    else:
        # spoken[i] = curr_num
        idx_map[curr_num] = i
        curr_num = 0
    # spoken[i] = curr_num



result = curr_num
print(f"Part21: The 3E7th result is: {result}")
