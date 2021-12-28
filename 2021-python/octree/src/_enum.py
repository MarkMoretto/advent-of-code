#!/bin/python

__all__ = [
    "Region"
    ]


from enum import Enum, auto


class AdjustedAuto(Enum):
    """Creates enum auto-numbering object that begins at zero."""
    def _generate_next_value_(name, start, count, last_values):
        return count

class Region(AdjustedAuto):
    TLF = auto() # Top left front
    TRF = auto() # Top right front
    BRF = auto() # Bottom right front
    BLF = auto() # Bottom left front
    TLB = auto() # Top left back
    TRB = auto() # Top right back
    BRB = auto() # Bottomr right back
    BLB = auto() # Bottom left back
