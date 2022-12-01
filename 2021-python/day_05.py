#!/bin/python

import re
from pathlib import Path
from math import atan2, pi

DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day05.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()
lines = data.strip().splitlines()


### Creating some classes and mixins because why not. ###

class PointBase:
    __slots__ = ["X", "y"]
    def __init__(self, X: int, y: int) -> None:
        self.X = X
        self.y = y

    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.X}, {self.y})>"

class PointNav:
    # Moving on normal Cartesian grid.
    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1

    def left(self):
        self.X -= 1

    def right(self):
        self.X += 1

    def move(self, other: PointBase):
        self.X += other.X
        self.y += other.y


class Point(PointBase, PointNav):
    def __init__(self, X: int, y: int) -> None:
        super().__init__(X, y)



class CoreMethod:
    """Basic helper functions and methods."""
    @staticmethod
    def net_diff(p1: Point, p2: Point) -> float:
        return (p2.X - p1.X), (p2.y - p1.y)


class DistanceMixin:
    """Various Cartesian plane distance methods."""
    def euclidean(self, p1: Point, p2: Point) -> float:
        delta_x, delta_y = CoreMethod.net_diff(p1, p2)
        return (delta_x**2 + delta_y**2)**(1/2)

    def taxicab(self, p1: Point, p2: Point) -> int:
        delta_x, delta_y = CoreMethod.net_diff(p1, p2)
        return abs(delta_x) + abs(delta_y)


class TrigMixin:
    """Methods to find angle and radians between two points."""
    def __init__(self, start_pt: Point, end_pt: Point) -> None:
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.__set()

    def __set(self):
        """Set various variables after initial points are set."""
        self.delta_x, self.delta_y = CoreMethod.net_diff(self.start_pt, self.end_pt)
        self.radians: float = atan2(self.delta_x, self.delta_y)
        self.angle: int = int((self.radians * 180) / pi)
        self.slope = round(self.delta_y / self.delta_x, 6) if self.delta_x > 0. else 0.


class Vector(DistanceMixin, TrigMixin):
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        super().__init__(self.start, self.end)

    def __repr__(self):
        pp1 = f"{self.start.X}, {self.start.y}"
        pp2 = f"{self.end.X}, {self.end.y}"
        return f"<Vector ({pp1}) ~~> ({pp2}) />"
    
    @property
    def taxicab_dist(self) -> int:
        return self.taxicab(self.start, self.end)


    def __is_negative(self):
        _cond1 = self.start.X > self.end.X
        _cond2 = self.start.y > self.end.y
        return _cond1 or _cond2

    def __is_X_equal(self):
        return self.start.X == self.end.X

    def __is_y_equal(self):
        return self.start.y == self.end.y

    def __create_path(self, rng, _x=None, _y=None):
        for i in rng:
            if _x is None:
                yield Point(i, _y)
            else:
                yield Point(_x, i)
            

    def create_full_path(self):
        """All values between X and y, inclusive of X and y.
        """
        base_pt = self.start
     
        if self.__is_negative():
            base_pt = self.end

        _dist = self.taxicab_dist

        # If X's equal, X will be static and y will change.
        if self.__is_X_equal():
            min_value = base_pt.y
            max_value = base_pt.y + _dist + 1
            _rng = range(min_value, max_value)
            cp = self.__create_path(_rng, _x=base_pt.X)

        # If y's equal, y will be static and X will change.
        elif self.__is_y_equal():
            min_value = base_pt.X
            max_value = base_pt.X + _dist + 1
            _rng = range(min_value, max_value)
            cp = self.__create_path(_rng, _y=base_pt.y)
        
        return list(cp)


########################
# --- Process data --- #

# Regular expression to capture relevant values.
# Probably overkill...
re_pattern = r"(\d+,\d+)\s*\W+\s*(\d+,\d+)"

# Create a list of all processed Vectors
def create_all_vectors(value_list: list) -> list:
    p = re.compile(re_pattern, flags = re.I)
    _vectors = []
    for line in value_list:
        res = p.search(line)
        if res:
            coord_set = list(map(lambda s: list(map(int, str(s).split(","))), res.groups()))
            p1, p2 = [Point(*c) for c in coord_set]
            _vectors.append(Vector(p1, p2))
    return _vectors


def update_grid(xy_hash, grid: dict):
    """Helper function to evaluate and update grid dictionary.
    """
    if not xy_hash in grid:
        grid[xy_hash] = 1
    else:
        grid[xy_hash] += 1 


# -- Part 1 --- #
def valid_pair(src: Point, dest: Point) -> bool:
    """Determine if Points are valid based on condition
    that at least one of X or y pairs must be equal.
    """
    return src.X == dest.X or src.y == dest.y



# Creaet list of all vectors
vectors = create_all_vectors(lines)


# Limit list to part 1 constraint.
p1_vectors = [v for v in vectors if valid_pair(v.start, v.end)]

# Iterate vectors
# Create full path from start to end for each Vector
# Check if immutable point in grid
# If not, add and set to 1
# Otherwise, increment value by 1.
grid = {}
for v in p1_vectors:
    for p in v.create_full_path():
        _hash = (p.X, p.y)
        update_grid(_hash, grid)

# Count grid points with values of two or more.
result = sum([v > 1 for v in grid.values()])
print(f"Part 1 solution: {result}") # 6283



# --- Part 2 --- #

# Mapping of multipliers for 45 and 135-degree angles
# This helps "walk" diagonally to the end point of the vector.
ang_map = {
    45: (1, 1),
    -45: (-1, 1),
    135: (1, -1),
    -135: (-1, -1),    
}


# Fresh grid because it's Sunday and Sunday's are Fresh Grid Days(R).
grid = {}

for v in vectors:
    # Check if angle in map
    if v.angle in ang_map:
        # Set max range for iteration
        abs_dist = abs(v.delta_x) + 1
        # Set base point, which should be the 
        # starting point of the Vector
        base_pt = v.start
        # Capture multipliers for X and y.
        dx, dy = ang_map[v.angle]
        # Iterate range and update grid values as
        # each new coordinate created.
        for i in range(abs_dist):
            _hash = (base_pt.X + i*dx, base_pt.y + i * dy)
            update_grid(_hash, grid)
    else:
        for p in v.create_full_path():
            _hash = (p.X, p.y)
            update_grid(_hash, grid)


result = sum([v > 1 for v in grid.values()])
print(f"Part 1 solution: {result}") # 18864