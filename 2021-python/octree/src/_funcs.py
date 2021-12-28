#!/bin/python

"""
Utility functions for octree data structure.


See:
    https://eisenwave.github.io/voxel-compression-docs/svo/construction.html
"""

from __future__ import annotations


def abs_svo(n: int) -> int:
    return -n^1 if (n^1)<0 else n

