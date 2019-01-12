#!/bin/python3

import math
import os
import random
import re
import sys


def minimumSwaps(arr):
    swaps = 0
    index = 0
    while index < len(arr):
        element = arr[index]
        if (index == element - 1):
            # This element is in the correct sorted position.
            index += 1
        else:
            # Move the element to the correct sorted position.
            # Do not increment index as an unsorted element could have been
            # swapped to the current index, therefore re-run this body.
            arr[element - 1], arr[index] = arr[index], arr[element - 1]
            swaps += 1

    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
