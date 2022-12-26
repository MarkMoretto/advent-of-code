#!/bin/python

from collections import defaultdict, deque
from itertools import count, product, starmap
from operator import add

class Vector(tuple):
    def __add__(self, other):
        return Vector(starmap(add, zip(self, other)))


def V(*args):
    return Vector(args)


DIRS = N, S, W, E, NE, NW, SE, SW = (
    V(-1, 0), V(1, 0), V(0, -1), V(0, 1),
    V(-1, 1), V(-1, -1), V(1, 1), V(1, -1)
)

CHECK = deque([(N, NE, NW), (S, SE, SW), (W, NW, SW), (E, NE, SE)])

elves = set()
elves.add(V(1,2))
elves.add(V(1,3))
elves.add(V(2,2))
elves.add(V(3,2))
elves.add(V(3,3))

for elf in elves:
    for d in DIRS:
        print(elf, d, elf + d)
