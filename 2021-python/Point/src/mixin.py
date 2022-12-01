
__all__ = [
    "PointNavigationMixin"
    ]

from src.base import PointBaseRC
from src.interface import IPointNavigation

class PointNavigationMixin(IPointNavigation):
    """Base point nabvigation class.  Will implement
    """    
    # Moving on normal Cartesian grid.
    def up(self, amount: int = 1):
        self.r -= amount

    def down(self, amount: int = 1):
        self.r += amount

    def left(self, amount: int = 1):
        self.c -= amount

    def right(self, amount: int = 1):
        self.c += amount

    def move(self, other: PointBaseRC):
        self.c += other.c
        self.r += other.r
