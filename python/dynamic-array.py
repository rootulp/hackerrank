#!/bin/python3

import math
import os
import random
import re
import sys

def dynamicArray(num_sequences, queries):
    sequence_list = [[] for i in range(num_sequences)]
    last_answer = 0

    for query, x, y in queries:
        sequence = get_sequence(num_sequences, x, last_answer, sequence_list)
        if query == 1:
            sequence.append(y)
        elif query == 2:
            index = y % len(sequence)
            last_answer = sequence[index]
            print(last_answer)

def get_sequence(num_sequences, x, last_answer, sequence_list):
    index = (x ^ last_answer) % num_sequences
    return sequence_list[index]

if __name__ == '__main__':
    num_sequences, num_queries = tuple(map(int, input().rstrip().split()))
    queries = []

    for _ in range(num_queries):
        queries.append(list(map(int, input().rstrip().split())))

    dynamicArray(num_sequences, queries)
