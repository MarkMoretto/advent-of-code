#!/bin/python

from collections import deque
from os import remove
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE_A = DATA_DIR.joinpath("day04.txt")
data = DATA_FILE_A.open(mode="r", encoding="utf-8").read()


def stoi(string: str, delimiter = None) -> tuple:
    """Return list of integers. Optional delimiter argument included
    to specify what to split the string upon.
    """
    if not delimiter is None:
        return tuple(map(int, string.split(delimiter)))
    return tuple(map(int, string.split()))

def flatten(iterable: list) -> list:
    """Unpack a two-dimensional grid into a single list of values.
    """
    return [x for y in iterable for x in y]


# https://adventofcode.com/2021/day/4
# test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7""".strip()

def get_numbers(string: str) -> list:
    return stoi(string, ",")

def get_boards(string: str) -> dict:
    s = string.strip()
    return {i:[stoi(line) for line in v.split("\n")] for i, v in enumerate(s.split("\n\n"))}

def process_input(string: str) -> tuple:
    _num_str, _string = string.split("\n", 1)
    _numbers = get_numbers(_num_str)
    _boardmap = get_boards(_string)
    return _numbers, _boardmap

# Process and set initial variables.
numbers, boardmap = process_input(data)



# Check board
def check_board(current_board, nums, board_size: int = 5) -> int:
    """Return 1 if current set of numbers matches at least one complete board dimension.
    Board dimensions include rows or columns, but not diagonals.
    If no match found, return 0.
    """
    n_matched = 0

    # Check rows
    for row in current_board:
        if sum([el in row for el in nums]) == board_size:
            n_matched += 1
            break
    
    # Check columns
    for col in list(zip(*current_board)):
        if sum([el in col for el in nums]) == board_size:
            n_matched += 1
            break

    return n_matched

def eval_boards(max_count = 1):
    number_q = deque()
    match_map = dict(count=0, board_index=-1)
    for n in numbers:
        print(number_q)
        print(match_map)
        
        if match_map.get("count", 0) == max_count:
            break
        number_q.append(n)
        for idx in boardmap:
            match_map["count"] = check_board(boardmap[idx], number_q)

            if match_map.get("count", 0) == max_count:
                match_map["board_index"] = idx
                break
    return boardmap.get(match_map["board_index"]), number_q

# --- Part 1 --- #
winning_board, numbers_called = eval_boards()
uncalled_sum = sum([n for n in flatten(winning_board) if not n in numbers_called])
result = uncalled_sum * numbers_called[-1]
print("Part 1 solution: ", result)


# -- Part 2 --- #

def eval_boards_2():
    number_q = deque()
    
    # Queue for all boards
    # Will remove each board as they are solved.
    # Each subsequent number called may eliminate more than
    # one board.
    unsolved_q = deque(boardmap.keys())

    for n in numbers:

        # Add next number to called queue.
        number_q.append(n)

        unsolved_len = len(unsolved_q)

        # Break if only one board remaining
        if unsolved_len == 1:
            break

        # Check boards against numbers.
        # Will only iterate unsolved boards.
        for idx in boardmap:
            if idx in unsolved_q:
                result = check_board(boardmap[idx], number_q)

                # If match found, remove from unsolved queue.
                if result >= 1:
                    unsolved_q.remove(idx)
    
    # Return solved boad and queue of numbers called.
    return boardmap.get(unsolved_q[-1]), number_q

winning_board, numbers_called = eval_boards_2()
len(numbers_called)
uncalled_sum = sum([n for n in flatten(winning_board) if not n in numbers_called])
result = uncalled_sum * numbers_called[-1]
print("Part 2 solution: ", result)









# def test_misc():
#     t_boardmap = {k:list(zip(*v)) for k, v in boardmap.items()}
#     bboard = boardmap.get(0)
#     t_bboard = list(zip(*bboard))
#     board_size = len(bboard)
#     t_board_size = board_size - 1 # Diagonal transversal limit.

#     # Check rows
#     test_row = (6, 10, 3, 18, 5)
#     for row in bboard:
#         if sum([el in row for el in test_row]) == board_size:
#             print(row)

#     # Check columns
#     test_col = (17, 23, 14, 3, 20)
#     for col in t_bboard:
#         if sum([el in col for el in test_col]) == board_size:
#             print(col)

#     # Check diag top left-to-bottom right
#     test_diag_t_lr = (22, 2, 14, 18, 19)
#     sum([bboard[i][i] in test_diag_t_lr for i in range(board_size)])
#     # [bboard[i][i] for i in range(board_size)] # Diag l-to-r

#     # Check diag bottom left-to-top right
#     test_diag_b_lr = (1, 10, 14, 4, 0)
#     sum([bboard[i][t_board_size-i] in test_diag_b_lr for i in range(t_board_size, -1, -1)])
#     # [bboard[i][t_board_size-i] for i in range(t_board_size, -1, -1)]

# Check board (includes diagonals)
# def check_board(current_board, nums, board_size: int = 5) -> int:
#     """Return 1 if current set of numbers matches at least one complete board dimension.
#     Board dimensions include rows, columns, or diagonals.
#     If no match found, return 0.
#     """
#     n_matched = 0

#     # Check rows
#     for row in current_board:
#         if sum([el in row for el in nums]) == board_size:
#             print("Row match: ", current_board)
#             n_matched += 1
#             break
    
#     # Check columns
#     for col in list(zip(*current_board)):
#         if sum([el in col for el in nums]) == board_size:
#             print("Column match: ", list(zip(*current_board)))
#             n_matched += 1
#             break

#     # Check top-to-bottom, left-to-right diagonal
#     if sum([current_board[i][i] in nums for i in range(board_size)]) == board_size:
#         print("t-to-b, l-to-r match: ", current_board)
#         n_matched += 1

#     # Check bottom-to-top, left-to-right diagonal
#     if sum([current_board[::-1][i][i] in nums for i in range(board_size)])== board_size:
#         print("b-to-t, l-to-r match: ", current_board[::-1])
#         n_matched += 1

#     return n_matched