#!/bin/python

# Local imports
from src._enum import Region
from src._point import Point
from src._types import List

class Octree:
    """Octree class.
    """
    def __init__(self, p1: Point = None, p2: Point = None) -> None:
        self.point: Point = None
        self.top_left_front: Point = None
        self.bottom_right_back: Point = None


        # List of child Octrees
        self.children: List[Octree | None] = [None for _ in range(Region.BLB.value+1)]

        if p1 is None and p2 is None:
            self.point = Point()
        elif not p1 is None and p2 is None:
            self.point = p1
        else:
            self._init_insert(p1, p2)

    def __iter__(self):
        return iter(self)


    def _init_insert(self, p1: Point, p2: Point):
        """Method to call if p1 and p2 present on class initialization.
        """
        if (p2.x < p1.x or p2.y < p1.y or p2.z < p1.z):
            return
        
        self.point = None

        # Set exteme points.
        self.top_left_front = p1
        self.bottom_right_back = p2

        # Create set of "empty" child octree objects.
        for i in range(Region.TLF.value, Region.BLB.value+1):
            self.children[i] = Octree()


    def invalid_point(self, pt: Point) -> bool:
        """Checking if point is valid compared to extemes of Octree."""
        # Alias exteme points.
        tlf = self.top_left_front
        brb = self.bottom_right_back        
        return (brb.x < pt.x < tlf.x) or (brb.y < pt.y < tlf.y) or (brb.z < pt.z < tlf.z)


    def insert(self, p: Point):
        """Insert point into structure."""
        if self.invalid_point(p):
            return
        
        # Set current region/position
        pos = self.current_position(p)
        
        # Alias child tree
        child_tree = self.children[pos]

        if self.children[pos] is None:
            self.children[pos].insert(p)
            return

        elif child_tree.point.x == -1:
            self.children[pos] = Octree(p)
            return

        else:
            # Alias exteme points.
            tlf = self.top_left_front
            brb = self.bottom_right_back

            # Set child point for easier visual comprehension.
            child_pt = self.children[pos].point
            self.children[pos] = None

            # Get midpoint measures.
            mid_x, mid_y, mid_z = self._get_mids()

            if pos == Region.TLF.value:
                self.children[pos] = Octree(Point(tlf.x, tlf.y, tlf.z), 
                                            Point(mid_x, mid_y, mid_z),
                                            )

            elif pos == Region.TRF.value:
                self.children[pos] = Octree(Point(mid_x+1, tlf.y, tlf.z), 
                                            Point(brb.x,  mid_y,  mid_z)
                                            )

            elif pos == Region.BRF.value:
                self.children[pos] = Octree(Point(mid_x+1, mid_y+1, tlf.z),
                                            Point(brb.x,   brb.y,   mid_z),
                                            )

            elif pos == Region.BLF.value:
                self.children[pos] = Octree(Point(tlf.x, mid_y+1, tlf.z),
                                            Point(mid_x, brb.y,   mid_z),
                                            )

            elif pos == Region.TLB.value:
                self.children[pos] = Octree(Point(tlf.x, tlf.y, mid_z+1),
                                            Point(mid_x, mid_y, brb.z),
                                            )

            elif pos == Region.TRB.value:
                self.children[pos] = Octree(Point(mid_x+1, tlf.y, mid_z+1),
                                            Point(brb.x,   mid_y, brb.z),
                                            )

            elif pos == Region.BRB.value:
                self.children[pos] = Octree(Point(mid_x+1, mid_y+1, mid_z+1),
                                            Point(brb.x,   brb.y,   brb.z),
                                            )

            elif pos == Region.BLB.value:
                self.children[pos] = Octree(Point(tlf.x, mid_y+1, mid_z+1),
                                            Point(mid_x, brb.y,   brb.z),
                                            )

            self.children[pos].insert(child_pt)
            self.children[pos].insert(p)

        print(f"Insert called.\nPosition of point {p}: {pos}")

    
    def contains(self, p: Point):
        if self.invalid_point(p):
            return
        
        print(f"Contains called.")

        pos = self.current_position(p)
        child_tree = self.children[pos]

        if child_tree.point is None:
            return self.children[pos].contains(p)
        
        elif p.x == child_tree.point.x and p.y == child_tree.point.y and p.z == child_tree.point.z:
                return 1
        else:
            return 0


    def _get_mids(self) -> tuple:
        # Alias exteme points.
        tlf = self.top_left_front
        brb = self.bottom_right_back 

        # Bitshfit midpoints       
        _mid_x = (brb.x + tlf.x) >> 1
        _mid_y = (brb.y + tlf.y) >> 1
        _mid_z = (brb.z + tlf.z) >> 1
        print(f"Mid. (x, y, z) => ({_mid_x}, {_mid_y}, {_mid_z})")
        return _mid_x, _mid_y, _mid_z


    def current_position(self, p: Point):
        # Get midpoints.
        mid_x, mid_y, mid_z = self._get_mids()
        _pos = -1
        if p.x <= mid_x:
            if p.y <= mid_y:
                if p.z <= mid_z:
                    _pos = Region.TLF
                else:
                    _pos = Region.TLB
            else:
                if p.z <= mid_z:
                    _pos = Region.BLF
                else:
                    _pos = Region.BLB
                
        else:
            if p.y <= mid_y:
                if p.z <= mid_z:
                    _pos = Region.TRF
                else:
                    _pos = Region.TRB
            else:
                if p.z <= mid_z:
                    _pos = Region.BRF
                else:
                    _pos = Region.BRB
        # Return value of enum item.
        return _pos.value
