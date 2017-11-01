#!/bin/python3
# Project Euler #2: Even Fibonacci numbers

def fibonacci_sequence(n):
    sequence = [1, 2]
    while sequence[-1] + sequence[-2] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def evens(array):
    return list(filter(lambda x: x % 2 == 0, array))


test_cases = int(input().strip())
for _ in range(test_cases):
    n = int(input().strip())
    print(sum(evens(fibonacci_sequence(n))))
