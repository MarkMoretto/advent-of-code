#!/bin/python

"""
Code for AOC 2021, day 6, from the following Gist:
    https://gist.github.com/p88h/d2a3664e6a38d894391dd18eb92b7d7d
"""

import numpy as np

def matrix_power(m, n, mod):
    e = m
    n -= 1
    while n > 0:
        if n % 2 == 1:
            m = np.dot(m, e) % mod
        e = np.dot(e, e) % mod
        n //= 2
    return m

t = np.array([[0,1,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0],
              [0,0,0,0,1,0,0,0,0],
              [0,0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,1,0,0],
              [1,0,0,0,0,0,0,1,0],
              [0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0]], dtype=object)

# v = np.bincount(list(map(int, input().split(","))), minlength=9)
# use precomputed reddit input 
v = np.array([22, 20, 16, 11, 7, 9, 13, 7, 0])

print(np.dot(matrix_power(t, 10**100, 10**20), v).sum() % (10**20))
