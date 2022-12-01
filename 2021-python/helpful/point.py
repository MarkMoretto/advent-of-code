#!/bin/python

__all__= [
    "Point",
    "sort_points"
    ]

from typing import List
from abc import ABC, abstractmethod

class IPointRC(ABC):
    @property
    @abstractmethod
    def r(self):
        pass

    @r.setter
    @abstractmethod
    def r(self, value):
        pass

    @property
    @abstractmethod
    def c(self):
        pass

    @c.setter
    @abstractmethod
    def c(self, value):
        pass        

class IPointNavigation(ABC):
    @abstractmethod
    def up(self, amount):
        pass
    
    @abstractmethod
    def down(self, amount):
        pass

    @abstractmethod
    def left(self, amount):
        pass

    @abstractmethod
    def right(self, amount):
        pass

    @abstractmethod
    def move(self, other):
        pass


class PointBase(IPointRC):
    """Base point class.  Defines column and row variables
    as well as various comparisons to other points.
    """

    def __init__(self, c: int, r: int) -> None:
        self.__c = c
        self.__r = r
    
    @property
    def r(self):
        return self.__r
    
    @r.setter
    def r(self, value):
        if not isinstance(value, int):
            raise ValueError("Integer type expected.")
        self.__r = value

    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self, value):
        if not isinstance(value, int):
            raise ValueError("Integer type expected.")
        self.__c = value        

    def __hash__(self):
        """Hashing method."""
        return hash(str(self))
    
    def __eq__(self, other):
        """Equal."""
        return self.c == other.c and self.r == other.r
    
    def __ne__(self, other):
        """Not equal."""
        return self.c != other.c or self.r != other.r
    
    def __lt__(self, other):
        """Less than."""
        return (self.c < other.c and self.r <= other.r
            or self.c <= other.c and self.r < other.r)

    def __le__(self, other):
        """Less than or equal."""
        return self.c <= other.c and self.r <= other.r
    
    def __gt__(self, other):
        """Greater than."""
        return (self.c > other.c and self.r >= other.r
            or self.c <= other.c and self.r > other.r)

    def __ge__(self, other):
        """Greater than or equal."""
        return self.c >= other.c and self.r >= other.r

    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.c}, {self.r})>"

class PointNavigationMixin(IPointNavigation):
    """Base point nabvigation class.  Will implement
    """    
    # Moving on normal Cartesian grid.
    def up(self, amount: int = 1):
        self.r -= amount

    def down(self, amount: int = 1):
        self.r += amount

    def left(self, amount: int = 1):
        self.c -= amount

    def right(self, amount: int = 1):
        self.c += amount

    def move(self, other: PointBase):
        self.c += other.c
        self.r += other.r

class Point(PointBase, PointNavigationMixin): pass


# --- Various helper functions --- #
def sort_points(p: List[Point], descending: bool = False, col_then_row: bool = True):
    if col_then_row:
        fn = lambda pt: (pt.c, pt.r)
    else:
        fn = lambda pt: (pt.r, pt.c)
    return sorted(p, key = fn, reverse=descending)