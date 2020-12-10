
"""
Purpose: Advent of Code challenge
Day: 10
Date created: 2020-12-09
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
import itertools as ittr
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

ones, threes = 0, 1
picks = [0]
for i in range(d_len):
    curr, nxt = picks[-1], data[i]
    tmp = nxt - curr
    if tmp < 4:
        picks.append(nxt)
        if tmp == 1:
            ones += 1
            # print(f"ones: {curr} {nxt}")
        elif tmp == 3:
            threes += 1
            # print(f"threes: {curr} {nxt}")

picks.append(max(data) + 3)

print(f"Part 1\n\tOnes: {ones}\n\tThrees: {threes}\n\tOnes * Threes: {ones * threes}")




####################################
######### --- Part 2 --- ###########
####################################


diffs = (1, 2, 3)
p_len = len(picks)
lendict = {}
for i in range(p_len-1):
    curr = picks[i]
    lendict[curr] = []
    j = i + 1
    nxt = picks[j]
    tmp = nxt - curr
    while tmp < 4:
        lendict[curr]
        j += 1
        nxt = picks[j]
        tmp = nxt - curr


    curr, nxt = picks[i-1], picks[i]
    diff = nxt - curr
    if not diff in lendict:
        lendict[diff] = 1
    else:
        lendict[diff] += 1

for i, j in ittr.combinations(range(p_len + 1), 2):
    print(picks[i:j])

for i in ittr.combinations(picks, r=2):
    print(i)

for i in range(p_len):
    for j in range(p_len):



picks.append(max(data) + 3)






