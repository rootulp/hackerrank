#!/bin/python3

import math
import os
import random
import re
import sys

# Referenced https://www.geeksforgeeks.org/largest-rectangle-under-histogram/


def largestRectangle(heights):
    stack = list()
    index = 0
    largest_rectangle = 0

    while index < len(heights):
        if (not stack) or (heights[stack[-1]] <= heights[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            largest_rectangle = max(largest_rectangle, area)

    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        largest_rectangle = max(largest_rectangle, area)

    return largest_rectangle


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
