#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
  output = []
  occurences = Counter()
  frequencies = Counter()

  for operation, value in queries:
    if (operation == 1):
      frequencies[occurences[value]] -= 1
      occurences[value] += 1
      frequencies[occurences[value]] += 1

    elif (operation == 2):
      frequencies[occurences[value]] -= 1
      occurences[value] -= 1
      frequencies[occurences[value]] += 1

    elif (operation == 3):
      if frequencies[value] > 0:
        output.append(1)
      else:
        output.append(0)

    print(occurences)
    print(frequencies)


  return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
