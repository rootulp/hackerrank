#!/bin/python3

import math
import os
import random
import re
import sys

def riddle(arr):
    return arr

def windows(arr, window_length):
    return [arr[i : i + window_length] for i in range(len(arr) - window_length + 1)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _num_elements = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = riddle(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
