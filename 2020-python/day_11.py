
"""
Purpose: Advent of Code challenge
Day: 11
Date created: 2020-12-10
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from copy import deepcopy
from array import array
from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

else:
    # Current file filepath
    thisfile = current_file(__file__)
    
    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")


# raw_data = read_data(f"day-11-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)
# data = sorted(data)
n_rows, n_cols = len(data), len(data[0])
grid = [list(i) for i in data]
gridsize = n_rows * n_cols


# Adjacency coordinates
adjacency = [[i, j] for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]


def out_of_bounds(coord, direction):
    res = not ((0 <= (coord[0] + direction[0]) < n_rows) and (0 <= (coord[1] + direction[1]) < n_cols))
    return res



# Adjacency cell function
def adjacent_cells(coords):
    x_coord, y_coord = coords
    for xx, yy in adjacency:
        if 0 <= (x_coord + xx) < n_rows and 0 <= (y_coord + yy) < n_cols:
            yield [x_coord + xx, y_coord + yy]



def tot_occupied(iterable):
    """Count number of occupied seats (#) in a grid."""
    return gridsize - len(re.sub(r"#", "", "".join([x for y in iterable for x in y])))

####################################
######### --- Part 1 --- ###########
####################################

"""
Each position is either floor (.), an empty seat (L), or an occupied seat (#).
The following rules are applied to every seat simultaneously:
    - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat
    becomes occupied.
    - If a seat is occupied (#) and four or more seats adjacent to it are also occupied,
    the seat becomes empty.
    - Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.
"""


grid = [list(i) for i in data]
grid_new = deepcopy(grid)
counts = []
while True:
    if len(counts) > 1 and counts[-1] == counts[-2]:
        break
    else:
        for r1 in range(n_rows):
            for c1 in range(n_cols):
                occ_cnt = 0
                for rr, cc in adjacent_cells([r1, c1]):
                    if grid[rr][cc] == "#":
                        occ_cnt += 1
        
                if grid[r1][c1] == ".":
                    pass
                elif grid[r1][c1] == "L":
                    if occ_cnt == 0:
                        grid_new[r1][c1] = "#"
                elif grid[r1][c1] == "#":
                    if occ_cnt > 3:
                        grid_new[r1][c1] = "L"
    n_occupied = gridsize - len(re.sub(r"#", "", "".join([x for y in grid_new for x in y])))
    counts.append(n_occupied)
    grid = deepcopy(grid_new)





####################################
######### --- Part 2 --- ###########
####################################


def walk_n_count(base_coord, target = "#"):
    """Function to walk each of eight directions and stop when a seat is met.

    If the seat is occupied, increment a counter.

    Return counter results when all possible directions exhausted for a given coordinate.
    """
    counter = 0
    for coord in adjacency:
        curr_coord = deepcopy(base_coord)
        while True:
            if out_of_bounds(curr_coord, coord):
                break
            curr_coord[0] += coord[0]
            curr_coord[1] += coord[1]
            xx, yy = curr_coord

            if grid[xx][yy] == target:
                counter += 1
                break
            elif grid[xx][yy] == "L":
                break

    return counter


grid = [list(i) for i in data]
grid_new = deepcopy(grid)
counts = [0]
while True:
    if len(counts) > 1 and counts[-1] == counts[-2]:
        break
    else:

        for r1 in range(n_rows):
            for c1 in range(n_cols):
                base_coord = [r1, c1]
                occ_cnt = 0

                occ_cnt = walk_n_count(base_coord)

                if grid[r1][c1] == "L":
                    if occ_cnt == 0:
                        grid_new[r1][c1] = "#"
                if grid[r1][c1] == "#":
                    if occ_cnt > 4:
                        grid_new[r1][c1] = "L"

    n_occupied = tot_occupied(grid_new)
    counts.append(n_occupied)
    grid = deepcopy(grid_new)
    # print(grid)










