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

# Simple regular expression to split IDs and values within a passport entry.
kwrd_ptrn = r"([\w]+):.+?\s*?"
p = re.compile(kwrd_ptrn)

# Cumulative validation count
valid_count_1 = 0
for pport in pports:
    ids = p.findall(pport)
    diff = fieldset.difference(set(ids))

    if len(diff) == 0:
        valid_count_1 += 1

    elif len(diff) == 1 and "cid" in diff:
        valid_count_1 += 1

output_msg.append(f"Valid Passport count for Part 1: {valid_count_1}")


##################
# --- Part 2 --- #
##################

# Constraint collection
# Keys are ID values
# Values are regular expressions for validation.
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


# Cumulative validation count
valid_count_2 = 0

for pport in pports:
    # Split passports by whitespace, then by colon
    # Unpack to id and value variables.
    ids, values = zip(*[re.split(r"\s?:\s?", el.strip()) for el in re.split(r"\s", pport)])
    
    # Find set difference between expected and actual.
    # Capture missing elements in variable.
    diff = fieldset.difference(set(ids))

    # Difference count between actual and expected should be less than 2.
    # Difference can be one as long as the value is 'cid'
    if len(diff) < 2:
        
        # Validate constraints using regular expressions.
        # Count number of valid values in each passport
        regex_count=0
        
        # Create a key-value collection for analysis
        ddict = dict(zip(ids, values))
        
        # Iterate dictionary
        # Compile regex value
        # Use .search() to determine if value is valid
        for k, v in ddict.items():
            p = re.compile(constraints[k])
            if p.search(v):
                regex_count += 1
                
        # If regex_count is 8, then passport valid
        # If regex_count is 7 and 'cid' in id list, then passport valid
        if regex_count == 8:
            valid_count_2 += 1
            
        elif regex_count == 7 and "cid" in diff:
            valid_count_2 += 1

output_msg.append(f"Valid Passport count for Part 2: {valid_count_2}")


if __name__ == "__main__":
    # # Run docstring tests
    # import doctest
    # doctest.testmod()
    print("Results for day 4:\n" + "\n".join(output_msg))
