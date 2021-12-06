"""
Purpose: Advent of Code challenge
Day: 19
Date created: 2020-12-19
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache
import itertools as ittr

from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """0: 4 1 5
        1: 2 3 | 3 2
        2: 4 4 | 5 5
        3: 4 5 | 5 4
        4: "a"
        5: "b"
        
        ababbb
        bababa
        abbbab
        aaabbb
        aaaabbb"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-19-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
# raw_data = re.sub(r'"', "", raw_data)
# try:
#     data = list(map(int, get_lines(raw_data)))
# except ValueError:
#     pass
# finally:
#     data = get_lines(raw_data)

# Get messages to test
# raw_data = re.sub(r"\n\s+", "\n", raw_data)
# messages = [i for i in data if i.startswith(("a","b",))]
# data = [i for i in data if not i in messages]
# data1 = "\n".join(data)
# data, messages = re.split(r"\n(?:[ab])", raw_data, maxsplit=1)
# ddict = dict(re.split(r":\s+", line) for line in data.splitlines())


# p = re.compile(r":\s+") # Previous regex
# sequence = re.split(r"\s+", p.split(data[0])[1])
# ddict = {p.split(line)[0]:p.split(line)[1] for line in data}

# def create_data_dict(iterable):
#     p = re.compile(r"(\d+):\s+(.+)")

#     out = {}
#     for line in iterable:
#         res = p.search(line)
#         if res:
#             k, v = res.groups()
#             if "|" in v:
#                 out[k] = []
#                 for el in re.split(r"\s+[|]\s+", v):
#                     out[k].append(re.split(r"\s+", el))
#             elif v.isalpha():
#                 out[k] = v
#             else:
#                 out[k] = re.split(r"\s+", v)

#     # Sort values; Convert keys into integers for proper sorting (ascending or descending)
#     return dict(sorted(out.items(), key=lambda q: int(q[0]), reverse=False))

# ddict = create_data_dict(data)
# letterdict = {int(k):v for k, v in ddict.items() if v in ("a", "b",)}


# Test method
raw_data = raw_data.replace("\r\n", "\n")
raw_data = re.sub(r'"', "", raw_data)
data, msgs = re.split(r"\n\n", raw_data, maxsplit=1)
ddict = dict(re.split(r":\s+", line) for line in data.split("\n"))

messages = msgs.split("\n")

####################################
######### --- Part 1 --- ###########
####################################


@cache(maxsize=None)
def isvalid(el):
    # if '"' in el:
    if el.isalpha():
        return set(el)
    if "|" in el:
        return set.union(*map(isvalid, re.split(r"\s+[|]\s+", el)))
    if " " in el:
        tmp = el.strip().split(" ")
        if len(tmp) == 2:
            l, r = tmp
            return set(x + y for x, y in ittr.product(isvalid(l), isvalid(r)))
        elif len(tmp) == 3:
            l, m, r = tmp
            return set(x + y + z for x, y, z in ittr.product(isvalid(l), isvalid(m), isvalid(r)))
    return isvalid(ddict[el])

# How many messages completely match rule 0?

result  = sum([1 if line in isvalid(ddict["0"]) else 0 for line in messages])
print(f"Part 1: Number of messages that match rule 0: {result}")




####################################
######### --- Part 2 --- ###########
####################################

# import sys
# # print(sys.getrecursionlimit())
# sys.setrecursionlimit(sys.getrecursionlimit() * 4)

to_update = {"8": "42 | 42 8", "11": "42 31 | 42 11 31"}
for k, v in to_update.items():
    ddict[k] = v

isvalid.cache_clear()


result = 0
for msg in messages:
    tmp = "".join(str(int(msg[i:i+8] in isvalid(ddict["42"]))) for i in range(0, len(msg), 8))
    if (tmp.count("1") > tmp.count("0")) and "10" in tmp and not "01" in tmp:
        result += 1

print(f"Part 2: Number of messages that match rule 0: {result}")
