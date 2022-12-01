#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 22
Date: 2021-12-22
URL: https://adventofcode.com/2021/day/22
Contributor(s):
    mark moretto
"""

from __future__ import annotations

import re
from collections import Counter
from functools import lru_cache
from itertools import product
# from dataclasses import dataclass # https://docs.python.org/3/library/dataclasses.html

# Locals
from helpful.fs import get_data, get_local_data
from helpful.types import *


# Get data
AOC_DAY: int = 22
USE_SAMPLE_TF: bool = True
raw_data = get_local_data(AOC_DAY, USE_SAMPLE_TF)
lines = raw_data.splitlines()


def to_int(pair: List[str]) -> List[int]:
    """Convert string iterable to integer iterable."""
    return list(map(int, pair))

def get_pairs(s: str) -> list:
    """Parse dimension specifications to list of integer pairs.
    """
    tmp = []
    for item in s.split(","):
        tmp.append(
            to_int(str(item).split("=")[1].split("."*2))
        )
    return [sorted(pair) for pair in tmp]

def ravel(nested_items: Iterable) -> List[int]:
    """Unnest nested items."""
    return [x for y in nested_items for x in y]

def abs_diff(pair: List[int]) -> int:
    return abs(pair[1]-pair[0]) + 1

# def update_minmax(current, mm):
#     if prev_pairs is None:

#     z = zip()
#     [abs_diff(p) for p in pairs]

def constraint_check(*args) -> bool:
    """Part 1: Check if all values fall within specified range.
    """
    return all(map(lambda n: -50 <= n <= 50, args))

minmax = [
    [0, 0],
    [0, 0],
    [0, 0],
    ]


# Iterate when implementing
sample = lines[0]
state, specs = sample.split(" ", maxsplit=1)
pairs = get_pairs(specs)


steps = []
for i, line in enumerate(lines):
    directive, specs = line.split(" ", maxsplit=1)
    pairs = get_pairs(specs)
    all_pairs = ravel(pairs)
    if constraint_check(*all_pairs):
        steps.append(
            dict(
                index = i,
                state = directive,
                pairs = pairs,
                ranges = [set(range(p[0],p[1]+1)) for p in pairs],
                # diffs = [abs_diff(p) for p in pairs],
                )
            )

current_count = 0

p0 = steps[0]["pairs"]
p0_ranges = [set(range(p[0],p[1]+1)) for p in p0]

tmp = 1
for item in p0_ranges:
    tmp *= len(item)
current_count += tmp

#TODO: Figure out 19 updates from p0_ranges
p1 = steps[1]["pairs"]
p1_ranges = [set(range(p[0],p[1]+1)) for p in p1]

a = (11,12,13)
a = (11,12,13)
p = product(range(p1[0][0], p1[0][1]+1), range(p1[1][0], p1[1][1]+1), range(p1[2][0], p1[2][1]+1))
all_values = [x for y in p for x in y]
counts = Counter(all_values)

for el in p:
    print(sorted(el))



for i in range(3):
    p0_ranges[i].update(p1_ranges[i])
    p1_ranges[0].difference(p0_ranges[0])

tmp_minmax = minmax
diffs = [0, 0, 0]
for i, (mm, pair) in enumerate(zip(minmax, p0)):
    tmp_minmax[i][0] -= abs(pair[0] - mm[0])
    tmp_minmax[i][1] += abs(pair[1] - mm[1])


net_min = [0, 0, 0]
net_max = [0, 0, 0]

a_min = [-20, -36, -47]
a_max = [26, 17, 7]
net_min = min(net_min, a_min)
net_max = max(net_max, a_max)
a_net = [abs(b-a) for a, b in zip(a_min, a_max)]
total_dims = a_net[0]*a_net[1]*a_net[2]



b_min = [-20, -21, -26]
b_max = [33, 23, 28]



p1 = steps[1]["pairs"]






"""  Distances
                                        (3, 4, 5)
                                       /
            *      .    .     .     x
        {y} *    .                . .     
            *  .                .   .    * {z}
            *                 .     .  *
            *               .        *
            *             .        *
            *           .        *
            *         .        *
            O  *  *  *  *  *  * {x}
           /
  (0, 0, 0)
