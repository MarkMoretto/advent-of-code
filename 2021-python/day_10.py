#!/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

"""
Purpose: Advent of Code 2021 - Day 10
Date: 2021-12-10
URL: https://adventofcode.com/2021/day/10
Contributor(s):
    mark moretto
"""

import re
from os import linesep
from pathlib import Path
from collections import Counter, deque
from typing import List, Union

DATA_DIR = Path("data")

# Signature Types
String = str
Integer = int
Number = Union[int, float]
NumList = List[Number]

# Get data
AOC_DAY: int = 10
USE_SAMPLE_TF: bool = True

DATA_FILE_A = DATA_DIR.joinpath(
    f"day{AOC_DAY:0>2}{'-sample' if USE_SAMPLE_TF else ''}.txt"
    )
raw_data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()

lines = raw_data.splitlines()


def delete_nth(d, n):
    """Delete nth item from deque."""
    d.rotate(-n)
    _ = d.popleft()
    d.rotate(n)

def view(d: deque) -> None:
    print("\n".join(f"{i:<4}{v}" for i, v in enumerate(d)))

def spacy(iterable) -> None:
    print(" ".join(list(iterable)))

def pprint(d: dict) -> None:
    print("\n".join(map(lambda k,v: f"{k} : {v}", d.keys(), d.values())))


bracket_str = r"<> {} [] ()"
bracket_map = {b[0]:b[1] for b in bracket_str.split()}
open_bracks = set(bracket_map.keys())
close_bracks = set(bracket_map.values())


# line_lengths = {i:len(line) for i, line in enumerate(lines)}


##################
# --- Part 1 --- #
##################

value_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def get_err_score(corruptions: deque, score_map: dict = value_map) -> int:
    return sum(score_map[v] for v in corruptions)

corrupted_lines = deque()
corrupted_chars = deque()
for idx, line in enumerate(lines):
    line = deque(line)
    stacker = deque()
    for b in line:
        if b in open_bracks:
            stacker.append(b)
        elif b in close_bracks:
            prev = stacker.pop()
            expected_curr = bracket_map[prev]
            actual_curr = b
            if expected_curr != b:
                # print(actual_curr, expected_curr, prev)
                corrupted_chars.append(b)
                corrupted_lines.append(idx)
                break

result = get_err_score(corrupted_chars)
print(f"Part 1 solution: {result}")


##################
# --- Part 2 --- #
##################

lines_2 = [line for i, line in enumerate(lines) if not i in corrupted_lines]


