"""
Purpose: Advent of Code challenge
Day: 20
Date created: 2020-12-20
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

# import itertools as ittr
import re
from collections import Counter
from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# Replace newline characters
raw_data = raw_data.replace(r"\r\n", "\n")

# raw_data = read_data(f"day-20-input.txt")



tile_pattern = r"Tile\s(\d+):\s+?"
ptitle = re.compile(tile_pattern)

class Grids:
    __slots__ = "titles", "tiles", "enum_titles", "enum_tiles", "title_tile_dict"
    def __init__(self, title_list, tile_list):
        self.titles = title_list
        self.tiles = tile_list
        self.enum_titles = self.enum_dict(title_list)
        self.enum_tiles = self.enum_dict(tile_list)
        self.title_tile_dict =  dict(zip(title_list, tile_list))

    @staticmethod
    def enum_dict(iterable):
        return {i:v for i, v in enumerate(iterable)}



# Find all title numbers.
titles = ptitle.findall(raw_data)

# Remove Title [...]: from each grid
tiles = []
for t in raw_data.split("\n" * 2):
    if ptitle.search(t):
        tmp = ptitle.sub("", t)
        tiles.append(tmp.strip().split("\n"))

tile_rows, tile_cols = len(tiles[0]), len(tiles[0][0])

G = Grids(titles, tiles)

####################################
######### --- Part 1 --- ###########
####################################

# --- Rotations --- #
flipper = lambda matrix: [i[::-1] for i in matrix]

rot0 = lambda matrix: list(map(list, matrix))
rot90 = lambda matrix: [list(i) for i in list(zip(*matrix))][::-1]
rot180 = lambda matrix: [i[::-1] for i in matrix[::-1]]
rot270 = lambda matrix: [i[::-1] for i in list(zip(*matrix))[::-1]]


rot0f = lambda matrix: flipper(rot0(matrix))
rot90f = lambda matrix: flipper(rot90(matrix))
rot180f = lambda matrix: flipper(rot180(matrix))
rot270f = lambda matrix: flipper(rot270(matrix))

# Rotation collection
rots = {
    "0": rot0,
    "90": rot90,
    "180": rot180,
    "270": rot270,
    "0f": rot0f,
    "90f": rot90f,
    "180f": rot180f,
    "270f": rot270f,
}


# --- Grid Slicers --- #
rightside = lambda matrix: list(zip(*matrix))[::-1][0]
leftside = lambda matrix: list(zip(*matrix))[0]
topside = lambda matrix: tuple(matrix[0])
bottomside = lambda matrix: tuple(matrix[-1])


# L`R -> Match on right, so grid should go on left, and vice-versa.
sidepairs = {
        "L`R": [rightside, leftside],
        "R`L": [leftside, rightside],
        "B`T": [topside, bottomside],
        "T`B": [bottomside, topside],
        }

# Count matches
matches = lambda a, b: sum([1 for i, j in zip(a, b) if i == j])

def comparesides(m1, m2, target = 10):
    """Function: comparesides(m1, m2, target=10)

    Compare all sides of two grid objects.  If match count equals target value,
    return comparison combination code ("L`R", "R`L", "B`T", "T`B")."""
    match_ = None
    for k in sidepairs:
        # Run grid through each slicerpair function.
        m1s, m2s = sidepairs[k][0](m1), sidepairs[k][1](m2)

        # Find matching elements and compare with target value.
        # Return key value if match found.
        # res = matches(m1s, m2s)
        if m1s == m2s:
            match_ = k
            break

    return match_

comparesides.__name__ = "comparesides"

# Quick test
def test_comparesides():
    t1 = rots["0"](G.tiles[0])
    t1_180_f = flipper(rot180(t1))
    t9 = rots["0"](G.tiles[-1])
    assert (comparesides(t1_180_f, t9) == "RL"), "Error: comparesides() unit test."


output = []
for title1 in G.titles:
    m1 = G.title_tile_dict[title1]
    for title2 in G.titles:
        if not title1 == title2:
            m2 = G.title_tile_dict[title2]
            for rot_m1 in rots:
                for rot_m2 in rots:
                    # # Check reverse set of results to avoid duplicates.
                    # rtmp = [title2, rot_m2, title1, rot_m1]
                    # if not rtmp in [o[0:4] for o in output]:
                    m1r, m2r = rots[rot_m1](m1), rots[rot_m2](m2)
                    sides = comparesides(m1r, m2r)
                    if not sides is None:
                        s1, s2 = sides.split("`")
                        # output.append([title1, rot_m1, title2, rot_m2, sides])

                        output.append(dict(
                                title1=title1,
                                rot1 = rot_m1,
                                side1=s1,
                                title2=title2,
                                rot2 = rot_m2,
                                side2=s2,
                                ))

adj_grid = {}
for d in output:
    t = d["title1"]
    related = d["title2"]
    if not t in adj_grid:
        adj_grid[t] = []
    if not related in adj_grid[t]:
        adj_grid[t].append(related)

#TODO: Recursive matching


# Create pairs
related_matrix = []
for title, related in adj_grid.items():
    for val in related:
        related_matrix.append([title, val])

# Set base title (center piece) and work around that?
counts = Counter([i[0] for i in related_matrix])
basetitle = [k for k, v in counts.items() if v == max(counts.values())]





# Create shell for final grid
rows_cols = int(round(len(G.titles)**(0.5),0))

fin = [[[""] * rows_cols] for i in range(rows_cols)]

for title in G.titles:
    output_ = output_by_title(title)

    for i, line1 in enumerate(output_):
        m1, rot1, m2, rot2, rel = line
        for j, line2 in enumerate(output):
            if i != j:
                m1, rot1, m2, rot2, rel = line





def output_by_title(*titles, expanded=False, strict = False, print_output=False):
    t = tuple(map(str, titles))
    # Include results for all titles in either field
    if expanded:
        tmplist = [q for q in output if q[0] in t or q[2] in t]

    # Include results where only given titles arein either field
    elif strict:
        tmplist = [q for q in output if q[0] in t and q[2] in t]
    # Include results where the given title is a match in the primary title field.
    else:
        tmplist = [q for q in output if q[0] in t]

    if print_output:
        tmplist = [f"{i}" for i in tmplist]
        print("\n".join(tmplist))
    else:
        return tmplist


output_by_title(1951)
output_by_title(2311, 1951)
output_by_title(2311, 1951, strict = True)













result  =  None
print(f"Part 1 result: {result}")




####################################
######### --- Part 2 --- ###########
####################################


print(f"Part 2: Number of messages that match rule 0: {result}")
