#!/bin/python

import octree

def insert_and_check() -> None:
    """Octree demo function.

    Steps:
    1. Create Octree.
    2. Add two points.
    3. Verify that a point was added.
    """
    pt1 = octree.Point(1, 1, 1)
    pt2 = octree.Point(4, 4, 4)

    point1 = octree.Point(3, 3, 3)
    point2 = octree.Point(3, 3, 4)

    o = Octree(pt1, pt2)
    o.insert(point1)
    o.insert(point2)
    if o.contains(point1):
        print(f"Tree contains point {point1}")
