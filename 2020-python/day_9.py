
"""
Purpose: Advent of Code challenge
Day: 9
Date created: 2020-12-08
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
    raw_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
    """
else:
    # Current file filepath
    thisfile = current_file(__file__)
    
    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
data = list(map(int, get_lines(raw_data)))


####################################
######### --- Part 1 --- ###########
####################################

# Variable (will appear in part 2, too) that determines whether process was a success.
match_found: bool = False

# Preamble, or Window, of lagging values to consider when looking for a sum that
# equals the current value.
preamble = 25

# Collection to hold results.
res = {}

# Index variable.
# Will start at preamble value and subtract the preamble to keep the window rolling.
i = preamble

# Run function until just under the number of data values (since index starts at zero.)
while i < len(data):
    # Set current target value.
    target = data[i]

    # Set determinant to False.
    match_found = False

    # Iterate over lagging range
    # Offset to help ensure indices don't cross.
    for m in range(i - preamble, i):
        for n in range(m+1, i):
            # If sum of value equals target, update determinant.
            if data[m] + data[n] == target:
                match_found = True
                break

    # Evaluate determinant and set result accordingly.
    if match_found:
        res[target] = "valid"
    else:
        res[target] = "invalid"

    # Increment indicer.
    i += 1

# Get all invalid results and print output.
invalids = [k for k, v  in res.items() if v == "invalid"]
invalid = "\n".join(invalids)

print(f"The invalid number(s) for part 1 is/are: {invalid}")


####################################
######### --- Part 2 --- ###########
####################################

# From part 1, our expected result was singular.
# This could easily be updated to accomodate multiple invalid results.
invalid: int = 177777905


# Cut down total number of values to consider.
# Could start by a higher denominator (e.g. - 4 vs. 2), but our list of values isn't
# too large, so this works for now.
ddata: list = [i for i in data if i < (invalid//2)]


# Create static variable for data length
ddata_len: int = len(ddata)

# Similar action to part 1, except there is no window and we are just looking for
# consecutive values in the data set that add up to our invalid value.
match_found = False
while not match_found:
    for m in range(ddata_len):
        for n in range(m, ddata_len):
            tmp = ddata[m:n+1]
            # Once invalid value is found, get minimum and maximum values from range
            # and break iteration.
            if sum(tmp) == invalid:
                min_, max_ = min(tmp), max(tmp)
                match_found = True
                break

# Print to standard output if match found.
if match_found:
    result = sum([min_, max_])
    print(f"The sum of min and max values for a range that equals {invalid:,} is: {result}")

