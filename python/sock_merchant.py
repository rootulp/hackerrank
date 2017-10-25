#!/bin/python3

from collections import Counter

def pairs(socks):
    return sum(list(map(lambda sock: sock // 2, Counter(socks).values())))

_ = int(input().strip())
socks = list(map(int, input().strip().split(' ')))
print(pairs(socks))
