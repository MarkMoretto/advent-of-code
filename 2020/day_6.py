
"""
Purpose: Advent of Code challenge
Day: 6
Date created: 2020-12-06
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""


from config import PROJECT_FOLDER


local_input_file = r"data\day-6-input.txt"

# Import data
with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
    raw_data = f.read()

##################
# --- Part 1 --- #
##################

responses = (
        b"".join(
                [b"`" if len(t) == 0 else t for t in raw_data.splitlines()]).split(b"`")
        )

yeses = sum(map(lambda q: len(set(q)), responses))

print(f"The number of `yes` responses is: {yeses}")


##################
# --- Part 2 --- #
##################






raw_data = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()


