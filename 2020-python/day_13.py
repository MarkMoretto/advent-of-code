
"""
Purpose: Advent of Code challenge
Day: 13
Date created: 2020-12-12
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

# import re
# import math
import numpy as np
from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """939
7,13,x,x,59,x,31,19"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-13-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)


value_arr = data[1].split(",")
in_service = [int(value_arr[i]) for i in range(len(value_arr)) if not value_arr[i] == "x"]

####################################
######### --- Part 1 --- ###########
####################################


earliest_departure = int(data[0])
in_service = [int(i) for i in data[1].split(",") if not i == "x"]
in_service_sorted = in_service.copy()
in_service_sorted.sort()
largest_gap = in_service.max()

min_gap = np.int32(1e6)
best_bus = []
start_time = earliest_departure + largest_gap
for i in range(1, start_time):
    for j in in_service_sorted:
        ji = j+i
        if i%j == 0 and ji > earliest_departure:
            tmp = abs(ji - earliest_departure)
            # print(i, j, ji, tmp)
            if tmp < min_gap:
                if len(best_bus) > 0:
                    best_bus.pop()
                min_gap = tmp
                best_bus.append(j)

result = min_gap * best_bus[0]
print(f"Part 1: The minimum gap times the best bus ID is: {result}")




####################################
######### --- Part 2 --- ###########
####################################


service_map = [[int(value_arr[i]), i] for i in range(len(value_arr)) if not value_arr[i] == "x"]

def find_schedule(id_map):
    t = 1
    stepsize = 1
    for busid in id_map:
        while (t + busid[1]) % busid[0] != 0:
            t += stepsize
        stepsize *= busid[0]
    return t

result = find_schedule(service_map)
print(f"Part 2:\n\tThe timestamp for the optimal time-offset schedule is:\n\t\t{result}\t({result:,})")


