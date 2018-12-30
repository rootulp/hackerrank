#!/bin/python3

import math
import os
import random
import re
import sys

# Referenced the following notes:
# 1) O(N) solution is possible using stacks; avoid DP for this problem
# 2) Think about how to identify the largest window a number is the minimum for (e.g. for the sequence 11 2 3 14 5 2 11 12 we would make a map of number -> window_size as max_window = {11: 2, 2: 8, 3: 3, 14: 1, 5: 2, 12: 1}) - this can be done using stacks in O(n)
# 3) Invert the max_window hashmap breaking ties by taking the maximum value to store a mapping of windowsize -> maximum_value (continuing with example above inverted_windows = {1: 14, 8:2, 3:3, 2:11}
# 4) starting from w=len(arr) iterate down to a window size of 1, looking up the corresponding values in inverted_windows and fill missing values with the previous largest window value (continuing with the example result = [2, 2, 2, 2, 2, 3, 11, 14] )
# 5) Return the result in reverse order (return [14, 11, 3, 2, 2, 2, 2, 2])

def riddle(arr):
    return largest_window_left(arr)

def largest_window_left(arr):
    num_elements_minimum = [None] * len(arr) # Initialize a list to capture the number of elements to the left of the current value for which the current value is the minimum.
    num_elements_minimum[0] = 1 # The first element always has a span of one because nothing comes before it.
    index_of_last_min_element = [0] # Use a stack to store the index of the last element smaller than the current element.

    for index in range(1, len(arr)):
        while len(index_of_last_min_element) > 0 and arr[index] <= arr[index_of_last_min_element[-1]]:
            index_of_last_min_element.pop()

        if len(index_of_last_min_element) == 0:
            num_elements_minimum[index] = index + 1
        else:
            num_elements_minimum[index] = index - index_of_last_min_element[-1]

        index_of_last_min_element.append(index)
        print("num_elements_minimum {}, index_of_last_min_element {}".format(num_elements_minimum, index_of_last_min_element))

    return num_elements_minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _num_elements = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = riddle(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
