#!/usr/bin/env python

from typing import List
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day2.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read().splitlines()

   
class Action:
    """Class Action: Object for holding action event for moving submarine.
    """
    __slots__ = ["direction", "amount"]
    def __init__(self, direction: str, amount: int) -> None:
        self.direction = direction
        self.amount = amount


class Submarine:
    def __init__(self, depth: int = 0, horiz: int = 0) -> None:
        self.depth: int = 0
        self.horiz: int = 0

    def forward(self, amount: int = 1):
        self.horiz += amount

    def backward(self, amount: int = 1):
        self.horiz -= amount

    def down(self, amount: int = 1):
        self.depth += amount

    def up(self, amount: int= 1):
        self.depth -= amount
    
    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.horiz}, {self.depth}) />"

    def __str__(self):
        return f"({self.horiz}, {self.depth})"

    def move(self, a: Action) -> None:
        """Move sub in a given direction by a given amount."""
        if a.direction == "down":
            self.down(a.amount)
        elif a.direction == "up":
            self.up(a.amount)
        elif a.direction == "forward":
            self.forward(a.amount)
        else:
            self.backward(a.amount)

    @property
    def result(self):
        return self.depth * self.horiz

# Test Data 
raw_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".strip().splitlines()

# Unpopulated list
moves: List[Action] = []

def parse_moves(d: str, m: List[Action]) -> None:
    if isinstance(d, str):
        d = d.strip().splitlines()
    
    for line in d:
        d, a = line.split()
        moves.append(Action(d, int(a)))

# -- Part 1 -- #
parse_moves(data, moves)

def run(moves_list: List[Action]):
    s = Submarine()
    for M in moves_list:
        s.move(M)
    print(s.result)

run(moves)

# --- Part 2 --- #
class Submarine:
    def __init__(self, depth: int = 0, horiz: int = 0) -> None:
        self.depth: int = 0
        self.horiz: int = 0
        self.aim: int = 0

    def forward(self, amount: int = 1):
        self.horiz += amount
        self.depth += (self.aim * amount)

    def backward(self, amount: int = 1):
        self.horiz -= amount

    def down(self, amount: int = 1):
        # self.depth += amount
        self.aim += amount

    def up(self, amount: int= 1):
        # self.depth -= amount
        self.aim -= amount
    
    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.horiz}, {self.depth}) : {self.aim} />"

    def __str__(self):
        return f"({self.horiz}, {self.depth}) : {self.aim}"

    def move(self, a: Action) -> None:
        """Move sub in a given direction by a given amount."""
        if a.direction == "down":
            self.down(a.amount)
        elif a.direction == "up":
            self.up(a.amount)
        elif a.direction == "forward":
            self.forward(a.amount)
        else:
            self.backward(a.amount)

    @property
    def result(self):
        return self.depth * self.horiz


# -- Part 1 -- #
def test_part_2():
    moves: List[Action] = []
    parse_moves(raw_data, moves)

    s = Submarine()
    s.move(moves[0])
    print(s)
    s.move(moves[1])
    print(s)
    s.move(moves[2])
    print(s)
    s.move(moves[3])
    print(s)
    s.move(moves[4])
    print(s)
    s.move(moves[5])
    print(s)


moves: List[Action] = []
parse_moves(data, moves)

run(moves)