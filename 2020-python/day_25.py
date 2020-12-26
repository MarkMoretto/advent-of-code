
"""
Purpose: Advent of Code challenge
Day: 25
Date created: 2020-12-25

Contributor(s):
    Mark M.
"""


try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache

import re
from array import array
import itertools as ittr
import more_itertools as mittr
from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True



# Import data
if DEBUG:
    # raw_data = """32415"""
    raw_data = """5764801
    17807724"""

    raw_data = raw_data.strip().replace("\r", "")
else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")
    raw_data = raw_data.strip().replace("\r", "")



# raw_data = read_data(f"day-25-input.txt")
# raw_data = raw_data.strip().replace("\r", "")

# Keys (aka - subject numbers)
card_key, door_key = map(int, re.split(r"\n\s*", raw_data))
keys = card_key, door_key
keys_arr = array("Q", keys)

# def ok(*args):
#     return sum([1 if i > 0 else 0 for i in args]) == len(args)

def max_range(key_value: int, method = None):
    if not method is None:
        if method[:3] == "min":
            return int(key_value **(1/2)) + 1
    else:
        return int(key_value // 4) + 1


@cache(maxsize=None)
def next_value(v, N, divisor=20201227):
    v *= N
    v %= divisor
    return v


def value_gen(n):
    """Generate values for key evaluation."""
    value = array("L", [1])
    while True:
        value[0] = next_value(value[0], n)
        yield value[0]


vg = value_gen(7)
next(vg)

@cache(maxsize=None)
def evaluator(key_value, subject_number):
    vg = value_gen(subject_number)
    max_loops = int(key_value // 4) + 1
    result = None
    for n in range(2, max_loops):
        if key_value == vg.__next__():
            result = n
            break

    return result


args = [(card_key, subjn) for subjn in range(2, 20)]
for j in ittr.starmap(evaluator, args):
    print(j)

testkey = keys[0]


max_rng = max_range(card_key)
matches = []
for subjn in range(max_rng):
    tmp = evaluator(card_key, subjn)
    if not tmp is None:
        matches.append(dict(subject_number=subjn, loop_count=tmp))
        # print(f"Match found.  Subject Number: {subjn} Number of loops: {tmp}")


# Key 0 - Match found.  Number of loops: 1663
# evaluator.cache_clear()

door_key_matches = [{'subject_number': 786, 'loop_count': 591},
 {'subject_number': 7054, 'loop_count': 1761},
 {'subject_number': 14966, 'loop_count': 129},
 {'subject_number': 30517, 'loop_count': 1420},
 {'subject_number': 35617, 'loop_count': 1132},
 {'subject_number': 47145, 'loop_count': 1896},
 {'subject_number': 52903, 'loop_count': 1372},
 {'subject_number': 56116, 'loop_count': 1257},
 {'subject_number': 57165, 'loop_count': 1789},
 {'subject_number': 111927, 'loop_count': 1620},
 {'subject_number': 113184, 'loop_count': 1218},
 {'subject_number': 137623, 'loop_count': 136},
 {'subject_number': 142800, 'loop_count': 990},
 {'subject_number': 152200, 'loop_count': 1071},
 {'subject_number': 154245, 'loop_count': 6},
 {'subject_number': 170421, 'loop_count': 1230},
 {'subject_number': 174989, 'loop_count': 1752},
 {'subject_number': 180946, 'loop_count': 1444},
 {'subject_number': 183273, 'loop_count': 937},
 {'subject_number': 187543, 'loop_count': 1818},
 {'subject_number': 201734, 'loop_count': 355},
 {'subject_number': 203924, 'loop_count': 1296},
 {'subject_number': 216816, 'loop_count': 1096},
 {'subject_number': 217012, 'loop_count': 1584},
 {'subject_number': 229004, 'loop_count': 474},
 {'subject_number': 229902, 'loop_count': 1630},
 {'subject_number': 233652, 'loop_count': 1086},
 {'subject_number': 248657, 'loop_count': 373},
 {'subject_number': 249060, 'loop_count': 1779}]


card_key_matches = []
for el in door_key_matches:
    subjn = el["subject_number"]
    tmp = evaluator(card_key, subjn)
    if not tmp is None:
        card_key_matches.append(dict(subject_number=subjn, loop_count=tmp))



match_count = 0
subject_num_MAX = int(testkey **(0.5)) + 1

value_list = {i for i in enumerate(value_gen(subject_num_MAX), start=1)}
subject_num = 2
while subject_num < subject_num_MAX:

    vg = value_gen(subject_num)
    value = next(vg)
    n_loops = 1
    while n_loops <= (subject_num * 2):
        if value == testkey:
            break
        value = next(vg)
        n_loops += 1


    subject_num += 1




keys = card_key, door_key
max_key = max(keys)
max_rng = int(max(keys) * 1.3)

# loopdict = dict.fromkeys(keys, 0)

loopdict = {}
for subj_number in range(2, max_rng):
    n_loops = 0
    match_count = 0
    vg = value_gen(subj_number)

    while n_loops < 100:
        value = next(vg)
        n_loops += 1
        if value in keys:
            print(value, subj_number)
            if not value in loopdict:
                match_count += 1
                loopdict[value] = n_loops
    print(loopdict)
    if match_count == 2:
        break
    else:
        loopdict = {}









def loop_finder(key_values: tuple):

    # Create keys instance


    matches = {}
    subj_nums = {}

    # max_rng = int(max(key_values) ** (0.5)) + 1

    m_key = max(keys)

    # rng = int(min_key // 2) + 1
    out_rng = range(2, m_key)

    for subj_num in out_rng:

        vg = value_gen(subj_num)

        in_rng = range(subj_num, m_key)

        n_loops = 0

        for _ in in_rng:
            value = next(vg)
            n_loops += 1
            if value in key_values:
                if not value in matches:
                    # matches[val] = [n_loops, subject_number]
                    matches[value] = n_loops
                    subj_nums[value] = subj_num
                    print(f"Match found for {value} with {n_loops} loops.")
                    print(f"Subject number: {subject_number}.")
                if len(matches) == 2:
                    break

            n_loops += 1

        if len(matches) == 2 and len(set(subj_nums.values())) == 1:
            break
        else:
            matches = {}
            sub_nums = {}
    return matches




ddict = loop_finder(keys)

# Minimum loop value
# n_loops = min(ddict.values())
# n_loops = 11

# Grab key for non-minimum loop value
# subject_number = [k for k, v in ddict.items() if v != n_loops][0]


subject_number = card_key
n_loops = ddict[door_key]

idx = 0
result = -1
vg = value_gen(subject_number)
while idx < n_loops:
    result = vg.__next__()
    idx += 1

print(f"Part 1: The encryption key is: {result}")


# --Testing -- #
# divisor_ = 20201227
# subject_number = 7
# value = subject_number
# for i in range(1, 12):
#     value *= subject_number
#     value %= divisor_
#     print(value)
#     if value == door_key:
#         print("match found: ", value)

