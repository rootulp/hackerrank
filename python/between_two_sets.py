#!/bin/python3

import sys
from functools import reduce


def multiples_of_a_divisors_of_b(lcm, gcd):
    result = []
    multiplyer = 1
    while (lcm * multiplyer <= gcd):
        if (gcd % (lcm * multiplyer) == 0):
            result.append(lcm * multiplyer)
        multiplyer += 1
    return result


# Import gcd and lcm from https://gist.github.com/endolith/114336
def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)


def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)


if __name__ == "__main__":
    n, m = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    print(len(multiples_of_a_divisors_of_b(lcm(*a), gcd(*b))))
