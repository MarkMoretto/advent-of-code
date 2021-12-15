#!/bin/python

__all__ = [
    "Callable",
    "Dict",
    "Float",
    "IntList",
    "Integer",
    "Iterable",
    "Iterator",
    "List",
    "Matrix",
    "NumList",
    "Number",
    "String",
    "Tuple",
    "Union",
    ]

from typing import Callable, Dict, Iterable, Iterator, List, Tuple, Union

# Types
String = str
Integer = int
Float = float
Number = Union[int, float]
IntList = List[Integer]
NumList = List[Number]

Matrix = List[IntList]
