#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

class OccurencesAndFrequencies:
  """A data structure that optimizes for keeping
  track of the number of occurences of a given value
  and the frequencies of occurences"""

  def __init__(self):
    # Dict of value to occurences of that value
    self.occurences = Counter()
    # Dict of occurences to the frequency of occurence
    self.frequencies = Counter()

  def add(self, value):
    if (self.occurences[value] > 0):
      self.frequencies[self.occurences[value]] -= 1

    self.occurences[value] += 1
    self.frequencies[self.occurences[value]] += 1

  def remove(self, value):
    if (self.occurences[value] > 0):
      self.frequencies[self.occurences[value]] -= 1
      self.occurences[value] -= 1
      self.frequencies[self.occurences[value]] += 1

  def containsFrequencyOf(self, freq):
    return self.frequencies[freq] > 0

def freqQuery(queries):
  oAndF = OccurencesAndFrequencies()
  queryOutput = []

  for operation, value in queries:
    if (operation == 1):
      oAndF.add(value)

    elif (operation == 2):
      oAndF.remove(value)

    elif (operation == 3):
      if oAndF.containsFrequencyOf(value):
        queryOutput.append(1)
      else:
        queryOutput.append(0)

  return queryOutput

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
