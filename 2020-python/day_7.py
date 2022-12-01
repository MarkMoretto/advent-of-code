
"""
Purpose: Advent of Code challenge
Day: 7
Date created: 2020-12-07
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from utils import current_file, day_number, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = False

# The bag color for evaluation.
TARGET_BAG: str = "shiny gold"


# Import data
if DEBUG:
    raw_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """
else:
    # Current file filepath
    thisfile = current_file(__file__)
    
    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
data = [i.strip() for i in raw_data.split("\n") if len(i.strip()) > 0]


def bag_qty_re(string):
    """Function to find bag and quantity data within string.

    Returns:
        bag: str - The color of a bag.
        quantity: int - The quantity of bags required.
    """
    s = re.findall(r"([\d]+)\s([\w\s]+)", string)

    quantity = s[0][0]
    bag = s[0][1]

    # return bag, int(quantity)
    return bag, int(quantity)



####################################
######### --- Part 1 --- ###########
####################################

bags = {}
for line in data:
    bag, requirements = line.split("contain")

    # Clean up bag name.
    bag = re.sub(r"(\s*bags?\s*)", "", bag)


    # Skip item if 'no other' in requirements.
    if not "no other" in requirements:
        # Set bag name as key
        bags[bag] = []

        # Split by delimiter
        reqs = re.split(r",\s*", requirements)
    
        # Iterate new list of split values
        for r in reqs:
    
            # Clean up string by removing unnecessary words and non-word characters
            r = re.sub(r"\s*bags?.?", "", r.strip())

            # Use function to extract bag name and quantity
            bag_name, qty = bag_qty_re(r)

            # Set key and value of subdictionary to bag_name and quantity.
            bags[bag].append(bag_name)




# Overly complicated method of identifying required bags for
# a given target color.
# Relies heavily on set() functions and could be improved if required
# on future AoC challenges.
targets = set()
for k in bags:
    if TARGET_BAG in bags[k]:
        targets.add(k)
    if len(targets) > 0:
        for i in bags:
            tmp = targets.intersection(set(bags[i]))
            if len(tmp) > 0:
                targets.add(i)

total = len(targets)
print(f"The number of bags that eventually can hold {TARGET_BAG} is: {total}")




####################################
######### --- Part 2 --- ###########
####################################


bags = {}
for line in data:
    bag, requirements = line.split("contain")

    # Clean up bag name.
    bag = re.sub(r"(\s*bags?\s*)", "", bag)

    # Set bag name as key
    bags[bag] = {}

    # Split by delimiter
    reqs = re.split(r",\s*", requirements)

    # Iterate new list of split values
    for r in reqs:

        # Clean up string by removing unnecessary words and non-word characters
        r = re.sub(r"\s*bags?.?", "", r.strip())

        if r == "no other":
            bags[bag][r] = 0
        else:
            # Use function to extract bag name and quantity
            bag_name, qty = bag_qty_re(r)
    
            # Set key and value of subdictionary to bag_name and quantity.
            bags[bag][bag_name] = qty




target = "shiny gold"


def bag_eval(target=None):
    """Recursive function to walk bags, match colors, and increment total
    bags required for a given color.
    """
    tot = 1
    if target == "no other":
        return tot
    else:
        tmp = bags[target]
        if not tmp:
            return tot

        for color, num in tmp.items():
            tot += num * bag_eval(color)

        return tot



result = bag_eval(TARGET_BAG) - 1
print(f"The number of bags required if taking a {target} bag is: {result}")



