#!/bin/python3

import math
import os
import random
import re
import sys


# NOTE: This only passes the first three test cases.
def taskOfPairing(freq):
    total = number_of_identical_pairs(freq)
    total += number_of_off_by_one_pairs(freq)
    return total

def number_of_identical_pairs(freq):
    pairs = []
    for i in range(len(freq)):
        for n in range(freq[i] // 2):
            pairs.append([i, i])
    # print("identical pairs", pairs)
    return(len(pairs))

def number_of_off_by_one_pairs(freq):
    remainder = [i % 2 for i in freq]
    pairs = []
    for i in range(len(remainder) - 1):
        if (remainder[i] == 1 and remainder[i + 1] == 1):
            pairs.append([i, i+1])
            remainder[i] -= 1
            remainder[i + 1] -= 1
    # print("off by one pairs", pairs)
    return(len(pairs))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    freq_count = int(input().strip())

    freq = []

    for _ in range(freq_count):
        freq_item = int(input().strip())
        freq.append(freq_item)

    result = taskOfPairing(freq)

    fptr.write(str(result) + '\n')

    fptr.close()
