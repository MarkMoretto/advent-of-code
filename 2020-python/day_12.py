
"""
Purpose: Advent of Code challenge
Day: 12
Date created: 2020-12-11
URL: https://adventofcode.com

Contributor(s):
    Mark M.
"""

import re
import math
from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """F10
N3
F7
R90
F11
"""

else:
    # Current file filepath
    thisfile = current_file(__file__)
    
    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-12-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
try:
    data = list(map(int, get_lines(raw_data)))
except ValueError:
    pass
finally:
    data = get_lines(raw_data)




# --- Functions --- #

def deg_to_cardinal(d):
    dirs = ["E", "ESE", "SE", "SSE",
            "N", "NNE", "NE", "ENE",
            "W", "WNW", "NW", "NNW",
            "S", "SSW", "SW", "WSW",
            ]

    dir_len = len(dirs)
    idx = round(d / (360. / dir_len))
    return dirs[idx % dir_len]


def get_deg(direction):
    """Return degree for a given cardinal direction (string)."""
    return [k for k, v in coords.items() if v == direction][0]


def new_dir(current_deg, command, rotation_deg):
    """Get new direction (in degrees) based on current direction and rotation command.

    Rotation command should be L or R.
    """
    if command == "R":
        tmp = (current_deg - rotation_deg) % 360
    else:
        tmp = (current_deg + rotation_deg) % 360

    radians_ = (tmp * math.pi) / 180.
    return int(radians_ * (180 / math.pi))


def coord_dir(degrees):
    """Get coordinates for movement based on current direction (in degrees).

    >>> coord_dir(0)
    (1, 0)
    >>> coord_dir(90)
    (0, 1)   
    >>> coord_dir(180)
    (-1, 0)
    >>> coord_dir(270)
    (0, -1)
    """
    xx = round(math.cos(math.radians(degrees)%360), 0)
    yy = round(math.sin(math.radians(degrees)%360), 0)
    return (int(xx), int(yy))


def manhattan(coordinates, origin=(0,0)):
    """Manhattan distance calculaton function."""
    return abs(origin[0]-coordinates[0])+abs(origin[1]-coordinates[1])

# Create coordinate dictonary
coords = {i:deg_to_cardinal(i) for i in range(0, 361, 90)}


# Regex to separate characters and numbers, compiled.
pcmd = re.compile(r"\d+",)
pnum = re.compile(r"\D+",)



####################################
######### --- Part 1 --- ###########
####################################

facing = "E"
facing_deg = get_deg(facing)
position = [0, 0]
move_coords = coord_dir(facing_deg)
for d in data:

    cmd, amt = pcmd.sub("", d), int(pnum.sub("", d))

    # Rotation
    if cmd in ("L", "R"):
        # Get new facing direction (in degrees)
        facing_deg = new_dir(facing_deg, cmd, amt)
        # Get new facing direction (as string)
        facing = coords[facing_deg]
        # Set new move coordinates
        move_coords = coord_dir(facing_deg)

    # Move forward
    elif cmd == "F":
        for i in range(2):
            position[i] += (move_coords[i] * amt)


    else:
        # Move in direction; Facing variable remains the same.
        dir_coords = coord_dir(get_deg(cmd))
        for i in range(2):
            position[i] += (dir_coords[i] * amt)

    # print(direction, position)


def manhattan(coordinates):
    return abs(0-coordinates[0])+abs(0-coordinates[1])

result = manhattan(position)
print(f"Part 1: The final Manhattan distance is: {result}")



####################################
######### --- Part 2 --- ###########
####################################

def relative_coords(base_coords, rela_coords):
    xx = base_coords[0] + rela_coords[0]
    yy = base_coords[1] + rela_coords[1]
    return [xx, yy]

def rotate_wp(base_coords, waypoint, angle):
    """
    Rotate waypoint counterclockwise around base coordinates.

    Parameter `angle` should be given in radians, so pass math.radians(<deg>)
                or calculate by: (degrees * PI) / 180.
    """
    bx, by = base_coords
    wpx, wpy = waypoint

    sin_ = math.sin(angle)
    cos_ = math.cos(angle)
    qx = round(bx + cos_ * (wpx - bx) - sin_ * (wpy - by), 0)
    qy = round(by + sin_ * (wpx - bx) + cos_ * (wpy - by), 0)
    return [int(qx), int(qy)]


facing = "E"
facing_deg = get_deg(facing)
position = [0, 0]

# Waypoint buffer
wpb = [10, 1]

# Set actual waypoint coordinates.
waypoint = relative_coords(position, wpb)

#
move_coords = coord_dir(facing_deg)
for d in data:
    cmd, amt = pcmd.sub("", d), int(pnum.sub("", d))
    # print(f"Cmd: {cmd}\tAmt: {amt}")

    # Rotation. Should rotate waypoint about ship.
    if cmd in ("L", "R"):
        if cmd == "L":
            # Update buffer only since ship doesn't move with this command.
            wpb = rotate_wp((0,0), wpb, math.radians(amt))
        else:
            wpb = rotate_wp((0,0), wpb, math.radians(-amt))

    # Move forward
    elif cmd == "F":
        # Increase amount by factor of 10.
        for i in range(2):
            # position[i] += (move_coords[i] * (waypoint[i] * amt))
            position[i] += (wpb[i] * amt)


    # Directional movement.  Should affect waypoint buffer only.
    else:
        # Move in direction; Facing variable remains the same.
        dir_coords = coord_dir(get_deg(cmd))
        for i in range(2):
            wpb[i] += (dir_coords[i] * amt)

    # Update waypoint with relative coords to ship.  This is usually required
    # after each command, so placing it here reduces redundancies.
    waypoint = relative_coords(position, wpb)

    # print(f"WP: {waypoint}\tWPB: {wpb}\tPos.: {position}")


result = manhattan(position)
print(f"Part 2: The final Manhattan distance is: {result}")


