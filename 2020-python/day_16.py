
"""
Purpose: Advent of Code challenge
Day: 16
Date created: 2020-12-16
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
    raw_data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-16-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)

def return_subset(keyword):
    tmp = [data[i] for i in range(len(data)) if data[i].startswith(keyword)][0]
    if len(tmp) > 0:
        return re.split(r":\s+", tmp)[1]

def lowhigh(string):
    if "-" in string:
        L, H = string.split("-")
        return int(L), int(H)


re_nums = r"(\d+-\d+) or (\d+-\d+)"
pnums = re.compile(re_nums)
groups = ("class", "row", "seat")
all_ranges = []
for group in groups:
    rngs = pnums.search(return_subset(f"{group}")).groups()
    for rng in rngs:
        all_ranges.append(rng)


full_range = []
for rng in all_ranges:
    l, h = rng.split("-")
    rrng = list(range(int(l), int(h)+1))
    full_range.extend(rrng)
full_range = list(set(full_range))


my_ticket = [data[i+1] for i in range(len(data)) if data[i].startswith("your")][0]
other_tickets = data[data.index("nearby tickets:")+1:]
other_tickets.append(my_ticket)
all_tickets = list(map(int, re.split(r",", ",".join(other_tickets))))

errors = []
for ticket in all_tickets:
    if not ticket in full_range:
        errors.append(ticket)

result = sum(errors)
print(f"Part 1: The error rate is: {result}")


# Part 2
raw_data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

ticket_fields, my_ticket, nearby_tickets = raw_data.split("\n\n")
fielddict = {}
for line in ticket_fields.split("\n"):
    name_, values_ = re.split(r":\s+", line)
    fielddict[name_] = values_

rangedict = {}
for k,v in fielddict.items():
    rangedict[k] = []
    for rng in re.split(r"\s+or\s+", v):

        l, h = rng.split("-")
        rrng = list(range(int(l), int(h)+1))
        rangedict[k].extend(rrng)

# Drop field label
nearby_tickets = [list(map(int, i.split(","))) for i in nearby_tickets.split("\n")[1:]]
nearby_tickets_T = list(map(list, zip(*nearby_tickets)))
# rowclass = {}

# for fld, nums in rangedict.items():
#     for tix in nearby_tickets_T:
#         if set(tix).issubset(set(nums)):
#             rowclass[fld] = tix

for i, tix in enumerate(nearby_tickets_T):
    counter = 0
    for fld, nums in rangedict.items():
        tmp = sum([1 for i in tix if i in nums])
        if tmp == 3:
            print(fld, tix)
        for n in tix:
            if n in v:
                counter += 1
        if counter == 3:
            print(i, tix, k)
    
        
    

