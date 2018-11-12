#!/bin/python3

import os
import sys

# n: the integer number of sticks to buy
# k: the integer number of box sizes the store carries
# b: the integer number of boxes to buy
def bonetrousle(n, k, b):
    if (minimumValue(k, b) <= n <= maximumValue(k, b)):
        return boxesToBuy(n, k, b)
    else:
        return -1

# The minimum number of sticks that may be purchased
def minimumValue(k, b):
    return 0

# The maximum number of sticks that may be purchased
def maximumValue(k, b):
    return 100

# One possible solution of boxes that sum to n
def boxesToBuy(n, k, b):
    return [0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nkb = input().split()

        n = int(nkb[0])

        k = int(nkb[1])

        b = int(nkb[2])

        result = bonetrousle(n, k, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
