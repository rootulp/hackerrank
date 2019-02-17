#!/bin/python3

import math
import os
import random
import re
import sys

def count_of_special_palindrome_substrings(string):
    count = 0
    for substring in substrings(string):
        if is_special_palindromic(substring):
            count += 1
    return count

def substrings(string):
    length = len(string)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield string[start:end]

def is_special_palindromic(string):
    return all_characters_are_same(string) or all_characters_except_middle_are_same(string)

def all_characters_are_same(string):
    return len(set(string)) == 1

def all_characters_except_middle_are_same(string):
    string_length_is_odd = len(string) % 2 == 1
    middle = len(string) // 2
    string_without_middle_character = string[:middle] + string[middle + 1:]
    return string_length_is_odd and all_characters_are_same(string_without_middle_character)


if __name__ == '__main__':
    _ = int(input())
    string = input()
    print(count_of_special_palindrome_substrings(string))
