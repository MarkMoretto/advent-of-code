#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 13
Date: 2021-12-13
URL: https://adventofcode.com/2021/day/13
Contributor(s):
    mark moretto
"""

from __future__ import annotations

from typing import Set

# Locals
from helpful.fs import get_data
from helpful.types import *

# Get data
AOC_DAY: int = 13
USE_SAMPLE_TF: bool = False

raw_data = get_data(AOC_DAY, USE_SAMPLE_TF)
coords, folds = raw_data.split("\n"*2)

# Creating a dictionary for keeping fold sequences in order
# even though a list would also probably work.
folds_map = dict()
for fold_nr, f in enumerate(str(folds).splitlines()):
    tmp = int(f.split("=")[1])
    folds_map[fold_nr] = dict(name="", value=0)
    if "x" in f:
        folds_map[fold_nr]["name"] = "c"
    else:
        folds_map[fold_nr]["name"] = "r"
    folds_map[fold_nr]["value"] = tmp



class PointBase:
    __slots__ = ["c", "r"]

    """Point base class."""

    def __init__(self, c: int, r: int) -> None:
        self.c = c
        self.r = r

    def __eq__(self, other):
        return self.c == other.c and self.r == other.r

    def __hash__(self):
        """Standard hash implementation.  Required for using in Sets and
        other collections were elements should be hashable.
        """
        return hash(str(self))
    
    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.c}, {self.r})>"

# Implemented point class.
class Point(PointBase): pass


# --- Create set of points --- #
points = set()
for coord in coords.splitlines():
    points.add(
        Point(*map(int, coord.split(",")))
    )


# --- Dual-purpose algorithm. --- #

# Variable part_1_tf (bool) - When set to 'True'
# the process will exit after the first fold has ompleted.
# If set to 'False', all of the folds will run for part 2.

part_1_tf: bool = False
fold_count = 0
worker_points = points
for fold_info in folds_map.values():
    # If part 1, break after first iteration
    # Otherwise, set `points` to
    # new `folded_points` data set.    
    if fold_count > 0 and part_1_tf:
        break

    # Capture the current type and value for the fold
    # instruction.
    fold_type = fold_info["name"]
    fold_value = fold_info["value"]

    # Set factor to subtract r or c value from for readjustment.
    max_factor = fold_value * 2
    fold_count += 1

    # -- Use new folded_points variable for each fold event.
    # Using a set collection will limit points to unique values
    # which will account for any point "overlaps" during a fold.
    folded_points = set()

    # Iterate remaining points and use logic to determine whether
    # the point should be folkded or left alone.  In either case,
    # the point will be added to the folded_points set.
    for pt in worker_points:
        if fold_type == "r":
            if pt.r > fold_value:
                pt = Point(pt.c, max_factor - pt.r)
            folded_points.add(pt)
        elif fold_type == "c":
            if pt.c > fold_value:
                pt = Point(max_factor - pt.c, pt.r)
            folded_points.add(pt)
    
    # The worker_points variable will update to the new folded_points
    # result, then run through the process again with a new fold.
    worker_points = folded_points

# Output different results based on part 1 or part 2.
if part_1_tf:
    result = len(folded_points)
    print(f"Part 1 result: {result}")
else:
    result = len(folded_points)
    print(f"Part 1 result:\n\n{result}")
