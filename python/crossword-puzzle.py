#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
