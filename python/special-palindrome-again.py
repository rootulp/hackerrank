#!/bin/python3

from itertools import groupby

# Special palindromic string conditions:
# 1. All of the characters are the same, e.g. aaa.
# 2. All characters except the middle one are the same, e.g. aadaa.

# Referenced this hint:
# 1. Build a list of tuples such that the string "aaabbc" => [("a", 3), ("b", 2), ("c", 1)].
# 2. The number of substrings that satisfy condition 1 above is a triangle
#    number where n = the count in the tuple. See:
#    https://en.wikipedia.org/wiki/Triangular_number
# 3. The number of substrings that satisfy condition 2 above can be found
#    by searching through the list of tuples.

def count_of_special_palindrome_substrings(string):
    count = 0

    # Step 1
    encoded = run_length_encode(string)

    # Step 2
    for char, run_length in encoded:
        count += triangle_number(run_length)

    # Step 3
    for i in range (1, len(encoded) - 1):
        char, run_length = encoded[i]
        only_one_middle_character = run_length == 1
        surrounded_by_same_character = encoded[i - 1][0] == encoded[i + 1][0]
        if only_one_middle_character and surrounded_by_same_character:
            count += min(encoded[i - 1][1], encoded[i + 1][1])

    return count

def run_length_encode(string):
    return [(char, len(list(group))) for char, group in groupby(string)]

def triangle_number(n):
    return n * (n + 1) // 2

if __name__ == '__main__':
    _ = int(input())
    string = input()
    print(count_of_special_palindrome_substrings(string))
