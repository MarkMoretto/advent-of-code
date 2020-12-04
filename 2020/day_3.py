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


# Set stepsize for each direction of travel
up = 0
down = 1
left = 0
right = 1 # 3

# Calculate vertical and horizontal increments based on stepsize values.
v_incr = (down - up)
h_incr = (right - left)

# Import data
with open(PROJECT_FOLDER.joinpath(local_input_file), "rb") as f:
    raw_data = f.read().decode("utf-8")


def data_size(string):
    """Return memory allocated to iterable,
    less any garbage collector storage.
    """
    ss = string.__sizeof__()
    kb = ss / (2<<9)
    mb = ss / (2<<9) / (2<<9)
    return f"{kb:.4f} KB or {mb:.4f} MB"


def softmax(a):
    """Simple softmax function.
    
    Returns maximum value of zero and a given value.
    
    >>> softmax(-1)
    0
    >>> softmax(1)
    1
    >>> softmax(1.1)
    1.1
    >>> softmax("A")
    
    """
    if isinstance(a, (int, float)):
        return max(0, a)


def product(iterable):
    """Product of values in iterable.
        
    >>> product([])
    1
    >>> product([2])
    2
    >>> product([2,2])
    4
    """    
    if len(iterable) == 0:
        return 1
    return iterable[0] * product(iterable[1:])


data = raw_data.splitlines()

# Set and run
woods = [list(i) for i in data]

n_rows = len(woods)
n_cols = len(woods[0])


##################
# --- Part 1 --- #
##################


hits = 0 # How many trees are hit?
pos = [0, 0]
while pos[0] < n_rows:
    # Set interim vertical and horizontal variables for easier interpretation
    v, h = pos[0], pos[1]
    
    # If we run out of columns, add more!

    if h > n_cols:
        woods[v:] = [w * 2 for w in woods[v:]]
        n_cols *= 2


    # If the location has an octothorpe
    #   - update woods grid
    #   - increment hit counter
    # Otherwise
    #   - Only update woods grid
    if woods[v][h] == "#":
        woods[v][h] = "X"
        hits += 1
    else:
        woods[v][h] = "O"
        
    # Increment coordinate position by vertical and horizontal steps.
    pos[0] += v_incr
    pos[1] += h_incr



# print("\n".join(["".join(w) for w in woods]))






##################
# --- Part 2 --- #
##################

class Slope:
    def __init__(self, right = 1, down = 1):
        self.right = right
        self.down = down


paths = [
        Slope(),            # (1, 1)
        Slope(right=3,),    # (3, 1)
        Slope(right=5,),    # (5, 1)
        Slope(right=7,),    # (7, 1)
        Slope(down=2,),     # (1, 2)
        ]


data_src = raw_data.splitlines()
n_rows = len(data_src)
n_cols_src = len(data_src[0])
row_len = len(data_src[0])

all_hits = []

for p in paths:

    multiplier = int(((n_rows / n_cols_src) * p.right) + 1)

    data = [x * multiplier for x in data_src]

    n_cols = len(data[0])
    # print(n_rows, n_cols)


    hits = 0 # How many trees are hit?
    pos = [0, 0] # Starting position or coordinates

    while pos[0] < n_rows:
        # Set interim vertical and horizontal variables for easier interpretation
        r, c = pos
        try:
            if data[r][c] == "#":
                # woods[h][w] = "X"
                hits += 1
        except IndexError:
            print(f"error: row {r}, column {c}, pos {pos}")


        # Increment coordinate position by vertical and horizontal steps.
        pos[0] += p.down
        pos[1] += p.right

    all_hits.append(hits)

if len(all_hits) > 0:
    print(f"The product of {all_hits} is: {product(all_hits)}")




if __name__ == "__main__":
    # Run docstring tests
    import doctest
    doctest.testmod()
