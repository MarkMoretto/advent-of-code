#!/bin/python
# -*- coding: utf-8 -*-

"""
Purpose: Advent of Code 2021 - Day 14
Date: 2021-12-14
URL: https://adventofcode.com/2021/day/14Contributor(s):
    mark moretto
"""

from __future__ import annotations

# from itertools import zip_longest
from collections import Counter, defaultdict

# Locals
from helpful.fs import get_data
from helpful.types import *


# Get data
AOC_DAY: int = 14
USE_SAMPLE_TF: bool = False
raw_data = get_data(AOC_DAY, USE_SAMPLE_TF)
seed, rules = raw_data.split("\n" * 2)

# Dictionary of letter pairs and letters to insert.
rules_map = dict(r.split(" -> ") for r in rules.splitlines())



# Update pair map and letter frequency counts on each iteration.
def update_pairs(pairs: Counter, letter_freqs: Counter) -> dict:
    new_map = defaultdict(int)
    for pair, freq in pairs.items():
        rule_value = rules_map[pair]
        new_map[pair[0] + rule_value] += freq
        new_map[rule_value + pair[1]] += freq
        letter_freqs[rule_value] += freq
    return new_map


def run(step_count: int) -> dict:
    """Run process based on step_count."""
    # Seed pair map and letter frequency counts
    pairs_map = Counter(a+b for a, b in zip(seed, seed[1:]))
    letter_freqs = Counter(seed)    
    for _ in range(N_STEPS):
        pairs_map = update_pairs(pairs_map, letter_freqs)
    return letter_freqs

def max_min(d: dict) -> tuple:
    d_values = d.values()
    return max(d_values), min(d_values)

##################
# --- Part 1 --- #
##################
N_STEPS: int = 10

letter_frequencies = run(N_STEPS)
freq_values = max_min(letter_frequencies)
result = max(freq_values) - min(freq_values)
print(f"Part 1 result: {result}")

##################
# --- Part 2 --- #
##################
N_STEPS: int = 40


letter_frequencies = run(N_STEPS)
freq_values = max_min(letter_frequencies)
result = max(freq_values) - min(freq_values)
print(f"Part 2 result: {result}")