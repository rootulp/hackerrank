#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimum_bribes(final_line):
    if invalid(final_line):
        return "Too chaotic"
    return bubble_sort(final_line)


def invalid(final_line):
    return any(did_bribe_more_than_two_people(person, index)
               for index, person in enumerate(final_line))


def did_bribe_more_than_two_people(person, index):
    return index + 2 < person - 1


def bubble_sort(line):
    swaps = 0
    swapped_in_current_pass = False

    for person in range(len(line)):
        for i in range(0, len(line) - 1):
            if line[i] > line[i + 1]:
                line[i], line[i + 1] = line[i + 1], line[i]
                swaps += 1
                swapped_in_current_pass = True
        if swapped_in_current_pass:
            swapped_in_current_pass = False
        else:
            break

    return swaps


if __name__ == '__main__':
    t = int(input())
    for _t_index in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        print(minimum_bribes(q))
