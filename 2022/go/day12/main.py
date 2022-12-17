#!/bin/python
from typing import List
from collections import namedtuple

IntGrid = List[List[int]]

Point = namedtuple("Point", ["r", "c"])

dirs = Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)


def find_in_grid(g: IntGrid, target: str) -> Point:
    for r in range(len(g)):
        for c in range(len(g[r])):
            if g[r][c] == target:
                return Point(r, c)


def make_grid() -> IntGrid:
    out = []
    with open("data-sm.in") as f:
        for line in f.readlines():
            out.append(list(line))
    return out


def manhattan_dist(p1: Point, p2: Point) -> int:
    return abs(p2.r-p1.r) + abs(p2.c-p1.c)

# def _maybe_okay(neigh: Point):
#     def _inner(current: Point) -> bool:
# def min_dist():



if __name__ == "__main__":
    grid = make_grid()
    l, w = len(grid), len(grid[0])
    pt_start: Point = find_in_grid(grid, "S")
    pt_end: Point = find_in_grid(grid, "E")
    # print(pt_start, pt_end)

