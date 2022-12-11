#!/bin/python
from __future__ import annotations
from typing import List

IntList = List[int]

instr: str = ""
amt: int = 0

addlist: IntList = [0, 1]

signal_list: IntList = list()
sig_strength: int = 0

x: int = 1

PIXEL_WIDTH: int = 3


# def draw_row(x: int):
#     pixel = 0
#     x_val = x-pixel

#     if x_val < 0:
#         ...

if __name__ == "__main__":

    with open("data.in") as f:
        for line in f.readlines():
            splits = line.split()

            instr = splits[0]
            if instr[0] == "n":
                addlist.append(x)
                continue
            
            amt = int(splits[1])
            x = addlist[-1]
            addlist.append(x)
            x += amt
            addlist.append(x)

    # Part 1
    def part1():
        tot_signal_strength: int = 0
        for p in range(len(addlist)):
            if p >= 20 and (p-20)%40==0:
                signal_list.append(p * addlist[p])
                tot_signal_strength += signal_list[-1]

        print(tot_signal_strength)

    # Part 2
    w, h = 40, 6
    crt = [["." for _ in range(w)] for _ in range(h)]

    for cycle, v in enumerate(addlist[1:]):
        c_d, c_m = divmod(cycle, 40)
        x = cycle%40
        if abs(v-c_m) < 2:
            crt[c_d][c_m] = "#"

    for r in crt:
        print("".join(r))
    # draw_table = dict()
    # for i, v in enumerate(addlist[1:]):
    #     x = i%40
    #     if abs(v-x) < 2:
    #         draw_table[x] = i//40

    # draw_table = dict(sorted(draw_table.items(), key=lambda x: x[0]))
    # for k, v in draw_table.items():
    #     print(f"{k}: {v:^3}")
