#!/bin/python3

import sys


def minimum_absolute_difference(array):
    sorted_pairs = zip(sorted(array)[:-1], sorted(array)[1:])
    differences = [abs(a - b) for a, b in sorted_pairs]
    return min(differences)


if __name__ == "__main__":
    _ = int(input().strip())
    array = list(map(int, input().strip().split(' ')))
    print(minimum_absolute_difference(array))
