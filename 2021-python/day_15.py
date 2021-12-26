#!/bin/python

"""
Purpose: Advent of Code 2021 - Day 15
Date: 2021-12-15
URL: https://adventofcode.com/2021/day/15
Contributor(s):
    mark moretto
"""

from __future__ import annotations

from sys import maxsize
from array import array
from heapq import heappop, heappush

# Locals
from helpful.fs import get_data
from helpful.types import *

# Get data
AOC_DAY: int = 15
USE_SAMPLE_TF: bool = False
raw_data = get_data(AOC_DAY, USE_SAMPLE_TF)

matrix = [array("I", map(int, list(r))) for r in raw_data.splitlines()]


class FunctionMixin:

    @staticmethod
    def get_dim(iterable: List[int]) -> int:
        """Return row and column size multipled by a provided scaling factor
        for a 2-D data collection.

        Returns
        -------
        int
            Single dimension multiplied by scaling factor.
        """
        h, w = len(iterable), len(iterable[0])
        if h == w:
            return h
        raise ValueError("Row and column count unequal.")
    

class Solution(FunctionMixin):

    SQUARE_DIRS = [[1,0], [-1,0], [0,1], [0,-1],]

    def __init__(self, m: Matrix, scale_factor: int = 1):
        self._m = m
        self.scale = scale_factor
        #--> Get general dimension and create scaled-up version.
        self.dim = self.get_dim(m)
        self.max_dim = self.dim * scale_factor
        self._divisor = 9

        #--> Worker collections
        #   Priority queue and distance map.
        self._distance_map = {(0, 0): 0}
        self._priority_q = [(0, (0, 0))]


    def _gen_neighbors(self, r, c):
        def _valid(y, x) -> bool:
            """Keep neighbors within limits."""
            return 0 <= x < self.max_dim and 0 <= y < self.max_dim

        all_dirs = [(r+d[0], c+d[1]) for d in self.SQUARE_DIRS]
        return [d for d in all_dirs if _valid(*d)]

    def __divmod(self, v):
        return divmod(v, self.dim)

    def _cost(self, r, c):
        r_div, r_mod = self.__divmod(r)
        c_div, c_mod = self.__divmod(c)
        tmp = self._m[r_mod][c_mod]
        tmp += (r_div + c_div)
        return 1 + (tmp-1) % self._divisor
    
    @property
    def pq_len(self) -> int:
        return len(self._priority_q)

    def djikstras_algo(self):
        """Djikstra's algorithm for finding optimal path."""
        while self.pq_len > 0:
            total, (r, c) = heappop(self._priority_q)
            if total <= self._distance_map[(r, c)]:
                for n in self._gen_neighbors(r, c):
                    this_distance = total + self._cost(*n)
                    if this_distance < self._distance_map.get(n, maxsize):
                        self._distance_map[n] = this_distance
                        heappush(self._priority_q, (this_distance, n))
    
    def run(self):
        self.djikstras_algo()
        return self._distance_map[(self.max_dim-1, self.max_dim-1)]


s1 = Solution(matrix, 1)
result = s1.run()
print(f"Part 1 result: {result}")

s2 = Solution(matrix, 5)
result = s2.run()
print(f"Part 2 result: {result}")



# def this_cost(X, y, divisor=nrc-1):
#     tmp = matrix[y%nrc, X%nrc]
#     tmp += (y//nrc + X//nrc)
#     return 1 + (tmp-1) % divisor
