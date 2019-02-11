#!/bin/python3

import math
import os
import random
import re
import sys

# To address with DP, work through the array, keeping track of the max at each position until you get to the last value of the array. You should start with the base cases defined before iterating through the remainder of the array.
# max @ position 0: value @ 0
# max @ position 1: either:
# value @ 0
# value @ 1
# from that point forward, the max of the next position is either:
# the current value at that position
# the max value found so far
# the max value from 2 positions back plus the current value
# keep track of the max at each position until you get to the last position of
# the array

def max_subset_sum(array):
    max_so_far = [None for i in range(len(array))]
    max_so_far[0] = array[0]
    max_so_far[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        take_only_this_element = array[i]
        do_not_take_this_element = max_so_far[i - 1]
        take_this_element = max_so_far[i - 2] + array[i]
        max_so_far[i] = max(take_only_this_element, do_not_take_this_element, take_this_element)

    return max_so_far[-1]


if __name__ == '__main__':
    _ = int(input())
    array = list(map(int, input().rstrip().split()))
    result = max_subset_sum(array)
    print(str(result))
