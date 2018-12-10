#!/bin/python3

import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    array = [0] * n
    for a, b, k in queries:
        # Start is a - 1 because this is a one indexed array
        for i in range(a - 1, b):
            array[i] += k
            print(array)
    return max(array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
