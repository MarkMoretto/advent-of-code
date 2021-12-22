#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 21
Date: 2021-12-21
URL: https://adventofcode.com/2021/day/21
Contributor(s):
    mark moretto
"""

from __future__ import annotations

from itertools import cycle, product
from collections import defaultdict, deque
# from random import randrange

# Locals
from helpful.fs import get_data, get_local_data
from helpful.types import *


# Get data
AOC_DAY: int = 21
USE_SAMPLE_TF: bool = True
raw_data = get_local_data(AOC_DAY, USE_SAMPLE_TF)
p1_start, p2_start = [int(line.split(": ")[1]) for line in raw_data.splitlines()]

# Max score before game ends
TERMINAL_SCORE: int = 1000

# Three folls of a die.
roll_3 = lambda d: [next(d) for _ in range(3)]

# Using deque for rotation method.
GAME_BOARD = deque(range(1, 11), maxlen=10)


# Initial variables and constructs.
scores = [0, 0] # p1, p2
boards = [
    GAME_BOARD.copy(),
    GAME_BOARD.copy(),
]
# Rotate each board to starting position.
boards[0].rotate(-p1_start+1)
boards[1].rotate(-p2_start+1)

# Initialize die and set initi counts and player variable, p.
die = cycle(range(1, 101))
roll_count = 0
p = 0
while max(scores) < TERMINAL_SCORE:
    player_idx = p%2
    for v in roll_3(die):
        boards[player_idx].rotate(-v)
        roll_count += 1
    scores[player_idx] += boards[player_idx][0]
    p += 1

result = roll_count * min(scores)
print(f"Part 1 result: {result}")
