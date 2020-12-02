"""
Purpose: Advent of Code challenge
Day: 2
Date created: 2020-12-02
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from config import PROJECT_FOLDER


local_input_file = r"data\day-2-input.txt"

with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
    data = f.read().decode("utf-8").splitlines()



def eval_pw_count(pw, letter, low_high_ct):
    """Evaluate count of letter in string vs. expected count range."""
    return pw.count(letter) >= low_high_ct[0] and pw.count(letter) <= low_high_ct[1]


def eval_pw_indices(pw, letter, low_high_ct):
    """Evaluate position of letter.

    If letter at one of two indices, return True, else False.
    """
    index_count = 0
    if letter in pw:
        for i in low_high_ct:
            if pw[i-1] == letter:
                index_count += 1
    return index_count == 1


# Regular expression pattern to capture values from each entry.
pattern = r"""
    ([\d]+)     # capture low-end of range
    -
    ([\d]+)     # capture high-end of range
    \s+
    ([\w]+)     # capture letter to evaluate
    :\s+
    ([\w]+)     # capture password
    """
p = re.compile(pattern, flags = re.X)

# Variable to hold output message chunks.
msgs = []



# Part 1: Evaluate letter count in each password.
valid_pw_1 = 0
for entry in data:
    m = p.search(entry)
    if m:
        rng = list(map(int, m.groups()[:2]))
        letter = m.groups()[2]
        pw = m.groups()[3]

        if eval_pw_count(pw, letter, rng):
            valid_pw_1 += 1

# Append results of part 1 to message list.
msgs.append(f"The valid password count for part 1 is: {valid_pw_1}")



# Part 2:
#   Evaluate letter at one of two indices.
#   Cannot be at both indices.
#   Indices start at 1, not zero.

valid_pw_2 = 0
for entry in data:
    m = p.search(entry)
    if m:
        rng = list(map(int, m.groups()[:2]))
        letter = m.groups()[2]
        pw = m.groups()[3]

        if eval_pw_indices(pw, letter, rng):
            valid_pw_2 += 1

# Append results of part 2 to message list.
msgs.append(f"The valid password count for part 2 is: {valid_pw_2}")

# Print results.
print("\n".join(msgs))


