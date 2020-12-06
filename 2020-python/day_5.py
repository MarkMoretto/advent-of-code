"""
Purpose: Advent of Code challenge
Day: 5
Date created: 2020-12-05
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

from array import array
from utils import current_file, day_number, read_data

# Current file filepath
thisfile = current_file(__file__)

# AOC day number
DAY_NO: int = day_number(thisfile.stem)

# Import data and split by newline character.
raw_data = read_data(f"day-{DAY_NO}-input.txt", return_bytes = True)
data = raw_data.splitlines()



def halfway(iterable):
    """Function that calculates half of a set of numbers."""
    return round((iterable[0] - iterable[1]) / 2., 0)

def get_seat_id(r, c):
    """Function to calculate seat ID based on row and column data."""
    return int((r * 8) + c)



# loc = b"FBFBBFFRLR"

# Row and column arrays
arow = array("B")
acol = array("B")


def get_row_col(location_code):
    rows = [127., 0.]
    cols = [7., 0.]

    arow.frombytes(location_code[:7])
    acol.frombytes(location_code[7:])

    while arow:
        row_var = chr(arow.pop(0))

        row_idx = halfway(rows)
        col_idx = halfway(cols)

        if row_var == "F":
            rows[0] -= row_idx
        else:
            rows[1] += row_idx


    while acol:
        col_var = chr(acol.pop(0))

        row_idx = halfway(rows)
        col_idx = halfway(cols)
        if col_var == "L":
            cols[0] -= col_idx
        else:
            cols[1] += col_idx

    if row_var == "F":
        row = min(rows)
    else:
        row = max(rows)

    if col_var == "L":
        col = min(cols)
    else:
        col = max(cols)

    return row, col


##################
# --- Part 1 --- #
##################

max_id = -1.
for location in data:
    seat_id = get_seat_id(*get_row_col(location))
    if seat_id > max_id: max_id = seat_id

print(f"The maximum seat ID is: {seat_id}")


##################
# --- Part 2 --- #
##################

all_data = dict(row=[], col=[], seat_id=[])
for location in data:
    r_, c_ = get_row_col(location)
    all_data["row"].append(r_)
    all_data["col"].append(c_)
    all_data["seat_id"].append(get_seat_id(r_, c_))


all_possible_seats = set(range(min(all_data["seat_id"]), max(all_data["seat_id"])+1))

remaining_seats = all_possible_seats.difference(set(all_data["seat_id"]))

if len(remaining_seats) == 1:
    my_seat = list(remaining_seats)[0]
    print(f"My seat ID is: {my_seat}")
