#!/bin/python
from __future__ import annotations

def parse_input(s: str):
    action, amount = s.split()
    return action, int(amount)

class Point:
    r: int
    c: int

class Coord(Point):
    def __init__(self, r, c) -> None:
        self.r = r
        self.c = c

    def __eq__(self, other: Coord) -> bool:
        return self.r == other.r and self.c == other.c

#TODO: Distance between
#TODO: Move t

movemap = {
    "R": Coord(0, 1),
    "L": Coord(0, -1),
    "U": Coord(1, 0),
    "D": Coord(-1, 0),
}

if __name__ == "__main__":

    t = Coord(0, 0)
    h = Coord(0, 0)
    assert t == h

    t_hist = [t]

    with open("data-sm.in") as f:
        for line in f.readlines():
            print(f"{h.r}, {h.c}")
            act, amt = parse_input(line)
            d = movemap.get(act)
            h.r += (d.r * amt)
            h.c += (d.c * amt)

