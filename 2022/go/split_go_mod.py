#!/bin/python

PRIOR_FLDER = "day05"

day_num = PRIOR_FLDER.replace("day0", "") if "0" in PRIOR_FLDER else PRIOR_FLDER.replace("day", "")

new_day = int(day_num) + 1

new_folder = f"day{new_day:02}"


def incr_go_mod(aoc_mod_str: str) -> str:
    parts = aoc_mod_str.split("/")
    old_day, parts = parts[-1], parts[:-1]
    new_day = int(old_day) + 1
    parts.append(f"{new_day}")
    return r"/".join(parts)


with open(f"{PRIOR_FLDER}/go.mod") as f:
    text = f.readline()
    mod_str = text.split()[1]
    print(incr_go_mod(mod_str))


# test1="aoc/2022/go/day/5"
# parts = test1.split("/")
# old_day, parts = parts[-1], parts[:-1]
# new_day = int(old_day) + 1
