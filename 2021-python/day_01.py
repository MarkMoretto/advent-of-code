#!/usr/bin/env python


'''
URL: https://adventofcode.com/2021/day/1
'''

from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day1a.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read().splitlines()

depth_data = """199
200
208
210
200
207
240
269
260
263""".strip().splitlines()

# depths = stoi(depth_data)

stoi = lambda string_list: list(map(int, string_list))

def quantify(iterable, pred=bool):
    return sum(map(pred, iterable))


def agg_sum(fterator):
    return sum(fterator)

def f(predicate: bool, *args):
    return map(predicate, *args)


depths = stoi(data)


### --- Part 1 --- ###
def solution_a(depth_list: list):
    return agg_sum(
        f(lambda a, b: 1 if b-a>0 else 0, depth_list[:-1], depth_list[1:])
    )

part_a_result = solution_a(depths)
print(part_a_result)



### --- Part 2 --- ###
WINDOW_SIZE = 3


def solution_b(depth_list: list, stepsize: int = WINDOW_SIZE) -> int:
    max_range = len(depth_list) - stepsize + 1
    increased_count = 0
    prev_measure = 0
    for i in range(max_range):
        if i == 0:
            prev_measure = sum(depth_list[i:i+stepsize])
        else:
            current_measure = sum(depth_list[i:i+stepsize])
            if (current_measure - prev_measure) > 0:
                increased_count += 1
            prev_measure = current_measure
    return increased_count

part_b_result = solution_b(depths)
print(part_b_result)