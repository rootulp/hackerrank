#!/bin/python3

from collections import Counter

def most_common(birds):
    return Counter(birds).most_common(1)[0][0]

_ = int(input().strip())
BIRDS = list(map(int, input().strip().split(' ')))
print(most_common(BIRDS))
