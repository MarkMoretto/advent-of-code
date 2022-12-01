#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 7
Date: 2021-12-07
URL: https://adventofcode.com/2021/day/7
Contributor(s):
    mark moretto
"""

from sys import maxsize
from typing import List, Union
from pathlib import Path

# Get data
AOC_DAY: int = 7
USE_SAMPLE_TF: bool = False


DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath(
    f"day{AOC_DAY:0>2}{'-sample' if USE_SAMPLE_TF else ''}.txt"
    )
raw_data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()

# Signature Types
String = str
Integer = int
Float = float
Number = Union[int, float]
IList = List[Integer]
NumList = List[Number]

def stoi(string: String) -> NumList:
    return list(map(int, string.split(",")))

# Parse and transform raw data.
data = stoi(raw_data)


##################
# --- Part 1 --- #
##################

# costmap = {}
min_cost = maxsize
for d in set(data):
    # costmap[d] = sum([abs(d-n) for n in data])
    current_cost = sum([abs(d-n) for n in data])
    if current_cost < min_cost:
        min_cost = current_cost

result = min_cost
print(f"Part 1 solution: {result}")


##################
# --- Part 2 --- #
##################

def cumsum(n: Number, target: Number, __cache={}) -> Integer:
    __hash = (n, target)
    if not __hash in __cache:
        stepcount = 0
        for i in range(abs(n - target)+1):
            stepcount += i
        __cache[__hash] = stepcount
    return __cache[__hash]


# Number of consecutive increases before a clear upward tend is spotted.
MAX_CONSECUTIVE_INCR = 3
n_consec = 0
min_cost = maxsize
min_pos, max_pos = min(data), max(data)
# costmap = {}
for i in range(min_pos, max_pos + 1):
    if n_consec >= MAX_CONSECUTIVE_INCR:
        break
    # costmap[i] = sum([cumsum(n, i) for n in data])
    current_cost = sum([cumsum(n, i) for n in data])
    if current_cost < min_cost:
        min_cost = current_cost
    elif current_cost > min_cost:
        n_consec += 1



# Alt method: Mean value and/or mean less 1
mean_value = int(round(sum(data) / len(data), 0))
mean_minus_one = mean_value - 1
trials = [mean_value, mean_minus_one]
alt_min_value = min([sum([cumsum(n, v) for n in data]) for v in trials])

# mapvalues = list(costmap.values())
# [f"Prev {x}, Curr. {y} -> {y-x}" for x, y in zip(mapvalues[:-1], mapvalues[1:])]

result = min_cost
print(f"Part 2 solution: {result}")
