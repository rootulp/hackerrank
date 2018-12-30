#!/bin/python3

import math
import os
import random
import re
import sys

# Referenced the following notes:
# 1) O(N) solution is possible using stacks; avoid DP for this problem
# 2) Think about how to identify the largest window a number is the minimum for (e.g. for the sequence 11 2 3 14 5 2 11 12 we would make a map of number -> window_size as max_window = {11: 2, 2: 8, 3: 3, 14: 1, 5: 2, 12: 1}) - this can be done using stacks in O(n)
# 3) Invert the max_window hashmap breaking ties by taking the maximum value to store a mapping of windowsize -> maximum_value (continuing with example above inverted_windows = {1: 14, 2:11, 3:3, 8:2}
# 4) starting from w=len(arr) iterate down to a window size of 1, looking up the corresponding values in inverted_windows and fill missing values with the previous largest window value (continuing with the example result = [2, 2, 2, 2, 2, 3, 11, 14] )
# 5) Return the result in reverse order (return [14, 11, 3, 2, 2, 2, 2, 2])

def max_of_minima_for_every_window_size(arr):
    """Given an integer array of size, find the maximum of the minimum(s) of every window size in the array. The window size varies from 1 to n.
    """
    results = [None] * len(arr)
    inverted_map = inverted_max_window(arr)
    last_max = inverted_map[max(inverted_map.keys())]
    print("inverted_map {}".format(inverted_map))

    for w in range(len(results),  0,  -1):
        print("last_max {}".format(last_max))
        print("w {}".format(w))
        if w in inverted_map:
            results[w - 1] = inverted_map[w]
            last_max = inverted_map[w]
        else:
            results[w - 1] = last_max

    return results


def inverted_max_window(arr):
    inverted_windows = dict()
    max_window = largest_window_map(arr)

    for max_value, window_size in max_window.items():
        if window_size not in inverted_windows:
            inverted_windows[window_size] = max_value
        else:
            inverted_windows[window_size] = max(inverted_windows[window_size], max_value)

    print("inverted_max_window {}".format(inverted_windows))
    return inverted_windows


def largest_window_map(arr):
    max_window = dict()
    largest_window = largest_minima_window(arr)
    for number, window in zip(arr, largest_window):
        if number not in max_window:
            max_window[number] = window
        else:
            max_window[number] = max(max_window[number], window)

    print("max_window {}".format(max_window))
    return max_window

def largest_minima_window(arr):
    left_window = largest_window_left(arr)
    right_window = largest_window_right(arr)
    print ("left_window {}, right_window {}".format(left_window, right_window))
    largest_minima_window = []

    for left, right in zip(left_window, right_window):
        largest_minima_window.append(left + right - 1) # Subtract one to avoid double counting

    print ("largest_minima_window: {}".format(largest_minima_window))
    return largest_minima_window


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

def largest_window_right(arr):
    return list(reversed(largest_window_left(list(reversed(arr)))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _num_elements = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = max_of_minima_for_every_window_size(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
