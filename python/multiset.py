#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter

class Multiset:

    def __init__(self):
        self.counter = Counter()

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.counter[val] += 1

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if(self.counter[val] > 0):
            self.counter[val] -= 1

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return self.counter[val] > 0

    def __len__(self):
        return sum(self.counter.values())
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
