#!/bin/python3

import math
import os
import random
import re
import sys

BRACKETS_MAP = {
    '[': ']',
    '{': '}',
    '(': ')',
}
def isOpen(bracket):
    return bracket in BRACKETS_MAP.keys()

def isClose(bracket):
    return bracket in BRACKETS_MAP.values()

def isBalanced(s):
    stack = []
    for bracket in s:
        if(isOpen(bracket)):
            stack.append(bracket)
        elif(isClose(bracket)):
            if(stack == [] or bracket != BRACKETS_MAP.get(stack.pop())):
                return ("NO")
    if(stack != []):
        return ("NO")
    return ("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
