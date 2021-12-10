#!/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

"""
Purpose: Advent of Code 2021 - Day 9
Date: 2021-12-09
URL: https://adventofcode.com/2021/day/9
Contributor(s):
    mark moretto
"""

from os import linesep
from pathlib import Path
from typing import List, Union, Iterable, Iterator, Tuple

DATA_DIR = Path("data")

# Signature Types
String = str
Integer = int
Number = Union[int, float]
NumList = List[Number]

Matrix = List[List[Integer]]


# Get data
AOC_DAY: int = 9
USE_SAMPLE_TF: bool = False

DATA_FILE_A = DATA_DIR.joinpath(
    f"day{AOC_DAY:0>2}{'-sample' if USE_SAMPLE_TF else ''}.txt"
    )
raw_data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()


# --- Functions
def stoi(string: String) -> NumList:
    return list(map(int, list(string)))

def middle(low, high) -> int:
    return (high - low) // 2

def grid_shape(matrix: Matrix) -> Tuple[Integer, Integer]:
    return len(matrix), len(matrix[0])


def gen_coords(max_height: int, max_width: int) -> Iterator:
    """Generate 2-D pairs based on height/width, rows/columns, etc."""
    genr = iter((h, w) for h in range(max_height) for w in range(max_width))
    tmp = next(genr, None)
    while tmp:
        yield tmp
        tmp = next(genr, None)
    return

matrix: Matrix = [stoi(line) for line in raw_data.split(linesep)]
n_rows, n_cols = grid_shape(matrix)



##################
# --- Part 1 --- #
##################
min_value = []
# Generator
cg = gen_coords(n_rows, n_cols)
for r, c in cg:
    all_dirs = []
    if r - 1 >= 0:
        all_dirs.append(matrix[r-1][c])
    if r + 1 < n_rows:
        all_dirs.append(matrix[r+1][c])
    if c - 1 >= 0:
        all_dirs.append(matrix[r][c-1])
    if c + 1 < n_cols:
        all_dirs.append(matrix[r][c+1])
    
    if matrix[r][c] < min(all_dirs):
        min_value.append(matrix[r][c])

result = sum(map(lambda n: n + 1, min_value))
print(f"Part 1 solution: {result}")


##################
# --- Part 2 --- #
##################

###(Note: Some of the above code repeats below.) ###

basin_areas = []
min_value = []
# Generator
cg = gen_coords(n_rows, n_cols)
for r, c in cg:
    all_dirs = []
    if r - 1 >= 0:
        all_dirs.append(matrix[r-1][c])
    if r + 1 < n_rows:
        all_dirs.append(matrix[r+1][c])
    if c - 1 >= 0:
        all_dirs.append(matrix[r][c-1])
    if c + 1 < n_cols:
        all_dirs.append(matrix[r][c+1])
    
    if matrix[r][c] < min(all_dirs):
        min_value.append(matrix[r][c])
        current_basin = [[r, c]]
        for r, c in current_basin:
            if r - 1 >= 0  and matrix[r-1][c] < 9:
                if not [r-1, c] in current_basin:
                    current_basin.append([r-1, c])
            if r + 1 < n_rows and matrix[r+1][c] < 9:
                if not [r+1, c] in current_basin:
                    current_basin.append([r+1, c])
            if c - 1 >= 0 and matrix[r][c-1] < 9:
                if not [r, c-1] in current_basin:
                    current_basin.append([r, c-1])
            if c + 1 < n_cols and matrix[r][c+1] < 9:
                if not [r, c+1] in current_basin:
                    current_basin.append([r, c+1])
        basin_areas.append(len(current_basin))


basin_areas.sort(reverse=True)
result = 1
for i in range(3):
    result *= basin_areas[i]
print(f"Part 1 solution: {result}")