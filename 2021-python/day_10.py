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

# --- Get data --- #
AOC_DAY: int = 10
USE_SAMPLE_TF: bool = False

DATA_FILE_A = DATA_DIR.joinpath(
    f"day{AOC_DAY:0>2}{'-sample' if USE_SAMPLE_TF else ''}.txt"
    )
raw_data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()

lines = raw_data.splitlines()

# --- Helper functions
def view(d: deque) -> None:
    """Print enumerated deque elements."""
    print("\n".join(f"{i:<4}{v}" for i, v in enumerate(d)))

def spacy(iterable) -> None:
    """Print single-whitespace separated elements."""
    print(" ".join(list(iterable)))

def pprint(d: dict) -> None:
    """Print dictionary items to individual lines."""
    print("\n".join(map(lambda k,v: f"{k} : {v}", d.keys(), d.values())))


# Bracket pairs and maps.
bracket_pairs = r"<> {} [] ()".split()
bracket_map = {b[0]:b[1] for b in bracket_pairs}
inv_bracket_map = {v:k for k, v in bracket_map.items()}
open_bracks = set(bracket_map.keys())
close_bracks = set(bracket_map.values())


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

# Get remaining list items.
lines_2 = [line for i, line in enumerate(lines) if not i in corrupted_lines]

# Updated value map for Part 2
value_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def calc_score(missing: str, score_map: dict = value_map) -> int:
    """Returns cumulative score for all missing items."""
    scr = 0
    for m in missing:
        scr *= 5
        scr += score_map[m]
    return scr

def get_middle_score(items: list) -> int:
    """Return middle score from list of scores.  Total item count
    for list should be odd.
    """
    middle = (len(items) // 2)
    return items[middle]

# Hold results for each line.
results = list()
for line in lines_2:
    # We will continue replacing all valid bracket pairs
    # untill there are no more replacements to be made.
    while True:
        if not any(b in line for b in bracket_pairs):
            break
        else:
            for b in bracket_pairs:
                if b in line:
                    line = line.replace(b, "")

    # Reverse the list and concatenate into a string.
    missing_brackets = "".join([bracket_map[b] for b in line[::-1]])

    # Append key-map for scores and missing brackets to results list.
    results.append({
        "missing_brackets": missing_brackets,
        "score": calc_score(missing_brackets)
    })

# Retrieve all scores and sort
scores = [r["score"] for r in results]
scores.sort(reverse=True)

# Find middle value as result and send to stdout.
result = get_middle_score(scores)
print(f"Part 2 solution: {result}")

