#!/bin/python3

import math
import os
import random
import re
import sys



# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
def reverse_words_order_and_swap_cases(sentence):
    return reverse_words(sentence.swapcase())

def reverse_words(sentence):
    return " ".join(reversed(sentence.split(" ")))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
