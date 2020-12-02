
"""
Purpose: Advent of Code challenge
Day: 1
Date created: 2020-12-02
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

from config import PROJECT_FOLDER
from pathlib import Path

# PROJECT_FOLDER = Path(r"C:\Users\Work1\Desktop\Info\GitHub\advent-of-code\2020")

local_input_file = r"data\day-1-input.txt"

with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
    raw_data = f.read().decode("utf-8").splitlines()
    data = sorted(list(map(lambda x: int(x), raw_data)))

half = len(data) // 2
h1, h2 = data[:100], data[100:]

h1_values = []
for i in range(half):
    for j in range(i+1, half):
        if h1[i] + h1[j] == 2020:
            h1_values.append(h1[i])
            h1_values.append(h1[j])

if len(h1_values) == 2:
    print(h1_values[0] * h1_values[1])

else:
    h2_values = []
    for i in range(half):
        for j in range(i+1, half):
            if h2[i] + h2[j] == 2020:
                h2_values.append(h1[i])
                h2_values.append(h1[j])

    if len(h2_values) == 2:
        print(h2_values[0] * h2_values[1])
