#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 6
Date: 2021-12-06
Contributor(s):
    mark moretto
"""

from typing import List, Union
from pathlib import Path

# Processing local data.
DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day06.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()

String = str
Integer = int
Float = float
Number = Union[int, float]
IList = List[Integer]
NList = List[Number]

def stoi(string: String) -> NList:
    return list(map(int, string.split(",")))

##################
# --- Part 1 --- #
##################

def solution(input_data: String, n_days: Integer = 80) -> Integer:
    """Clobbered together function to handle fish count.
    """
    # Start with "previous" list of values, or just the initial
    # array provided.
    previous = stoi(input_data)

    # Iterate across days.
    for _ in range(n_days):
        # Update current array to decrement each value
        # unless the value is zero, which would reset the value
        # to six.
        current = [i-1 if i > 0 else 6 for i in current]
        # Append an eight to the end of the array for each zero within
        # the previous array.
        for _ in range(previous.count(0)):
            current += [8]
        # Copy current array into previous array.
        previous = current

    # Return length of array as solution.
    return len(current)

result = solution(data)
print(f"Part 1 solution: {result}")


##################
# --- Part 2 --- #
##################

# Functions
def zero_array(n_slots: Integer) -> IList:
    return [0] * n_slots


# Variables/constants
start_array = stoi(data)

N_DAYS = 256

N_SLOTS: Integer = 8
# For buffer slot at zero.
TOTAL_SLOTS: Integer = N_SLOTS + 1
# Index to restart countdown.
NEW_IDX: Integer = 6


def seed_array(arr: IList, base_array: IList = start_array) -> None:
    """Update new array with values from other array."""
    for i in base_array:
        arr[i] += 1


def solution(reset_index: Integer = NEW_IDX, total_slots: Integer = TOTAL_SLOTS, n_epochs: Integer = N_DAYS):
    # Static list of total slots available
    slot_range = list(range(total_slots+1))

    # Previous and current arrays,
    # initialized to values of zero for each of the total slots.
    previous = zero_array(total_slots)
    current = zero_array(total_slots)

    # 'Seed' initial array based on given start array.
    seed_array(previous)

    # Iterate through all the days
    for _ in range(n_epochs):
        # Shift index count from previous array to current array
        for i, j in zip(slot_range[:-1], slot_range[1:]):
            current[i] = previous[j%total_slots]

        # Update current array with number of zero values
        # that need to 'restart' their cycle.
        current[reset_index] += previous[0]

        # Copy updated current array into previous array.
        # Rinse and repeat.
        previous[:] = current
    
    return sum(current)


start_data = stoi(data)
result = solution()
print(f"Part 2 solution: {result}")
