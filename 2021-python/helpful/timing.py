#!/bin/python
#! -*- coding: utf-8 -*-

__all__ = [
    "timewrap"
    ]

from time import perf_counter
from functools import wraps


# def print_elapsed_time(start: float, stop: float) -> None:
#     time_diff = stop - start
#     n = 1
#     while time_diff < 1 and n <= 3:
#         time_diff *= 1000
#         n += 1

#     units = {1: "s", 2: "ms", 3: "µs", 4: "ns"}
#     print(f"Elapsed time: {time_diff:.2f} {units[n]}")


# https://docs.python.org/3/library/time.html#time.perf_counter
def timewrap(func):
    wraps(func)
    def inner(*args, **kwargs):
        _start = perf_counter()
        _value = func(*args, **kwargs)
        _stop = perf_counter()
        print(f"Elapsed time: {_stop-_start:0.3f}s")
        return _value
    return inner

