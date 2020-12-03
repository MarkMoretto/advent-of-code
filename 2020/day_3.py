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


print("\n".join(["".join(w) for w in woods]))






##################
# --- Part 2 --- #
##################


class Course:
    def __init__(self):
        self.course: list = []
        self.__n_rows: int
        self.__n_cols: int


    def generate(self, raw_data: str):
        if isinstance(raw_data, str):
            dd = raw_data.splitlines()

            # Split course data into matrix.
            self.course = [list(i) for i in dd]
            self.__n_rows = len(self.course)
            self.__n_cols = len(self.course[0])

    @property
    def n_rows(self):
        return self.__n_rows
    
    @n_rows.setter
    def n_rows(self, value):
        if isinstance(value, int):
            self.__n_rows = value
        else:
            self.__n_rows = 0

    @property
    def n_cols(self):
        return self.__n_cols
    
    @n_cols.setter
    def n_cols(self, value):
        if isinstance(value, int):
            self.__n_cols = value
        else:
            self.__n_cols = 0            

# c = Course()
# c.generate(raw_data)

class Attempt:
    def __init__(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.__v_incr: int = (down - up)
        self.__h_incr: int = (right - left)
        
        self.hits: int = 0      # How many trees hit
        self.pos: list = [0, 0] # Starting coordinates for an attempt.
    
    def __repr__(self):
        return f"<Attempt l: {self.left}, r: {self.right}, u: {self.up}, d:{self.down}>"

    @property
    def v_incr(self):
        return self.__v_incr
    
    @v_incr.setter
    def v_incr(self, value):
        if isinstance(value, int):
            self.__v_incr = value
        else:
            self.__v_incr = 1

    @property
    def h_incr(self):
        return (self.right - self.left)
    
    @h_incr.setter
    def h_incr(self, value):
        if isinstance(value, int):
            self.__h_incr = value
        else:
            self.__h_incr = 1
            
        
            


class Attempts(Course):
    
    ALL_HITS: list = []
    
    def __init__(self, data: str, directions: list):
        super().__init__()
        self.data = data
        self.dirs = directions
        self.generate(self.data)

    def __repr__(self):
        return f"<Attempts rows: {self.n_rows}, cols: {self.n_cols}/>"


    def __run(self, direction):
        """Run attempt."""
        
        #TODO: Fix this section.  Kind of close, but not really.
        self.generate(self.data)
        woods = self.course
        n_rows = self.n_rows
        n_cols = self.n_cols
        
        # Create Attempt instance
        a = Attempt(right = direction[0], down = direction[1])
        print(a)
        r = 0
        while r < n_rows:

            # Set vert and horiz variables.
            v, h = a.pos[0], a.pos[1]
            print(v, h)
            
                
            # If we run out of columns, add more!
            if h > n_cols:
                print("Expanding course columns.")
                for w in n_rows:
                    woods[w] += woods[w]
                n_cols = len(woods[0])

            if woods[v][h] == "#":
                a.hits += 1

            # Increment coordinate position by vertical and horizontal steps.
            a.pos[0] += a.v_incr
            a.pos[1] += a.h_incr
            r += a.pos[0] # Increment r indexer


        self.ALL_HITS.append(a.hits)
        

    def run_all(self):
        for d in self.dirs:
            self.__run(d)
            
        if len(self.ALL_HITS) > 0:
            print(f"Trees hit for each run were: {self.ALL_HITS}")
            print(f"The product of all the hits is: {product(self.ALL_HITS)}")
        
        

# fields = [i for i in dir(SkiDirection) if not str(i).startswith("_")]
    

given = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
    ]

# attempts = [
#     Attempt(right = i[0], down = i[1]) for i in given
#     ]


attempts = Attempts(raw_data, given)

attempts.run_all()


hits = 0 # How many trees are hit?
pos = [0, 0]
while pos[0] < n_rows:
    # Set interim vertical and horizontal variables for easier interpretation
    v, h = pos[0], pos[1]
    
    # If we run out of columns, add more!
    if h > n_cols:
        woods[v:] = [w * 2 for w in woods[v:]]
        n_cols *= 2

    if woods[v][h] == "#":
        hits += 1
        
    # Increment coordinate position by vertical and horizontal steps.
    pos[0] += v_incr
    pos[1] += h_incr





# --- Data for Testing --- #
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



if __name__ == "__main__":
    # Run docstring tests
    import doctest
    doctest.testmod()
