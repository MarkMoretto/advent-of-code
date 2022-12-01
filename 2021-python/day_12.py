#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 12
Date: 2021-12-12
URL: https://adventofcode.com/2021/day/12
Contributor(s):
    mark moretto

Notes:
    https://en.wikipedia.org/wiki/Graph_traversal
    https://en.wikipedia.org/wiki/Tree_traversal
"""

from __future__ import annotations

from collections import defaultdict, deque

# Locals
from helpful.fs import get_data
from helpful.types import *

# Additional Type for graphs.
Graph =  Dict[str, List[str]]


# Retrieve puzzle data.
AOC_DAY: int = 12
USE_SAMPLE_TF: bool = False
raw_data = get_data(AOC_DAY, USE_SAMPLE_TF)
lines = raw_data.splitlines()


### Create adjacency list
G = defaultdict(list)
for line in lines:
    src,dest = (map(lambda s: str(s).strip(), line.split("-")))
    G[src].append(dest)
    G[dest].append(src)


##################
# --- Part 1 --- #
##################

# Find all paths
def all_paths_1(cave_list: list, graph: Graph):
    tail = cave_list[-1]

    if tail == "end":
        return [cave_list]

    _paths = list()

    for cave in graph[tail]:
        if cave.islower() and cave in cave_list:
            continue
        _paths.extend(all_paths_1(cave_list + [cave], graph))
    return _paths

# Start function with 'seeded' list
# that included the name of the starting cave.
result = all_paths_1(["start"], G)
print(f"Part 1 result: {len(result)}")



##################
# --- Part 2 --- #
##################

def all_paths_2(cave_list: list, graph: Graph, can_revisit: bool = True):
    tail = cave_list[-1]

    if tail == "end":
        return [cave_list]

    _paths = list()

    for cave in graph[tail]:
        # Skip starting node
        if cave == "start":
            continue

        if cave.islower() and cave in cave_list:
            # Lowercase 'cave' that has not been visited yet.
            if can_revisit:
                _paths.extend(
                    # Indicate with next iteration that the cave
                    # can no longer be visited.
                    all_paths_2(cave_list + [cave], graph, False)
                )
        else:
            _paths.extend(
                all_paths_2(cave_list + [cave], graph, can_revisit)
            )
    return _paths

result = all_paths_2(["start"], G)
print(f"Part 1 result: {len(result)}")