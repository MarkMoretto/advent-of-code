
"""
Purpose: Advent of Code challenge
Day: 10
Date created: 2020-12-09
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import queue
# import threading
import concurrent.futures as ccf
from array import array
import itertools as ittr

from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Allowed gaps between outlet adapter joltage ratings.
DIFFS: tuple = (1, 2, 3)


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

apicks = array("B")
apicks.fromlist(picks)
length = apicks.buffer_info()[1]
min_pick, max_pick = min(apicks), max(apicks)


# Remove frst zero from array
apicks.pop(0)

paths_dict = {}
paths_dict[0] = 1
for adapter in apicks:
    tot_paths = 0
    for n in DIFFS:
        tot_paths += paths_dict.get(adapter - n, 0)
    paths_dict[adapter] = tot_paths


print(f"Part 2: Distinct N ways to arrange adapters: {max(paths_dict.values())}")



# ddict = {}
# for i in range(length-1):
#     a = picks[i]
#     ddict[a] = []
#     for j in range(i+1, length):
#         b = picks[j]
#         diff = b - a
#         if diff < 4:
#             ddict[a].append(apicks[j])

# least_picks = array("B")
# target = min(ddict)
# for k, v in ddict.items():
#     if k == target:
#         least_picks.append(k)
#         target = max(v)
# least_picks.append(max(apicks))




# def combo_test(arr, arr_len):
#     res = True
#     for i in range(arr_len-1):
#         if arr[i+1] - arr[i] >= 4:
#             res = False
#             break
#     return res


# def get_combos(N):
#     tmp = []
#     L = length - N
#     for combo in ittr.combinations(apicks, L):
#         if combo[0] == min_pick and combo[-1] == max_pick:
#             if combo_test(combo, L):
#                 tmp.append(combo)  
#     return tmp


# # def even_combos(n):
# #     tmp = []
# #     for i in range(0, n, 2):
# #         res = get_combos(i)
# #         tmp.extend(res)
# #     return tmp


# # def odd_combos(n):
# #     tmp = []
# #     for i in range(1, n, 2):
# #         res = get_combos(i)
# #         tmp.extend(res)
# #     return tmp


# def proc_combos(rng):
#     return [get_combos(i) for i in rng]



# start_length = least_picks.buffer_info()[1]
# # min_pick, max_pick = min(apicks), max(apicks)
# # start_length = length // 4


# num_threads = min(50, length)

# """
# # Works
# rng = [length-i for i in range(start_length, length+1)]
# tpe = ccf.ThreadPoolExecutor(max_workers=num_threads)
# wait_for = [tpe.submit(get_combos, i) for i in rng]
# combos = []
# for f in ccf.as_completed(wait_for):
#     combos.append(f.result())
# final = [x for y in combos for x in y]
# tpe.shutdown()
# """


# rng = [length-i for i in range(start_length, length+1)]

# combos = []
# with ccf.ThreadPoolExecutor(max_workers=num_threads) as tpe:
#     wait_for = [tpe.submit(get_combos, i) for i in rng]
#     for f in ccf.as_completed(wait_for):
#         combos.append(f.result())

# final = [x for y in combos for x in y]

            
