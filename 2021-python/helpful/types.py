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
    "Union",
    ]

from typing import Callable, Dict, Iterable, Iterator, List, Union

# Types
String = str
Integer = int
Float = float
Number = Union[int, float]
IntList = List[Integer]
NumList = List[Number]

Matrix = List[IntList]
