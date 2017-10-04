#!/bin/python3
import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
print(sum([cupcake * 2 ** index for index, cupcake
           in enumerate(reversed(sorted(calories)))]))
