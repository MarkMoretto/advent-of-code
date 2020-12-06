
"""
Purpose: Advent of Code challenge
Day: 6
Date created: 2020-12-06
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""


from utils import current_file, day_number, read_data

# Current file filepath
thisfile = current_file()

# AOC day number
DAY_NO: int = day_number(thisfile.stem)

# Import data
raw_data = read_data(f"day-{DAY_NO}-input.txt")


##################
# --- Part 1 --- #
##################

responses = (
        "".join(["`" if len(t) == 0 else t for t in raw_data.splitlines()]).split("`")
        )

yeses = sum(map(lambda q: len(set(q)), responses))

print(f"The number of `yes` responses is: {yeses}")


##################
# --- Part 2 --- #
##################

def counter(iterable: str):
    """Return dictionary of frequency counts for each letter in an array of letters.

    >>> counter("aaa")
    {'a': 3}
    >>> counter("abc")
    {'a': 1, 'b': 1, 'c': 1}
    >>> counter("aabbb")
    {'a': 2, 'b': 3}
    >>>
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    tmp = {}
    for i in iterable:
        if not i in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1
    return tmp


def add_nl(string):
    """Function to add newline character to end of string for processing purposes.

    >>> add_nl("aaa")
    'aaa\n'
    >>> add_nl(aaa)
    Traceback (most recent call last):
        ...
    NameError: name 'aaa' is not defined
    >>> add_nl(123)
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'endswith'
    """
    if not string.endswith("\n"):
        string += "\n"
    return string


# Part 2 data
p2_data = add_nl(raw_data)

# Delimiter used to separate groups
delim = "|"

# Split data into groups
groups = []
tmp = []
for line in p2_data.split("\n"):
    if len(line) > 0:
        tmp.append(line)
    elif len(tmp) > 0:
        groups.append(f"{delim}".join(tmp))
        tmp = []


# Variable to hold total count.
total = 0

# Iterate through each group
for group in groups:
    # If there are multiple groups, as indicated by our delimiter,
    if f"{delim}" in group:

        # Split into subgroups
        subgroups = group.split(f"{delim}")

        # Count the number of subgroups
        n_subgroups = len(subgroups)

        # Create string of all characters to find frequency count.
        all_choices = "".join(subgroups)

        # Increment total by the number of characters selected by all subgroups.
        total += sum([1 for v in counter(all_choices).values() if v == n_subgroups])

    else:
        # Otherwise, count number of unique letters in a string, which would be a
        # group count of 1.
        total += len(set(group))



if __name__ == "__main__":
    import doctest
    doctest.testmod()

