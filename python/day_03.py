#!/usr/bin/env python3

# https://adventofcode.com/2021/day/3

from typing import Union
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day3.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read().splitlines()


# data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".strip().splitlines()



def counter(iterable: Union[str, tuple]):
    output = {}
    for el in set(iterable):
        output[el] = iterable.count(el)
    return output

def most_freq(d: dict):
    max_freq = max(d.values())
    tmp = iter([k for k, v in d.items() if v == max_freq])
    return next(tmp, None)

def bin_flip(value: str) -> str:
    if value == "1":
        return "0"
    return "1"

def calc_gamma_rate(matrix: list) -> str:
    _tmp: str = ""
    for line in matrix:
        _tmp += most_freq(counter(line))
    return _tmp

def calc_epsilon_rate(bin_string: str) -> str:
    """FLip 0s and 1s of gamma binary string."""
    return "".join(map(bin_flip, bin_string))

def transpose(iterable: list) -> list:
    """Transpose nested list rows and columns."""
    return list(zip(*iterable))

# --- Part 1 --- #

# Transpose data matrix
t_bin_matrix = transpose(data)

# Find and populate gamma and epsilon rates
gamma_rate: str = calc_gamma_rate(t_bin_matrix)
epsilon_rate = calc_epsilon_rate(gamma_rate)


# Convert binary values to decimal values
# Multiply results and show output.
gamma_value = int(gamma_rate, 2)
epsilon_value = int(epsilon_rate, 2)
power_consumption = gamma_value * epsilon_value
print(f"The power consumption is: {power_consumption}")


# --- Part 2 --- #