"""

class BaseCube:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.xyz = [x, y, z]

    def __repr__(self):
        return f"<Cube ({self.x}, {self.y}, {self.z})>"

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"   

    def __hash__(self) -> int:
        return hash(str(self))

    def __iter__(self):
        for el in self.xyz:
            yield el

    @staticmethod
    def distance(cube_1: BaseCube, cube_2: BaseCube) -> float:
        """Distance between two 3-D points."""
        xx = (cube_2.x - cube_1.x)**2
        yy = (cube_2.y - cube_1.y)**2
        zz = (cube_2.z - cube_1.z)**2
        return (xx + yy + zz) ** (1/2)


class Cube(BaseCube):
    def __init__(self, x: int, y: int, z: int) -> None:
        super().__init__(x, y, z)
        self.origin = BaseCube(0, 0, 0)
    
    def __hash__(self) -> int:
        return hash(str(self))

    @property
    def this_cube(self) -> BaseCube:
        """Return BaseCube with (x, y, z) of current instance.
        """
        return BaseCube(self.x, self.y, self.z)

    def __self_other_dist(self, other: BaseCube):
        _self = self.distance(self.origin, self.this_cube)
        _other = self.distance(self.origin, other)
        return _self, _other
    
    def __eq__(self, other: BaseCube):
        xx: bool = self.x == other.x
        yy: bool = self.y == other.y
        zz: bool = self.z == other.z
        return xx and yy and zz

    def __lt__(self, other: BaseCube):
        dist_self, dist_other = self.__self_other_dist(other)
        return dist_self < dist_other

    def __le__(self, other: BaseCube):
        dist_self, dist_other = self.__self_other_dist(other)
        return dist_self <= dist_other

    def __gt__(self, other: BaseCube):
        dist_self, dist_other = self.__self_other_dist(other)  
        return dist_self > dist_other

    def __ge__(self, other: BaseCube):
        dist_self, dist_other = self.__self_other_dist(other)
        return dist_self >= dist_other


class RegexPattern:
    """Descriptor class for a pre-defined regular expression string.
    """
    # def __new__(cls) -> str:
    def __get__(self, obj, objtype=None) -> str:
        return r"""
            ^(?P<directive>on|off)\s
            \w.(?P<x_lower>-?\d+)\.\.(?P<x_upper>-?\d+),
            \w.(?P<y_lower>-?\d+)\.\.(?P<y_upper>-?\d+),
            \w.(?P<z_lower>-?\d+)\.\.(?P<z_upper>-?\d+)$
        """


class RebootFuncsMixer:
    # Descriptor object
    REGEX_PATTERN = RegexPattern()

    def __init__(self) -> None:
        self.p = re.compile(self.REGEX_PATTERN, flags = re.X | re.M)

    def get_pairs(self, s: str) -> list:
        """Parse dimension specifications to list of integer pairs.
        """
        tmp = []
        for item in s.split(","):
            tmp.append(
                self.to_int(str(item).split("=")[1].split("."*2))
            )
        return [sorted(pair) for pair in tmp]

    @staticmethod
    def to_int(pair: List[str]) -> List[int]:
        """Convert string iterable to integer iterable."""
        return list(map(int, pair))

    @staticmethod
    def ravel(nested_items: Iterable) -> List[int]:
        """Unnest nested items."""
        return [x for y in nested_items for x in y]

    @staticmethod
    def as_range(pair: List[int]) -> Iterator:
        return range(pair[0], pair[1] + 1)
    
    @staticmethod
    def constraint_check(*args) -> bool:
        """Part 1: Check if all values fall within specified range.
        """
        return all(map(lambda n: -50 <= n <= 50, args))

    def parse_step(self, string: str) -> Tuple[range, str]:
        """Return ranges for (x, y, z) along with the specified directive.
        """
        state, specs = string.split(" ", maxsplit=1)
        pairs = self.get_pairs(specs)

        # Part 1 constraint
        all_pairs = self.ravel(pairs)
        if self.constraint_check(*all_pairs):
            return self.as_range(pairs[0]), self.as_range(pairs[1]), self.as_range(pairs[2]), state


class Cuboid(RebootFuncsMixer):
    def __init__(self) -> None:
        super().__init__()
        self.cubes = dict()
        self.__directive = None

    @lru_cache(maxsize=None)
    def __get_cube(self, x, y, z):
        return Cube(x, y, z)

    def set_cubes(self, step_string: str) -> None:
        """Create set of Cubes from Reboot Step string/command.
        """
        try:
            x_rng, y_rng, z_rng, d = self.parse_step(step_string)
            if self.__directive is None:
                self.__directive = d
            for p in product(x_rng, y_rng, z_rng):
                _c = self.__get_cube(*p)
                # Cubes are hashable, so we can set them as keys in
                # a dictionary object and then update the 'state' of
                # the cube, as needed.
                self.cubes[_c] = 1 if d == "on" else 0
        except TypeError:
            self.cubes = None

    @property
    def directive(self) -> str:
        return self.__directive

    def get_state(self, cube) -> int:
        return self.cubes[cube]

    def toggle_state(self, cube) -> None:
        """Flip state of cube."""
        prev_state = self.cubes[cube]
        self.cubes[cube] = 1 - prev_state

    @property
    def cube_list(self):
        """Return list of keys (cubes) in current cube-state mapping.
        """
        return list(self.cubes.keys())

    @property
    def cube_set(self):
        """Return set of keys (cubes) in current cube-state mapping.
        """
        return set(self.cubes.keys())      

    def filter_cubes(self, current_state: int = 1) -> list:
        """Return cubes that are currently on/off (1/0)."""
        return list(k for k, v in self.cubes.items() if v == current_state)
    
    @property
    def active_cubes(self):
        return set(self.filter_cubes(1))

    @property
    def inactive_cubes(self):
        return set(self.filter_cubes(0))

class RebootStep(Cuboid):
    """Reboot Step class.
    """
    def __init__(self, reboot_string: str) -> None:
        super().__init__()
        self.set_cubes(reboot_string)

# Run process
cubes = set()
for step in lines:
    rebooter = RebootStep(step)
    if rebooter.cubes:
        if rebooter.directive == "on":
            cubes.update(rebooter.cube_set)
        else:
            for c in cubes.intersection(rebooter.cube_set):
                cubes.remove(c)

# should be 590784 for larger sample set
len(cubes) # 590784 OK!


rs1 = RebootStep(lines[0])
rs2 = RebootStep(lines[1])
rs3 = RebootStep(lines[2])
rs4 = RebootStep(lines[3])

rsX = RebootStep(lines[-1])

cubes: set = rs1.cube_set
len(cubes) # 27
cubes.update(rs2.cube_set)
len(cubes) # 46
# 46 - 27 == 19
for c in cubes.intersection(rs3.cube_set):
    cubes.remove(c)
len(cubes) # 38
cubes.update(rs4.cube_set)
len(cubes) # 39



# Regex
# re_pattern = r"""
#     ^(?P<directive>on|off)\s
#     \w.(?P<x_lower>\d+)\.\.(?P<x_upper>\d+),
#     \w.(?P<y_lower>\d+)\.\.(?P<y_upper>\d+),
#     \w.(?P<z_lower>\d+)\.\.(?P<z_upper>\d+)$
# """
# p = re.compile(re_pattern, flags = re.X | re.M)

# sample = lines[0]
# res = p.search(sample)
# mres = p.match(sample)
# mres.groupdict()




# FREQS = Counter(a + b + c for a, b, c in product([1, 2, 3], repeat=3))
# list(product((10,11,12),(10,11,12),(10,11,12)))


def get_ranges(s: str) -> Tuple[range]:
    mres = p.match(s)
    d = mres.groupdict()
    x_lo, x_hi = map(int, [d["x_lower"], d["x_upper"]])
    y_lo, y_hi = map(int, [d["y_lower"], d["y_upper"]])
    z_lo, z_hi = map(int, [d["z_lower"], d["z_upper"]])
    return range(x_lo, x_hi+1), range(y_lo, y_hi+1), range(z_lo, z_hi+1)

