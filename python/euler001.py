#!/bin/python3

def sum_of_multiples_below(max_num):
    return sum(set(multiples_of(3, max_num) + multiples_of(5, max_num)))

def multiples_of(n, max_num):
    return list(range(n, max_num, n))

test_cases = int(input().strip())
for _ in range(test_cases):
    max_num = int(input().strip())
    print(sum_of_multiples_below(max_num))
