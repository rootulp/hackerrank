#!/bin/python3

import math
import os
import random
import re
import sys



def countInversions(arr):
    global COUNT_INVERSIONS
    COUNT_INVERSIONS = 0
    mergeSort(arr)
    return COUNT_INVERSIONS


def mergeSort(arr):
    if (len(arr) <= 1):
        return arr

    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return merge(left, right)


def merge(arrLeft, arrRight):
    mergedArray = []
    leftIndex = 0
    rightIndex = 0
    global COUNT_INVERSIONS

    while(leftIndex < len(arrLeft) and rightIndex < len(arrRight)):
        if(arrLeft[leftIndex] <= arrRight[rightIndex]):
            mergedArray.append(arrLeft[leftIndex])
            leftIndex += 1
        else:
            mergedArray.append(arrRight[rightIndex])
            rightIndex += 1
            COUNT_INVERSIONS += len(arrLeft) - leftIndex

    # If there are any remaining elements in arrLeft
    # Append them to mergedArray
    while(leftIndex < len(arrLeft)):
        mergedArray.append(arrLeft[leftIndex])
        leftIndex += 1
        # COUNT_INVERSIONS += 1

    # If there are any remaining elements in arrLeft
    # Append them to mergedArray
    while(rightIndex < len(arrRight)):
        mergedArray.append(arrRight[rightIndex])
        rightIndex += 1

    # print("Merged array: {}".format(mergedArray))
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
