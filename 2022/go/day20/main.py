#!/bin/python
from functools import partial

# https://github.com/Phil-DS/AdventOfCode2022/blob/master/day18/day18_2.py

rsorted = partial(sorted, reverse=True)

def to_ints(s: str)  -> tuple:
    return tuple(map(int, s.split(",")))

dirs = set([
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (-1,0,0),
    (0,-1,0),
    (0,0,-1),
])

def tot_sides(pts: set) -> int:
    tot = 0
    for x, y, z in pts:
        tot += 6
        for a, b, c in dirs:
            if (x+a, b+y, c+z) in pts:
                tot -= 1
    return tot

def get_max_point(pts: set) -> tuple:
    max_x = rsorted(points, key=lambda p: p[0])[0]
    max_y = rsorted(points, key=lambda p: p[1])[0]
    max_z = rsorted(points, key=lambda p: p[2])[0]
    max_pt = max_x[0], max_y[1], max_z[2]
    return max_pt

if __name__ == "__main__":
    points = set()
    with open("data.in") as f:
        for line in list(f):
            line = line[:-1]
            points.add(to_ints(line))
    # Part 1
    part_1 = tot_sides(points)
    # print(part_1)

    # Part 2
    max_pt = get_max_point(points)
    rng_a, rng_b, rng_c = range(max_pt[0]+1), range(max_pt[1]+1), range(max_pt[2]+1)
    surfaces = {(a, b, c) for a in rng_a for b in rng_b for c in rng_c}

    open_space = list(surfaces-points)
    pockets = list()
    visited = list()
    while len(open_space):
        visited.append(open_space[0])
        curr_pocket = set()
        while len(visited):
            next_pocket = visited.pop()
            if next_pocket in open_space:
                curr_pocket.add(next_pocket)
                open_space.remove(next_pocket)
                a, b, c = next_pocket
                for x, y, z in dirs:
                    visited.append(tuple([a+x,b+y,c+z]))

        if not (0, 0, 0) in curr_pocket:
            pockets.append(curr_pocket)
    
    # part_1 = tot_sides(points)
    part_2 = sum(map(tot_sides, pockets))
    print(part_1-part_2)
