#!/bin/python
__all__ = [
    "Point",
    ]

from ._types import Number

class Point3d:
    """3D point object."""
    x: Number
    y: Number
    z: Number

class ExtraAttrs:
    """Attributes object."""
    class_name: str

class BasePoint(Point3d):
    """Base point class. Implements required class methods (dunders).
    """
    def __init__(self, x=-1, y=-1, z=-1) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

    def __repr__(self):
        return f"<P ({self.x}, {self.y}, {self.z}) />"
    
    def __hash__(self):
        return hash(str(self))

    def __dist(self) -> int:
        """Simple distance from origin."""
        return abs(self.x-0)+abs(self.y-0)+abs(self.z-0)

    def __eq__(self, other: Point):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other: Point):
        return self.x != other.x or self.y != other.y or self.z != other.z
    
    def __lt__(self, other: Point):
        return self.__dist() < other.__dist()

    def __le__(self, other: Point):
        return self.__dist() <= other.__dist()

    def __gt__(self, other: Point):
        return self.__dist() > other.__dist()

    def __ge__(self, other: Point):
        return self.__dist() >= other.__dist()


class Point(BasePoint, ExtraAttrs): pass
