
"""
Purpose: Advent of Code challenge
Day: 17
Date created: 2020-12-17
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import itertools as ittr
from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """.#.
..#
###"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-17-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)


grid = [list(i) for i in data]


# -- objects and functions --- #

def create_cubes(matrix):
    cube_set = set()
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "#":
                cube_set.add((c, r, 0, 0))
    return cube_set

####################################
######### --- Part 1 --- ###########
####################################

"""
If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube
remains active. Otherwise, the cube becomes inactive.

If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
Otherwise, the cube remains inactive.
"""

# gen_positions = ittr.product(range(-1, 2), repeat=3)
# positions =  tuple((pos[0], pos[1], pos[2], 0) for pos in gen_positions if pos != (0, 0, 0))
# n_pos = len(positions)


# tf_data = [[False] * len(data) for x in range(len(data))]
# for r in range(len(data)):
#     for c in range(len(data[r])):
#         if data[r][c] == "#":
#             tf_data[r][c] = True


# directions = []
# neighbor_rng = range(-1, 2)
# for x in neighbor_rng:
#     for y in neighbor_rng:
#         for z in neighbor_rng:
#             directions.append(Cube(x, y, z))
#             print(x, y, z)




def main(matrix, N=3):

    gen_positions = ittr.product(range(-1, 2), repeat=N)
    if N == 3:
        positions =  tuple((pos[0], pos[1], pos[2], 0) for pos in gen_positions if pos != (0, 0, 0))
    elif N == 4:
        positions =  tuple(pos for pos in gen_positions if pos != (0, 0, 0, 0))

    cubes = create_cubes(matrix)

    for _ in range(6):

        next_cubes = set()
        neighbors = set()
    
        for cube in cubes:
            counter = 0
            for p in positions:
                pos = tuple((cube[i] + p[i] for i in range(4)))
                if pos in cubes:
                    counter += 1
                else:
                    neighbors.add(pos)
            if counter >= 2 and counter <= 3:
                next_cubes.add(cube)
    
        for cube in neighbors:
            counter = 0
            for p in positions:
                pos = tuple(cube[i] + p[i] for i in range(4))
                if pos in cubes:
                    counter += 1
            if counter == 3:
                next_cubes.add(cube)
    
        cubes = next_cubes

    return len(cubes)

result = main(grid, 3)
print(f"Part 1 - Number of remaining cubes: {result}")



####################################
######### --- Part 2 --- ###########
####################################

# Switch the main function up to handle 4 dimensions, now.
result = main(grid, 4)
print(f"Part 1 - Number of remaining cubes: {result}")
