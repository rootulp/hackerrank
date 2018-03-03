#!/bin/python3


def getRecord(scores):
    highest_score = scores[0]
    lowest_score = scores[0]
    times_score_increased = 0
    times_score_decreased = 0
    for score in scores:
        if score > highest_score:
            highest_score = score
            times_score_increased += 1
        elif score < lowest_score:
            lowest_score = score
            times_score_decreased += 1
    return times_score_increased, times_score_decreased


_ = int(input().strip())
SCORES = list(map(int, input().strip().split(' ')))
print(" ".join(map(str, getRecord(SCORES))))
