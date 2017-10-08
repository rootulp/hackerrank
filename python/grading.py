#!/bin/python3

import sys


def round(grade):
    return grade if grade < 38 else round_up(grade)


def round_up(grade):
    if (grade + 1) % 5 == 0:
        return grade + 1
    elif (grade + 2) % 5 == 0:
        return grade + 2
    return grade


n = int(input().strip())
for _ in range(n):
    print(round((int(input().strip()))))
