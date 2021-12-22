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
from itertools import product
from dataclasses import dataclass # https://docs.python.org/3/library/dataclasses.html

# Locals
from helpful.fs import get_data, get_local_data
from helpful.types import *


# Get data
AOC_DAY: int = 22
USE_SAMPLE_TF: bool = True
raw_data = get_local_data(AOC_DAY, USE_SAMPLE_TF)
lines = raw_data.splitlines()


"""  Distances
                        (3, 4, 5)
                        /
                 . . . x
        {y}     .      .      
            *  .       .      * {z}
            * .        .     *
            *          .    *
            *         .    *
            *        .    *
            *       .    *
            0 * * * * * * {x}
           /
  (0, 0, 0)
"""

class BaseCube:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

class Cube(BaseCube):
    def __init__(self, x: int, y: int, z: int) -> None:
        super().__init__(x, y, z)
        self.origin = BaseCube(0, 0, 0)
    
    def __repr__(self):
        return f"<Cube ({self.x}, {self.y}, {self.z})>"

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"   

    def __hash__(self) -> int:
        return hash(str(self))

    @property
    def this_cube(self) -> BaseCube:
        """Return BaseCube with (x, y, z) of current instance.
        """
        return BaseCube(self.x, self.y, self.z)

    @staticmethod
    def distance(cube_1: BaseCube, cube_2: BaseCube) -> float:
        """Distance between two 3-D points."""
        xx = (cube_2.x - cube_1.x)**2
        yy = (cube_2.y - cube_1.y)**2
        zz = (cube_2.z - cube_1.z)**2
        return (xx + yy + zz) ** (1/2)

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
            \w.(?P<x_lower>\d+)\.\.(?P<x_upper>\d+),
            \w.(?P<y_lower>\d+)\.\.(?P<y_upper>\d+),
            \w.(?P<z_lower>\d+)\.\.(?P<z_upper>\d+)$
        """


class RebootFuncsMixer:
    # Descriptor object
    REGEX_PATTERN = RegexPattern()

    def __init__(self) -> None:
        self.p = re.compile(self.REGEX_PATTERN, flags = re.X | re.M)

    def parse_step(self, s: str) -> Tuple[range, str]:
        """Return ranges for (x, y, z) along with the specified directive.
        """
        mres = self.p.match(s)
        d = mres.groupdict()
        directive = d["directive"]
        x_lo, x_hi = map(int, [d["x_lower"], d["x_upper"]])
        y_lo, y_hi = map(int, [d["y_lower"], d["y_upper"]])
        z_lo, z_hi = map(int, [d["z_lower"], d["z_upper"]])
        return range(x_lo, x_hi+1), range(y_lo, y_hi+1), range(z_lo, z_hi+1), directive



class Cuboid(RebootFuncsMixer):
    def __init__(self) -> None:
        self.cubes = dict()
        super().__init__()

    def set_cubes(self, step_string: str) -> None:
        """Create set of Cubes from Reboot Step string/command.
        """
        x_rng, y_rng, z_rng, d = self.parse_step(step_string)
        for p in product(x_rng, y_rng, z_rng):
            # Cubes are hashable, so we can set them as keys in
            # a dictionary object and then update the 'state' of
            # the cube, as needed.
            self.cubes[Cube(*p)] = 1 if d == "on" else 0

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



sample = lines[0]

rs1 = RebootStep(lines[0])
rs2 = RebootStep(lines[1])


cubes: set = rs1.cube_set
cubes.update(rs2.cube_set)
cubes.difference(rs2.cube_set)
rs2.cube_set.difference(rs1.cube_set)


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

