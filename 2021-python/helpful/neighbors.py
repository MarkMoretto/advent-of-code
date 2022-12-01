# -*- coding: utf-8 -*-

"""Module for neighbor-generation helper functions.
"""

from __future__ import annotations

from .types import Callable, Iterator, List
from .point import Point

# Aliases (don't do this)
R = range

# --- Constants --- #
# No diagonals.
SQUARE_DIRS: tuple = tuple([
    (-1, 0)
    ( 1, 0),
    ( 0,-1),
    ( 0, 1),
])

# Including diagonals.
ALL_DIRS: tuple = tuple([
    (-1,-1),
    (1,1),
    (-1,1),
    (1,-1),
    (-1,0),
    (1,0),
    (0,-1),
    (0,1),
])

# Comparison functions
square_fn = lambda x, y: abs(x) != abs(y)
all_fn = lambda a, b: a != 0 or b != 0

# Runtime creation.
RANGE = range(-1, 2)
square_dirs = [Point(x, y) for y in RANGE for x in RANGE if abs(x) != abs(y)]
all_dirs = [Point(x, y) for y in RANGE for x in RANGE if x != 0 or y != 0]



# Generators
def gen_directions(func: Callable = all_fn):
    """Generate directional points.
    Parameters
    ----------
    func : Callable
        Constraint function on X and y values to limit output.
        Possible options are: all_fn (defualt), square_dirs.
        
        all_fn ----> All directions around a given point, including diagonal.
        square_fn -> Only directions up, down, left, and right of a point.
    
    Returns
    -------
    Iterator
        Generator for all direction points that constraint specified in func parameter.

    Examples
    --------
    >>> list(gen_directions())
    [<Point (-1, -1)>,
     <Point (0, -1)>,
     <Point (1, -1)>,
     <Point (-1, 0)>,
     <Point (1, 0)>,
     <Point (-1, 1)>,
     <Point (0, 1)>,
     <Point (1, 1)>]
    """
    g = iter((x, y) for y in RANGE for x in RANGE if func(x, y))
    for d in g:
        yield Point(d[0], d[1])
    return


def xy_generator() -> Iterator:
    return iter((x, y) for y in R(-1, 2) for x in R(-1, 2))

class DirectionType:
    SQUARE: List[Point]
    ALL: List[Point]


class DirectionConstraintFuncs:
    # Comparison functions
    @staticmethod
    def fn_square(a, b) -> bool:
        return abs(a) != abs(b)
    
    @staticmethod
    def fn_all(a, b) -> bool:
        return a != 0 or b != 0


class DirectionMixin(DirectionConstraintFuncs):
    def __init__(self) -> None:
        pass

    def get_square(self) -> List[Point]:
        """Return square directions."""
        return [Point(x, y) for x, y in xy_generator() if self.fn_square(x, y)]
    
    def get_all(self) -> List[Point]:
        """Return all directions."""
        return [Point(x, y) for x, y in xy_generator() if self.fn_all(x, y)]


class Directions(DirectionMixin):
    def __init__(self, is_square: bool):
        """"""
        self.__set_dirs(is_square)

    def __set_dirs(self, option: bool) -> None:
        self.DIRS: List[Point] = []
        if option:
            self.DIRS = self.get_square()
        else:
            self.DIRS = self.get_all()


class Neighbors(Directions):
    """Class to generate coordinates about a point in a Cartesian plane.
    
    Should initialize with the maximum width and height values for
    your given structure.
    """
    def __init__(self, max_width: int, max_height: int, only_square: bool = False) -> None:
        """
        Parameters
        ----------
        max_width : int
            Max number of columns or x-axis values within a structure.
        max_height : int
            Max number of rows or y-axis values within a structure.
        only_square : bool
            Whether to generate neighbors that are above, below, left, or right of a point.
            Default: False.
        """
        self.max_width = max_width
        self.max_height = max_height
        super().__init__(only_square)

    def __width_check(self, value: int) -> bool:
        """Check if column value within spec."""
        return 0 <= value < (self.max_width - 1)

    def __height_check(self, value: int) -> bool:
        """Check if row value within spec."""
        return 0 <= value < (self.max_height - 1)      

    def __gen_neighbors(self, p: Point):
        output = []
        for d in self.DIRS:
            pt = Point(p.c + d.c, p.r + d.r)
            if self.__width_check(pt.c) and self.__height_check(pt.r):
                output.append(pt)
        return output

    def get_neighbors(self, point: Point, __cache = {}):
        if not point in __cache:
            __cache[point] = self.__gen_neighbors(point)
        return __cache[point]    

