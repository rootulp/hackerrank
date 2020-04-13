#!/bin/python3

import math
import os
import random
import re
import sys


from itertools import zip_longest

#
# Complete the 'minimumSwaps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING status as parameter.
#

# NOTE: This only passes the first three test cases.
def minimumSwaps(status):
    return min(num_swaps_to_start_with_sale(status), num_swaps_to_start_with_regular(status))

def num_swaps_to_start_with_sale(status):
    swaps = 0
    groups = grouper(status, 2)
    for group in groups:
        a, b = group
        if(a != None and a != 'S'):
            swaps += 1
        elif(b != None and b != 'R'):
            swaps += 1
    return swaps

def num_swaps_to_start_with_regular(status):
    swaps = 0
    groups = grouper(status, 2)
    for group in groups:
        a, b = group
        if(a != None and a != 'R'):
            swaps += 1
        elif(b != None and b != 'S'):
            swaps += 1
    return swaps


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    status = input()

    result = minimumSwaps(status)

    fptr.write(str(result) + '\n')

    fptr.close()
