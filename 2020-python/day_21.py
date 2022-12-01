
"""
Purpose: Advent of Code challenge
Day: 21
Date created: 2020-12-21
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re

from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-13-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)

def counter(iterable):
    tmp = {}
    for k in iterable:
        if not k in tmp:
            tmp[k] = 1
        else:
            tmp[k] += 1
    return tmp

# ddict = dict(line=[], words=[], ingredients=[])
ddict = {}
for idx, line in enumerate(data):
    w, i = line.split(" (contains ")
    i = i[:-1].split(", ")
    w = w.strip().split(" ")
    # print(words, ingredients)
    # ddict[idx] = {}
    # ddict[idx]["words"] = counter(w)
    # ddict[idx]["ingredients"] = counter(i)
    ddict[idx] = dict(words=[], ingredients=[])
    ddict[idx]["words"].extend(w)
    ddict[idx]["ingredients"].extend(i)


for i in range(len(ddict)):
    for j in range(len(ddict)):
        for w in ddict[i]["words"]:









# # Print json-like structure.
# def print_json():
#     import json
#     print(json.dumps(ddict, indent=4))

# def all_values(cat = "words"):
#     d_ = []
#     for k in ddict:
#         tmp = [i for i in ddict[k][cat]]
#         d_.extend(tmp)
#     return d_

# worddict = counter(all_values("words"))
# ingreddict = counter(all_values("ingredients"))











