"""
Purpose: Advent of Code challenge
Day: 3
Date created: 2020-12-03
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""


from config import PROJECT_FOLDER


local_input_file = r"data\day-3-input.txt"


up = 0
down = 1
left = 0
right = 3

v_incr = (down - up)
h_incr = (right - left)


with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
    raw_data = f.read().decode("utf-8")
    

def softmax(a):
    return max(0, a)



data = raw_data.splitlines()

# Set and run
woods = [list(i) for i in data]

n_rows = len(woods)
n_cols = len(woods[0])

hits = 0 # How many trees are hit?
pos = [0, 0]
while pos[0] < n_rows:
    # print(pos[0], n_rows)
    
    v, h = pos[0], pos[1]
    
    if h > n_cols:
        woods[v:] = [w * 2 for w in woods[v:]]
        n_cols *= 2

    if woods[v][h] == "#":
        # print(f"#: {v}, {h}")
        woods[v][h] = "X"
        hits += 1
    else:
        # print(f"O: {v}, {h}")
        woods[v][h] = "O"
        
    pos[0] += v_incr
    pos[1] += h_incr



# --- Testing --- #



raw_data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()

# We only need to get to the bottom
# so adding more rows doesn't make sense.
factor: int = 1
if n_cols < n_rows:
    multiplier = (n_rows / n_cols)
    req_cols = int(n_cols * multiplier * softmax(right - left))



# def rightsize_data(iterable):
#     lr = (right - left)
#     du = (down - up)
#     # Multiply the pattern out
#     h_factor = lr if lr > 1 else 1
#     v_factor = du + 1 if du > 1 else 1
    
    
#     if lr / du < 1:
#         data_ = [line for line in iterable]       
#         data_ *= v_factor
#     else:
#         data_ = [line * h_factor for line in iterable]
#     return data_

# data = rightsize_data(sample)
# data = rightsize_data(data)


max_row = n_rows + (up - down)
max_col = n_cols + (left - right)



# Set and run
woods = [list(i) for i in data]

hits = 0 # How many trees are hit?
pos = [0, 0]
while pos[1] < max_col or pos[0] < max_row:
    
    pos[0] += (down - up)
    
    pos[1] += (right - left)    
    
    v, h = pos[0], pos[1]

    if woods[v][h] == "#":
        woods[v][h] = "X"
        hits += 1
    else:
        woods[v][h] = "O"

    # row += (down - up)
    
    

                
        

    
    
    
