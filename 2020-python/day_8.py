# -*- coding: utf-8 -*-
"""
Purpose: Advent of Code challenge
Day: 8
Date created: 2020-12-06
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from os import linesep
from utils import current_file, day_number, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = False


# regex pattern for extracting parts of data line.
INSTR_PATTERN: str = r"(\w+)\s+(\+|-)(\d+)"


# Import data
if DEBUG:
    raw_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
else:
    # Current file filepath
    thisfile = current_file(__file__)
    
    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")
    
    raw_data = str(raw_data).replace(linesep, "\n")
    
data = [s.strip() for s in raw_data.split("\n") if len(s.strip()) > 0]

def cls_property(name, data_type):
    """Helper function to define class properties."""

    masked_name = "__" + name

    @property
    def prop(self):
        return getattr(self, masked_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, data_type):
            raise TypeError(f"Expected data type for {name} is {data_type}.")
        setattr(self, masked_name, value)

    return prop


class Cmd:
    
    cls_property("instruction", str)
    cls_property("sign", str)
    cls_property("value", str)
    
    def __init__(self, instruction, sign, value):
        self.instruction = instruction
        self.sign = sign
        self.value = int(value)
        

class Core:
    
    INSTR_PATTERN: str = r"(\w+)\s+(\+|-)(\d+)"
    
    cls_property("data", str)
    
    def __init__(self, data):
        self.data = data
        
    def generate_instructions(self):
        self.__p = re.compile(self.INSTR_PATTERN)
        self.cmds: list = []
        for line in self.data:
            res = self.__p.search(line)
            if res:
                cmd = Cmd(*res.groups())
                self.cmds.append(cmd)
                
    @property
    def length(self):
        return len(self.cmds)


    def print_cmds(self):
        self.__msgs = [f"{c.instruction} | {c.sign} | {c.value}" for c in self.cmds]
        print("\n".join(self.__msgs))        


core = Core(data)
core.generate_instructions()

if DEBUG:
    assert (core.length == 9), "Unit test: Instruction count error."
    assert (core.cmds[0].instruction == "nop"), "Unit test: Instruction command error."
    assert (core.cmds[0].sign == "+"), "Unit test: Instruction sign error."
    assert (core.cmds[0].value == 0), "Unit test: Instruction value error."
    

####################################
######### --- Part 1 --- ###########
####################################

visited = []
accumulator = 0
i = 0
while True:
    if i in visited:
        break
    
    visited.append(i)
    
    current = core.cmds[i].instruction
    
    if current == "nop":
        i += 1

    elif current == "acc":
        if core.cmds[i].sign == "+":
            accumulator += core.cmds[i].value
        else:
            accumulator -= core.cmds[i].value
        i += 1

    else:
        # If "jmp", update index according to sign
        if core.cmds[i].sign == "+":
            i += core.cmds[i].value
        else:
            i -= core.cmds[i].value

print(f"The accumulator value for part 1 is: {accumulator}")


    
####################################
######### --- Part 2 --- ###########
####################################


# Get indices for all jmp and all nop instructions.
all_jmps = [i for i in range(core.length) if core.cmds[i].instruction == "jmp"]
all_nops = [i for i in range(core.length) if core.cmds[i].instruction == "nop"]

# Join jmp and nop lists
jmps_nops = sorted(all_jmps + all_nops, reverse=True)

# Set variables to hold visited indices and the accumulated total, along with
# and index variable.
visited = []
accumulator = 0
i = 0

while True:
    # If index variable in visited indices list, adjust params and re-run.
    if i in visited:
        if DEBUG:
            print("resetting variables")
            
        visited = []
        accumulator = 0
        i = 0
        to_revert = to_change
        try:
            to_change = jmps_nops.pop()
            if DEBUG:
                print(f"to_change: {to_change}")
                
            # Change `jmp` to `nop,` or vice-versa, before re-running.
            if to_change in all_jmps:
                core.cmds[to_change].instruction = "nop"
            elif to_change in all_nops:
                core.cmds[to_change].instruction = "jmp"

            # Revert `jmp` to `nop,` or vice-versa, from prior run.
            if to_revert in all_jmps:
                core.cmds[to_revert].instruction = "jmp"
            elif to_revert in all_nops:
                core.cmds[to_revert].instruction = "nop"   
                
            if DEBUG:
                print(core.print_cmds())
            
        except IndexError:            
            break
            
    try:
        visited.append(i)
        
        current = core.cmds[i].instruction
        
        if current == "nop":
            i += 1
    
        elif current == "acc":
            if core.cmds[i].sign == "+":
                accumulator += core.cmds[i].value
            else:
                accumulator -= core.cmds[i].value
            i += 1
    
        else:
            # If "jmp", update index according to sign
            if core.cmds[i].sign == "+":
                i += core.cmds[i].value
            else:
                i -= core.cmds[i].value

    except IndexError:
        break



print(f"The accumulator value for part 2 is: {accumulator}")



