#!/bin/python3

import math
import os
import random
import re
import sys

def countInversions(arr):
    return bubbleSort(arr)


# Sort array via bubble sort and return the number of swaps performed
def bubbleSort(arr):
    swaps = 0

    performedSwapInCurrentPass = True # Set to True initially to trigger first pass
    while (performedSwapInCurrentPass == True):
        performedSwapInCurrentPass = False
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swaps += 1
                performedSwapInCurrentPass = True

    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    num_test_cases = int(input())
    for _test_case in range(num_test_cases):
        _ = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        fptr.write(str(result) + '\n')
    fptr.close()
