"""
Purpose: Advent of Code challenge
Day: 4
Date created: 2020-12-04
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from config import PROJECT_FOLDER

local_input_file = r"data\day-4-input.txt"

fields = [
    "byr", # (Birth Year)
    "iyr", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Color)
    "ecl", # (Eye Color)
    "pid", # (Passport ID)
    "cid", # (Country ID)
    ]


fieldset = set(fields)


DEBUG = True
if DEBUG:
    raw_data = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm
    
    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929
    
    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm
    
    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """.strip()
else:
    # Import data
    with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
        raw_data = f.read().decode("utf-8")

# Clear up passport strngs
lines = [line.strip() for line in raw_data.splitlines()]
pports = list(map(lambda x: str(x).strip(),
                  str(" ".join(["`" if len(line) == 0 else line for line in lines]))
                  .split("`")))


output_msg = []

##################
# --- Part 1 --- #
##################

kwrd_ptrn = r"([\w]+):.+?\s*?"
p = re.compile(kwrd_ptrn)

valid_count = 0
for pport in pports:
    ids = p.findall(pport)
    diff = fieldset.difference(set(ids))

    if len(diff) == 0:
        valid_count += 1

    elif len(diff) == 1 and "cid" in diff:
        valid_count += 1

output_msg.append(f"Valid Passport count for Part 1: {valid_count}")


##################
# --- Part 2 --- #
##################

constraints = {
    "byr": r"(19[2-9]\d|200[0-2])",
    "iyr": r"(201\d|2020)",
    "eyr": r"(202\d|2030)",
    "hgt": r"(1[5-8]\d|19[0-3])(?=cm)|(59|6\d|7[0-6])(?=in)",
    "hcl": r"(#[0-9a-f]{6})",
    "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)",
    "pid": r"^(\d{9})$",
    "cid": r"(.*?)",
    }

# a = "000000001"
# b = "0123456789"
# re.search(r"(\d{9})", a)

# kwrd_ptrn = r"([\w]+):([.]+)\s*?"
# p = re.compile(kwrd_ptrn)

# t1 = "ecl:#eef340 eyr:2023 hcl:#c0946f pid:244684338 iyr:2020 cid:57 byr:1969 hgt:152cm"
# p.findall(t1)

# t2 = "iyr:1993 hgt:74cm eyr:1960 byr:2029 hcl:293244 ecl:#3cb5e5 pid:4861232363"
# p.findall(t2)

# # Invalid sample
# sample = """
# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# """.strip()

# # Valid sample
# sample = """
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# """.strip()

# lines = [line.strip() for line in sample.splitlines()]
# pports = list(map(lambda x: str(x).strip(),
#                   str(" ".join(["`" if len(line) == 0 else line for line in lines]))
#                   .split("`")))

valid_count = 0
for pport in pports:
    
    ids, values = zip(*[re.split(r"\s?:\s?", el.strip()) for el in re.split(r"\s", pport)])
    

    diff = fieldset.difference(set(ids))

    if len(diff) < 2:
        
        regex_count=0
        ddict = dict(zip(ids, values))
        for k, v in ddict.items():
            p = re.compile(constraints[k])
            if p.search(v):
                regex_count += 1
        if regex_count == 8:
            valid_count += 1
        elif regex_count == 7 and "cid" in diff:
            valid_count += 1
        
                

results = dict(passport=[], isvalid=[], ids=[], id_count=[])
    results["passport"].append(pport)
    results["isvalid"].append(validated)
    results["ids"].append(ids)
    results["id_count"].append(len(ids))

    
zipres = list(zip(results["passport"], results["isvalid"], results["ids"], results["id_count"]))
for el in zipres:
    # if el[1] == False:
    #     print(el)
    if el[1] and el[3] < 8:
        print(el[0], el[2], el[3])


if __name__ == "__main__":
    # Run docstring tests
    import doctest
    doctest.testmod()
