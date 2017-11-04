#!/bin/python3

import bisect

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def generate_palindromes():
    return [i * j
            for i in range(100, 1000)
            for j in range(100, 1000)
            if is_palindrome(i * j)]

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

palindromes = sorted(generate_palindromes())
test_cases = int(input().strip())
for _ in range(test_cases):
    n = int(input().strip())
    print(find_lt(palindromes, n))
