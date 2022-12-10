#!/bin/python
from __future__ import annotations


if __name__ == "__main__":
    
    cycle = 0
    x = 1
    amd = 0
    addmap = dict()

    with open("data-sm.in") as f:
        for line in f.readlines():
            instr, amt = line.split()
            if amt:
                amt = int(amt)
            if instr == "addx":
                addmap[cycle+2] = amt
        print(addmap)
