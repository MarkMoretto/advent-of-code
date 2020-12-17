
"""
Purpose: Advent of Code challenge
Day: 14
Date created: 2020-12-13
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-14-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)

enum_data = {i:v for i, v in enumerate(data)}
mask_idxs = [i for i, v in enum_data.items() if v.startswith("mask")]
mask_dict = {i:str(v).split("=")[1].strip() for i, v in enum_data.items() if v.startswith("mask")}
mem_dict = [i for i in data if not i.startswith("mask")]

for line in data:
    if line.startswith("mask"):
        mask = line.split("=")[1].strip()

mask = data[0].split("=")[1].strip()
commandz = {i:re.search(r"(\d+).+?(\d+)", v).groups() for i, v in enum_data.items() \
            if not v.startswith("mask")}

commands = {i:(int(v[0]), int(v[1])) for i, v in commandz.items()}

# def getcmd(string):



def getbits(n):
    b = bin(n).split("b")[1]
    return f"{b:0>36}"

def writemask(number, mask_val):
    b = getbits(number)
    res = []
    length = 36
    for i in range(length):
        if mask_val[i] == "X":
            res.append(b[i])
        else:
            res.append(mask_val[i])
    return "".join(res)

def memsum(mem_list):
    return sum([int(i, 2) for i in mem_list])

####################################
######### --- Part 1 --- ###########
####################################

total = 0
memory = ["0"] * 36
for idx, line in enum_data.items():
    if idx in mask_dict:
        mask = mask_dict[idx]
        total = memsum(memory)
    else:
        memcmd, numcmd= commands[idx]
        if memcmd > len(memory):
            tmp = ["0"] * (memcmd - len(memory) + 1)
            memory.extend(tmp)
        memory[memcmd] = writemask(numcmd, mask)


result = memsum(memory)

print(f"Part 1: The total memory used was:\n\t\t{result}\t({result:,})")

####################################
######### --- Part 2 --- ###########
####################################

raw_data = """mask = 1X000X0101XX101101X01X101X1000111X00
mem[10004] = 3787163
mem[18866] = 665403
mem[13466] = 175657346
mem[21836] = 99681152"""





