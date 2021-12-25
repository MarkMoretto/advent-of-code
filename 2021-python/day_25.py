#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 25
Date: 2021-12-25
URL: https://adventofcode.com/2021/day/25
Contributor(s):
    mark moretto
"""

from __future__ import annotations

from functools import partial
from collections import defaultdict
from copy import deepcopy

# Locals
from helpful.fs import get_data
from helpful.types import *

# Get data
AOC_DAY: int = 25
USE_SAMPLE_TF: bool = False
raw_data = get_data(AOC_DAY, USE_SAMPLE_TF)


# --- Functions --- #
def _get_tracker(h: Integer, w: Integer) -> Grid:
    return [[0 for _ in range(w)] for _ in range(h)]

def ravel(data_list: Grid) -> IntList:
    return [x for y in data_list for x in y]

def view(g: Grid) -> None:
    print("\n" + "\n".join(["".join(line) for line in g]) + "\n")


def _locations(cucumber: str, locationmap: Dict[set], data_grid: Grid, H: int, W: int) -> Grid:
    """Get locations of desired sea cucumbers."""
    locationmap[cucumber].clear()
    for r in range(H):
        for c in range(W):
            if data_grid[r][c] == cucumber:
                locationmap[cucumber].add((r, c))


# --- Parsing board --- #
base_grid: Grid = [list(line) for line in raw_data.splitlines()]
height: Integer = len(base_grid)
width: Integer = len(base_grid[0])

# -- Partial funcs with known grid dimensions.
get_tracker = partial(_get_tracker, h = height, w = width)
locations = partial(_locations, H = height, W = width)


# Sea cucumber types.
cuke_moves = ">", "v"


# Create a tracking collection.
locs = defaultdict(set)
for cuke in cuke_moves:
    locs[cuke] = set()


if __name__ == "__main__":

    # Copy base grid.
    grid = deepcopy(base_grid)  

    # Update known locations map
    for cuke in cuke_moves:
        locations(cuke, locs, grid)

    # Number of steps taken
    steps = 0

    # Run-stop variable
    no_step_made = False

    while True:
    # for step in range(4):
        if no_step_made:
            break

        # Copy grid for step manipulation
        prev_grid = deepcopy(grid)

        # Get fresh tracking grid.
        tracker = get_tracker()
        tracker = 0

        # Iterate over each cucumber move and known locations
        # to help shorten process.
        for cuke in cuke_moves:
            # Copy grid
            # Prev_grid will be used to update grid.
            prev_grid = deepcopy(grid)

            coords = deepcopy(locs[cuke])
            for coord in coords:
                # Unpack row, column (for clarity)
                r, c = coord

                # Set next row, col coordinate.
                if cuke == ">":
                    rr = r
                    cc = 0 if c+1 == width else c+1
                else:
                    rr =  0 if r+1 == height else r+1
                    cc = c

                # Move to open spot if available
                if prev_grid[rr][cc] in ("."):
                    # Move cucumber and set prior place to empty indicator.
                    grid[rr][cc] = cuke
                    grid[r][c] = "."

                    # Update locs collection
                    # Remove old coordinate and add new coordinate.
                    locs[cuke].remove(coord)
                    locs[cuke].add((rr, cc))
                    
                    # Update tracker
                    tracker += 1
        
        steps += 1

        # If no steps made, exit loop.
        if tracker == 0:
            no_step_made = True

    print(f"Exited after {steps} steps.")
