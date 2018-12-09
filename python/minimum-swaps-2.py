#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    return sortInPlace(arr)

def sortInPlace(arr):
    swaps = 0
    index = 0
    while index < len(arr):
        element = arr[index]
        if (element - 1 == index):
            index += 1
        else:
            print("swapping: {} and {}".format(arr[element - 1], arr[index]))
            arr[element - 1], arr[index] = arr[index], arr[element - 1]
            swaps += 1
    print(arr)
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
