
"""
Purpose: Advent of Code challenge
Day: 10
Date created: 2020-12-09
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""


from array import array

from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True



# Import data
if DEBUG:
    raw_data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""
#     raw_data = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# """
else:
    # Current file filepath
    thisfile = current_file(__file__)
    
    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")


# raw_data = read_data(f"day-10-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
data = list(map(int, get_lines(raw_data)))
data = sorted(data)

d_len = len(data)


####################################
######### --- Part 1 --- ###########
####################################

apicks = array("B")
ones, threes = 0, 1
apicks.append(0)
for i in range(d_len):
    curr, nxt = apicks[-1], data[i]
    tmp = nxt - curr
    if tmp < 4:
        apicks.append(nxt)
        if tmp == 1:
            ones += 1
        elif tmp == 3:
            threes += 1

picks.append(max(data) + 3)

print(f"Part 1\n\tOnes: {ones}\n\tThrees: {threes}\n\tOnes * Threes: {ones * threes}")




####################################
######### --- Part 2 --- ###########
####################################

# Allowed gaps between outlet adapter joltage ratings.
DIFFS: tuple = (1, 2, 3)


# Remove frst zero from array
apicks.pop(0)

# Create dictionary for holding path combos
paths_dict = {}
paths_dict[0] = 1
for adapter in apicks:
    tot_paths = 0
    for n in DIFFS:
        tot_paths += paths_dict.get(adapter - n, 0)
    paths_dict[adapter] = tot_paths


print(f"Part 2: Distinct N ways to arrange adapters: {max(paths_dict.values())}")

