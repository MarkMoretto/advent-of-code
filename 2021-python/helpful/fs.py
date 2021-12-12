#!/bin/python
# -*- coding: utf-8 -*-

__all__ = [
    "get_data",
    ]

"""
Purpose: Retrieve data files for AOC 2021
Date: 2021-12-12
Contributor(s):
    mark moretto
"""

from pathlib import Path

DATA_DIR = Path("data")

# Day of event
AOC_DAY: int

# Whether to use sample data file or not.
USE_SAMPLE_TF: bool = False



def get_data(aoc_day_number: int, use_sample: bool = True) -> str:
    def create_path(day_n, sample_tf) -> Path:
        """Returns Path object."""
        DATA_DIR.joinpath(f"day{day_n:0>2}{'-sample' if sample_tf else ''}.txt")

    DATA_FILEPATH = create_path(aoc_day_number, use_sample)

    return DATA_FILEPATH.open(mode="r", encoding="utf-8").read()
