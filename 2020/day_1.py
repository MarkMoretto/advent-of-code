
"""
Purpose: Advent of Code challenge
Day: 1
Date created: 2020-12-02
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

from config import PROJECT_FOLDER
from pathlib import Path


local_input_file = r"data\day-1-input.txt"


def prod(iterable):
    """Product of values in array."""
    if len(iterable) == 0:
        return 1
    else:
        return iterable[0] * prod(iterable[1:])


with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
    raw_data = f.read().decode("utf-8").splitlines()
    data = sorted(list(map(lambda x: int(x), raw_data)))

# Evaluate half of the number list
half = len(data) // 2
h1, h2 = data[:half], data[half:]



# Part 1: Two numbers that sum up to 2020
NUMBER_TO_FIND: int = 2

values: list = []
h1_values: list = []
for i in range(half):
    for j in range(i+1, half - 1):
        if h1[i] + h1[j] == 2020:
            h1_values.append(h1[i])
            h1_values.append(h1[j])

if len(h1_values) == NUMBER_TO_FIND:
    values = h1_values

else:
    values: list = []
    h2_values: list = []
    for i in range(half):
        for j in range(i+1, half -1):
            if h2[i] + h2[j] == 2020:
                h2_values.append(h1[i])
                h2_values.append(h1[j])

    if len(h2_values) == NUMBER_TO_FIND:
        values = h2_values

if len(values) == NUMBER_TO_FIND:
    print(f"Part 1 answer:\n\tValues: {values}\n\tProduct: {prod(values)}")


# Part 2: Three numbers that sum up to 2020

NUMBER_TO_FIND: int = 3

values: list = []
for i in range(half):
    for j in range(i+1, half - 1):
        for k in range(j+1, half - 2):
            if h1[i] + h1[j] + h1[k] == 2020:
                values.append(h1[i])
                values.append(h1[j])
                values.append(h1[k])

if len(values) == NUMBER_TO_FIND:
    print(f"Part 2 answer:\n\tValues: {values}\n\tProduct: {prod(values)}")