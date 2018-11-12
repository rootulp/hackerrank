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
        return [-1]

# The minimum number of sticks that may be purchased
# Equivalant to: 1 + 2 + 3 ... b
# See: https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
def minimumValue(k, b):
    return b * (1 + b) / 2

# The maximum number of sticks that may be purchased
# Equivalant to: (k - b + 1) ... (k - 2) + (k -1) + k
# See: https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
def maximumValue(k, b):
    return b * ((k - b + 1) + k) / 2

# One possible solution of boxes that sum to n
def boxesToBuy(n, k, b):
    boxes = list(range(1, b + 1))
    (quotient, remainder) = divmod((n - int(minimumValue(k, b))),  b)
    boxes = list(map(lambda box: box + quotient, boxes))
    for i in range(len(boxes) - 1, len(boxes) - remainder - 1, -1):
        boxes[i] += 1

    return boxes



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
