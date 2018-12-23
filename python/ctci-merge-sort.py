#!/bin/python3

import math
import os
import random
import re
import sys


# This solution times out on Hackerrank with Python 3
# However, it passes all test cases with Pypy 3

def countInversions(arr):
    global COUNT_INVERSIONS
    COUNT_INVERSIONS = 0
    mergeSort(arr)
    return COUNT_INVERSIONS


def mergeSort(arr):
    if (len(arr) <= 1):
        return arr

    # Split the array in two
    # Recursively sort both halves
    middle = len(arr) // 2
    arrLeft = mergeSort(arr[:middle])
    arrRight = mergeSort(arr[middle:])

    # Merge the two halves
    mergedArray = []
    leftIndex = 0
    rightIndex = 0
    global COUNT_INVERSIONS

    # Iterate through both lists and append the smaller element
    while(leftIndex < len(arrLeft) and rightIndex < len(arrRight)):
        if(arrLeft[leftIndex] <= arrRight[rightIndex]):
            mergedArray.append(arrLeft[leftIndex])
            leftIndex += 1
        else:
            mergedArray.append(arrRight[rightIndex])
            rightIndex += 1
            COUNT_INVERSIONS += len(arrLeft) - leftIndex

    # Append any left over elements
    mergedArray.extend(arrLeft[leftIndex:])
    mergedArray.extend(arrRight[rightIndex:])

    return mergedArray


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    num_test_cases = int(input())
    for _test_case in range(num_test_cases):
        _ = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        fptr.write(str(result) + '\n')
    fptr.close()
