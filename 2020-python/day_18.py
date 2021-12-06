"""
Purpose: Advent of Code challenge
Day: 18
Date created: 2020-12-17
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
from collections import namedtuple
from utils import current_file, day_number, get_lines, read_data

# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
1 + (2 * 3) + (4 * (5 + 6))"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-18-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)

if DEBUG:
    samples = [
            (data[0], 26),
            (data[1], 437),
            (data[2], 12240),
            (data[3], 13632),
            (data[4], 51),
            ]

# --- Classes and functions --- #


# https://docs.python.org/3/library/re.html#writing-a-tokenizer



def parentheses_matched(string, i = 0, count = 0):
    if i == len(string):
        return True
    if count < 0:
        return False
    if string[i] == "(":
        return parentheses_matched(string, i + 1, count + 1)
    elif string[i] == ")":
        return parentheses_matched(string, i + 1, count - 1)
    return parentheses_matched(string, i + 1, count)

# parentheses_matched(samples[0][0])

#  Shunting Yard Algorithm  #

# Weighted precedence for basic mathematical operators.
operator_precedence = {
        "*": 1,
        "/": 1,
        "+": 0,
        "-": 0,
        }

mathops = {
        "+": (lambda x, y: x + y),
        "-": (lambda x, y: x - y),
        "/": (lambda x, y: x / y),
        "*": (lambda x, y: x * y),
        }

class Token(namedtuple("Token", "kind, value")):
    __slots__ = ()

    @property
    def precedence(self):
        if self.kind == "OPERATOR":
            return operator_precedence[self.value]


def tokenizer(string):
    token_specifications = [
        ('PAREN',    r"[()]"),
        ('OPERATOR',    r"[+*/-]"),
        ('OPERAND',    r"\d+"), # Or, INTEGER
        ('IGNORE',    r"\s+"),
        ('JUNK',    r"\S+?\b"),
    ]

    tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_specifications)
    line_num = 1
    line_start = 0

    # Compile regex string
    ptok = re.compile(tok_regex)


    for m in ptok.finditer(string):
        k, v = m.lastgroup, m.group(m.lastgroup)
        if k == "JUNK":
            raise ValueError(f"Unrecognized token: {value}")
        elif k != "IGNORE":
            yield Token(k, v)


def parser(expression: str):
    operators = []
    for tok in tokenizer(expression):
        if tok.kind == "OPERAND":
            yield tok
        elif tok.kind == "OPERATOR":
            while (operators
                   and operators[-1].value != "("
                   and operators[-1].precedence <= tok.precedence):
                        yield operators.pop()
            operators.append(tok)

        elif tok.value == "(":
            operators.append(tok)
        elif tok.value == ")":

            while (operators and operators[-1].value != "("):
                yield operators.pop()
            if not operators:
                raise ValueError("Unmatched ')'")

            # Remove matching parenthesis
            operators.pop()
    for op in operators:
        if op.value == "(":
            raise ValueError("Unmatched '('")
        yield op


def eval_pol_notation(string):
    tokens = re.split(r"\s+", string)
    stack = []

    for token in tokens:
        if token in mathops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = mathops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack.pop()



####################################
######### --- Part 1 --- ###########
####################################

# --- Trying out Shunting Yard Algorithm --- #


# Work area
"""
Samples - 
[
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51)
]
"""
def balanced(s, i=0, cnt=0):
    if i == len(s): return cnt == 0
    if cnt < 0: return False
    if s[i] == "(": return  balanced(s, i + 1, cnt + 1)
    elif s[i] == ")": return  balanced(s, i + 1, cnt - 1)
    return balanced(s, i + 1, cnt)


from collections import deque

a = samples[3][0]
tmp = []
lp_cnt = a.count("(")
rp_cnt = a.count(")")
for i in range(len(a)-1):
    if a[i] == "(":
        lp_cnt -= 1



b = samples[-1][0]
b = re.sub(r"\s+", "", b)
revmap = {"(":")", ")":"("}
print("".join([revmap[b[-i]] if b[-i] in ("(",")") else b[-i] for i in range(1, len(b)+1)]))
lp_cnt = b.count("(")
rp_cnt = b.count(")")
prev = 0
if lp_cnt > 0:
    i = b.index("(", prev)
    prev = i + 1
else:
    i = 0

i = 0
tmp = []
ptmp = deque()
prior_lvl = 0
curr_lvl = 0
while i < len(b) - 1:
    if not b[i] in mathops.keys():
        if b[i] == "(":
            curr_lvl += 1
        elif b[i] == ")":
            curr_lvl -= 1
    print(prior_lvl, curr_lvl, b[i], b[i+1])
    if curr_lvl > prior_lvl:
        ptmp.appendleft(b[i+1])
    else:
        ptmp.append(b[i])
    prior_lvl = curr_lvl
    i += 1

def checkpar(x):
    while len(x.split('()'))>1:
        x=''.join(x.split('()'))
        if not x:
            return True
        return False


q = deque()
for i in range(1, len(b)+1):
    tmp = []
    string = b[0:i]
    print(string, checkpar(string))
    # print(b[0:i], balanced(b[0:i]))
    if not balanced(string):
        q.appendleft(b[i+1:i+2])
    else:
        q.append(b[i:i+1])

for i in range(len(b)-1):
    print(b[i:i+1])

### Print samples
# print("\n".join(map(lambda q: q[0], samples)))

a = " ".join([op.value for op in parser(samples[1][0])])
eval_pol_notation(a)

b = " ".join([op.value for op in parser("1 + 2 * 3 + 4 * 5 + 6")])
eval_pol_notation(b)


result = sum([eval(line) for line in data])
print(f"Part 1: Sum of input data: {result} ({result:,})")





"\((?:[^()]|(?<open> \( )|(?<-open> \)))+(?(open)(?!))\)"


re.findall(r"(\(.+\))", b)
re.findall("[+/*()-]|\d+", ssample)
re.findall(r"\((.+)\)", b) # Outer parentheses
re.findall(r"\([^()]*\)", b) # Outer parentheses
re.findall(r"\((?:[^()]|(?<open> \( )|(?<-open> \)))+(?(open)(?!))\)", b)

pmtch = re.compile(r"(?<=\().*(?=\))")
for i in pmtch.finditer(b):
    print(i.group())

ssample = re.sub(r"\s+", "", sample2)
counter = 0
for i in range(len(ssample) -1):
    curr, nxt = ssample[0:i+1], ssample[0:i+2]
    if nxt != ")":

    print(ssample[0:i+1])














