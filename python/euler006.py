#!/bin/python3


def square_of_sum(n):
    return sum(range(n + 1)) ** 2


def sum_of_squares(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)


def sum_square_diff(n):
    return square_of_sum(n) - sum_of_squares(n)


test_cases = int(input().strip())
for _ in range(test_cases):
    n = int(input().strip())
    print(sum_square_diff(n))
