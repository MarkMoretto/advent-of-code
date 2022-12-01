#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 11
Date: 2021-12-11
URL: https://adventofcode.com/2021/day/11
Contributor(s):
    mark moretto
"""

# from copy import deepcopy
# from functools import partial
from pathlib import Path

from typing import Dict, Iterator, List, Union

DATA_DIR = Path("data")

# Types
String = str
Integer = int
Float = float
Number = Union[int, float]
IntList = List[Integer]
NumList = List[Number]

Matrix = List[IntList]

# Get data
AOC_DAY: int = 11
USE_SAMPLE_TF: bool = False

DATA_FILE_A = DATA_DIR.joinpath(
    f"day{AOC_DAY:0>2}{'-sample' if USE_SAMPLE_TF else ''}.txt"
    )
raw_data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()

# DIRECTIONS = set([
#     (-1,-1),
#     (1, 1),
#     (-1, 0),
#     (1, 0),
#     (-1, 1),
#     (1, -1),
#     (0, -1),
#     (0, 1),])

def reset_octopi(string: str=raw_data) -> dict:
    return {(x,y): int(energy) for x, line in enumerate(string.splitlines()) \
        for y, energy in enumerate(line.strip())}

H = W = 10

# def get_neighbors(R,C, __cache={}):
#     __hash = (R,C)
#     if not __hash in __cache:
#         __cache[__hash] = [(R+d[0], C+d[1]) for d in DIRECTIONS \
#                             if 0<=(R+d[0])<H and 0<=(C+d[1])<W]
#     return __cache[__hash]


dirs = [-1,0,1]
octopi = reset_octopi()

def f():
    uu = {}
    m = lambda p: octopi[p]+1 + sum(map(lambda i: i in uu,[(p[0]+a,p[1]+b) for a in dirs for b in dirs]))
    llen = -1
    while len(uu)>llen:
        llen = len(uu)
        uu = set(q for q in octopi if m(q)>9)
    return {k:0 if k in uu else m(k) for k in octopi}, len(uu)

buff=[]
cnt=0
while len(octopi)>cnt:
    octopi,cnt=f()
    buff+=[cnt]

result = sum(buff[:100])
print(f"Part 1 result: {result}")
print(f"Part 2 result: {len(buff)}")


# flash_count=0
# agg_flash=0
# for s in range(1, 11):
#     to_flash, flashed = set(), set()

#     u = {}
#     m = lambda p: octopi[p]+1 + sum(map(lambda i: i in u,[(p[0]+a,p[1]+b) for a in dirs for b in dirs]))
#     llen = -1
#     while

#     # Increment energy for all.
#     for i in octopi:
#         octopi[i]+=1
#         if octopi[i]>9:
#             to_flash.add(i)

#     while to_flash:
#         o = to_flash.pop()
#         octopi[o] = 0
#         flashed.add(o)

#         for n in get_neighbors(*o):
#             octopi[n] += 1
#             if octopi[n]>9:
#                 to_flash.add(n)
            
#     if s<=10:
#         flash_count += len(flashed)
#         agg_flash += sum([octopi[o] for o in flashed])

#     # if sum(octopi.values())==0:
#     #     print(s)
#     #     break

# print(flash_count)



