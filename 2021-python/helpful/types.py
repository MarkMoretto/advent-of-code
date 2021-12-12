#!/bin/python

__all__ = [
    "Dict",
    "Float",
    "IntList",
    "Integer",
    "Iterator",
    "List",
    "Matrix",
    "NumList",
    "Number",
    "String",
    "Union",
    ]

from typing import Dict, Iterator, List, Union

# Types
String = str
Integer = int
Float = float
Number = Union[int, float]
IntList = List[Integer]
NumList = List[Number]

Matrix = List[IntList]
