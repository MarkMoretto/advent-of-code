
"""
Purpose: Advent of Code challenge
Day: 10
Date created: 2020-12-09
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
import queue
import threading
import concurrent.futures
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
    raw_data = """16
10
15
5
1
11
7
19
6
12
4
"""
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


ddict = {}
for i in range(len(picks)):
    for j in range(i+1, len(picks)):
        print(picks[i], picks[j])
    curr, nxt = picks[i-1], picks[i]
    diff = nxt - curr
    
    ddict[i] = []
    j = i + 1
    


def combo_test(arr, arr_len):
    res = True
    for i in range(arr_len-1):
        if arr[i+1] - arr[i] >= 4:
            res = False
            break
    return res



def get_combos(N):
    tmp = []
    L = length - N
    for combo in ittr.combinations(apicks, L):
        if combo[0] == min_pick and combo[-1] == max_pick:
            if combo_test(combo, L):
                tmp.append(combo)  
    return tmp


def even_combos(n):
    tmp = []
    for i in range(0, n, 2):
        res = get_combos(i)
        tmp.extend(res)
    return tmp


def odd_combos(n):
    tmp = []
    for i in range(1, n, 2):
        res = get_combos(i)
        tmp.extend(res)
    return tmp


def proc_combos(rng):
    return [get_combos(i) for i in rng]


apicks = array("B")
apicks.fromlist(picks)

length = apicks.buffer_info()[1]
min_pick, max_pick = min(apicks), max(apicks)
start_length = length // 4


num_threads = min(50, len(apicks))

combos = []
rng = range(start_length, length)
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as tpe:
    fdict = {tpe.submit(get_combos, i):i for i in rng}
    for f in concurrent.futures.as_completed(fdict):
        idx = fdict[f]
        try:
            tmp = f.result()
            combos.append(tmp)
        except ValueError as ve:
            print(f"Error for index {idx}: {ve}")
        
            
# even_rng = range(0, h_length, 2)
# odd_rng = range(1, h_length, 2)

q = queue.Queue(maxsize=0)
num_theads = min(50, len(apicks))

t_list = []

t1 = threading.Thread(target=lambda x, y: q.put(even_combos(y)), args=(q, length))
t1.start()
t_list.append(t1)

t2 = threading.Thread(target=lambda x, y: q.put(odd_combos(y)), args=(q, length))
t2.start()
t_list.append(t2)

t3 = threading.Thread(target=lambda x, y: q.put(even_combos(y)), args=(q, length))
t3.start()
t_list.append(t3)

t2 = threading.Thread(target=lambda x, y: q.put(odd_combos(y)), args=(q, length))
t2.start()
t_list.append(t2)

for t in t_list:
    t.join()

combos = []
while not q.empty():
    combos.append(q.get())
    
combos = [x for y in combos for x in y]

# t1 = threading.Thread(target=even_combos, args=(h_length,)) 
# t2 = threading.Thread(target=odd_combos, args=(h_length,))
# t1.start()
# t2.start()
# res1 = t1.join()
# res2 = t2.join()

combos = res1 + res2


list(range(0, 6, 2)) # 0, 2, 4

list(range(1, 6, 2)) # 1, 3, 5




