#!/bin/python3

import math
import os
import random
import re
import sys


def dynamic_array(num_sequences, queries):
    sequence_list = [[] for i in range(num_sequences)]
    last_answer = 0

    for query, x, y in queries:
        index = get_sequence_index(num_sequences, x, last_answer)
        sequence = sequence_list[index]

        if query == 1:
            sequence.append(y)
        elif query == 2:
            last_answer = get_new_answer(sequence, y)
            print(last_answer)


def get_sequence_index(num_sequences, x, last_answer):
    return (x ^ last_answer) % num_sequences


def get_new_answer(sequence, y):
    index = y % len(sequence)
    return sequence[index]


if __name__ == '__main__':
    num_sequences, num_queries = tuple(map(int, input().rstrip().split()))
    queries = []

    for _ in range(num_queries):
        queries.append(list(map(int, input().rstrip().split())))

    dynamic_array(num_sequences, queries)
