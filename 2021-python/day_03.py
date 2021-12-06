#!/usr/bin/env python3

# https://adventofcode.com/2021/day/3

from typing import Callable, Iterable, Union
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day3.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read().splitlines()

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

def transpose(iterable: list, as_string: bool = False) -> list:
    """Transpose nested list rows and columns."""
    output = list(zip(*iterable))
    if as_string:
        return ["".join(line) for line in output]
    return output

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

data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".strip().splitlines()
# Transpose data matrix
# t_bin_matrix = transpose(data)
t_data = transpose(data, True)
bin_matrix = transpose(t_bin_matrix)


def sort_freq(iterable: Iterable, fn_minmax: Callable = max):
    D = counter(iterable)
    if D.get("0") == D.get("1"):
        return fn_minmax(D.keys())
    else:
        tmp = iter([k for k, v in D.items() if v == fn_minmax(D.values())])
        return next(tmp, None)


def solution(iterable, rating_name = "oxy") -> str:
    """Part 2 solution function.
    
    Parameter
    ---------
    iterable : list
        List of binary values to process
    rating_name : str
        Name of rating for which the solution should be found.

    Returns
    -------
    str
        Binary string calculated based on the given rating name constraints.
    """
    # Copies iterable (probably not necessary)
    ddata = iterable

    # Initial data transpose.
    t_data = transpose(ddata, True)

    # Output string
    _rate = ""

    for i in range(len(t_data)):
        # First transpose value.
        col = t_data[i]
        # Chec krating name and apply appropriate function
        if rating_name == "oxy":
            freq = sort_freq(col, max)
        else:
            freq = sort_freq(col, min)

        # Append output string
        _rate += freq

        # Thin out data list and re-transpose before looping.
        ddata = [line for line in ddata if line[i] == freq]
        t_data = transpose(ddata, True)
    return _rate

oxy_gen_rate = solution(data, rating_name="oxy")
co2_scrubber_rate = solution(data, rating_name="scrub")

oxy_gen_value = int(oxy_gen_rate, 2)
co2_scrubber_value = int(co2_scrubber_rate, 2)
life_support_rating = oxy_gen_value * co2_scrubber_value
print(f"The life support rating is: {life_support_rating}")
