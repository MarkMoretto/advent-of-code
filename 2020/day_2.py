"""
Purpose: Advent of Code challenge
Day: 2
Date created: 2020-12-02
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""


from config import PROJECT_FOLDER
from pathlib import Path

NUMBER_TO_FIND = 3

local_input_file = r"data\day-1-input.txt"

with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
    raw_data = f.read().decode("utf-8").splitlines()
    data = sorted(list(map(lambda x: int(x), raw_data)))

