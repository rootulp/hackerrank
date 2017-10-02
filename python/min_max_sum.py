#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
minimal_sum = sum(arr) - max(arr)
maximal_sum = sum(arr) - min(arr)
print(str(minimal_sum) + " " + str(maximal_sum))
