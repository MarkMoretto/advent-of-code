#!/bin/python

import re
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day05-sample.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()
lines = data.splitlines()

[re.search(r"(\d+,\d+)\s*\W+\s*(\d+,\d+)", line).groups() for line in lines]

class Point:
    __slots__ = ["X", "y",]
    def __init__(self, X: int, y: int) -> None:
        self.X = X
        self.y = y

    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.X}, {self.y})>"

class Vector:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def __repr__(self):
        return f"""
        <Vector
            start: {self.start}
            end:   {self.end}
        />"""

# Distance formulae
def euclidean_dist(p1: Point, p2: Point) -> float:
    return ((p1.X - p2.X)**2 + (p1.y - p2.y)**2)**(1/2)

def taxicab_dist(p1: Point, p2: Point) -> int:
    return abs(p1.X - p2.X) + abs(p1.y - p2.y)

# p1 = Point(0, 9)
# p2 = Point(5, 9)
# euclidean_dist(p1, p2)


def valid_pair(src: Point, dest: Point) -> bool:
    return src.X == dest.X or src.y == dest.y

# Regular expression to capture relevant data.
re_pattern = r"(\d+,\d+)\s*\W+\s*(\d+,\d+)"
p = re.compile(re_pattern, flags = re.I)

# Create a list of Vectors
def create_vectors(value_list: list) -> list:
    _vectors = []
    for line in value_list:
        res = p.search(line)
        if res:
            coord_set = list(map(lambda s: list(map(int, str(s).split(","))), res.groups()))
            p1, p2 = [Point(*c) for c in coord_set]
            if valid_pair(p1, p2):
                _vectors.append(Vector(p1, p2))
    return _vectors

vectors = create_vectors(lines)

def valid_vec(src: Point, dest: Point) -> bool:
    return src.X == dest.X or src.y == dest.y


w, h = 9, 9
grid = dict()
for i in range(h + 1):
    for j in range(w + 1):
        grid[(i,j)] = "."
