#!/bin/python3

import math
import os
import random
import re
import sys


def max_luck_balance(contests, num_can_lose):
    """
    Returns a single integer denoting the maximum amount of luck Lena can have
    after all the contests.
    """
    balance = 0

    # We can lose all unimportant contests.
    unimportant_contests = [contest for contest in contests if contest[1] == 0]
    for contest_luck, _is_important in unimportant_contests:
        balance += contest_luck

    # Sort the important contests in descending order of luck balance.
    important_contests = sorted(
        [contest for contest in contests if contest[1] == 1], reverse=True)

    # We want to lose as many of the high balance contests as possible.
    contests_to_lose = (important_contests)[:num_can_lose]

    # We must win the remaining contests.
    contests_to_win = (important_contests)[num_can_lose:]

    for contest_luck, _is_important in contests_to_lose:
        balance += contest_luck

    for contest_luck, _is_important in contests_to_win:
        balance -= contest_luck

    return balance


if __name__ == '__main__':
    num_contests, num_can_lose = map(int, input().split())

    contests = []
    for _ in range(num_contests):
        contests.append(tuple(map(int, input().rstrip().split())))

    result = max_luck_balance(contests, num_can_lose)
    print(result)
