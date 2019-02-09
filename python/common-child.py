#!/bin/python3

import math
import os
import random
import re
import sys

# See https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def commonChild(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        if s1[-1] == s2[-1]:
            return commonChild(s1[:-1], s2[:-1]) + 1
        else:
            temp1 = commonChild(s1[:-1], s2)
            temp2 = commonChild(s1, s2[:-1])
            return max(temp1, temp2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()
