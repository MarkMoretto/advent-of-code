#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 17
Date: 2021-12-17
URL: https://adventofcode.com/2021/day/17
Contributor(s):
    mark moretto
"""

from __future__ import annotations

import re

# Locals
from helpful.fs import get_data
from helpful.types import *


# Get data
AOC_DAY: int = 17
USE_SAMPLE_TF: bool = False
raw_data = get_data(AOC_DAY, USE_SAMPLE_TF)

# Import data
res = re.search(r"x=(-?\d+)\.+(-?\d+).+y=(-?\d+)\.+(-?\d+)", raw_data)
if res:
    X_min, X_max, y_max, y_min = map(int, res.groups())


class Point:
    """Flexible Point class.  Implements hashing, comparisons, etc.
    """
    def __init__(self, X: int, y: int) -> None:
        self.X = X
        self.y = y
        self.dist1 = None
        self.dist2 = None
    
    @property
    def X_abs(self):
        return abs(self.X)

    @property
    def y_abs(self):
        return abs(self.y)
    
    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other):
        """Equal."""
        return self.X_abs == other.X_abs and self.y_abs == other.y_abs
    
    def __ne__(self, other):
        """Not equal."""
        return self.X_abs != other.X_abs or self.y_abs != other.y_abs
    
    def __lt__(self, other):
        """Less than."""
        if not self.dist1:
            self.__get_distances(other)
        return self.dist1 < self.dist2

    def __le__(self, other):
        """Less than or equal."""
        if not self.dist1:
            self.__get_distances(other)        
        return self.dist1 <= self.dist2
    
    def __gt__(self, other):
        """Greater than."""
        if not self.dist1:
            self.__get_distances(other)
        return self.dist1 > self.dist2

    def __ge__(self, other):
        """Greater than or equal."""
        if not self.dist1:
            self.__get_distances(other)        
        return self.dist1 >= self.dist2

    def __str__(self):
        return f"({self.X}, {self.y})"

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"<{cls_name} ({self.X}, {self.y}) />"

    @staticmethod
    def taxicab_dist(p1: Point, p2: Point) -> float:
        return abs(p1.X - p2.X) + abs(p1.y - p2.y)

    def __get_distances(self, other):
        origin = Point(0, 0)
        self.dist1 = self.taxicab_dist(self, origin)
        self.dist2 = self.taxicab_dist(other, origin)


    def move(self, other: Point):
        self.X += other.X
        self.y += other.y


##################
# --- Part 1 --- #
##################

result = (y_max * (y_max - -1))//2
print(f"Part 1 result: {result}")


# Alt method: iterative, but the same concept.
def part_1_alt():
    y_hat = -y_min-1
    y_accum = 0
    while y_hat:
        y_accum += y_hat
        y_hat -=1
    print(f"Part 1 result: {y_accum}")


##################
# --- Part 2 --- #
##################

### Little more involved.


# Set min and max points.
min_Xy = Point(X_min, y_min)
max_Xy = Point(X_max, y_max)


def update_vector(p: Point):
    """Update velocity vector according to specification.
    """
    p.X = min([0, p.X-1])
    p.y -= 1


def check_hit(pt: Point, min_pts: Point = min_Xy, max_pts: Point = max_Xy) -> bool:
    """Check if point falls within targeted area."""
    X_check: bool = min_pts.X <= pt.X <= max_pts.X
    y_check: bool = min_pts.y <= pt.y <= max_pts.y
    return X_check and y_check


def flight_path(v: Point, min_pts: Point = min_Xy, max_pts: Point = max_Xy) -> Iterator:
    """Return reasonable trajectory path for vessel.
    """
    ship_pos = Point(0, 0)
    while ship_pos.X <= max_pts.X and ship_pos.y >= min_pts.y:
        yield ship_pos
        ship_pos.move(v)
        update_vector(v)


def run_simulation():
    """Run through velocity pairs within given range
    and return number of successes.
    """
    is_hit: bool = False
    hit_count = 0
    # hit_list = []
    for x in range(max_Xy.X+1):
        for y in range(min_Xy.y, -min_Xy.y):
            is_hit = False
            velocity = Point(x, y)
            for p in flight_path(velocity):
                if check_hit(p):
                    is_hit = True
                    break
            
            if is_hit:
                # hit_list.append(Point(x,y))
                hit_count += 1
    return hit_count

result = run_simulation()
print(f"Part 2 result: {result}")



