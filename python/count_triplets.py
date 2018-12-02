#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def countTriplets(arr, r):
    potential_triplets_with_middle = Counter()
    potential_triplets_with_end = Counter()
    total_triplets = 0
    for num in arr:
        # num completed potential_triplets_with_end[num] triplets
        if potential_triplets_with_end[num]:
            total_triplets += potential_triplets_with_end[num]

        # num can be the middle number in
        # potential_triplets_with_middle[num] triplets
        if potential_triplets_with_middle[num]:
            potential_triplets_with_end[num * r] += \
                potential_triplets_with_middle[num]

        # num can be the begining of a triplet
        potential_triplets_with_middle[num * r] += 1
    return total_triplets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
