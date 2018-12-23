#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import copy


def isValid(s):
    return "YES" if containsOnlyOneDifferentCharacterCount(s) else "NO"


def containsOnlyOneDifferentCharacterCount(string):
    characterCounts = Counter(string)
    if allOccurencesAreEqual(characterCounts):
        return True
    else:
        # Try to remove one occurence of every character
        for character in characterCounts:
            characterCountWithOneRemovedCharacter = characterCounts.copy()
            characterCountWithOneRemovedCharacter[character] -= 1
            characterCountWithOneRemovedCharacter += Counter() # remove zero and negative counts
            if allOccurencesAreEqual(characterCountWithOneRemovedCharacter):
                return True
    return False


def allOccurencesAreEqual(dict):
    return len(set(dict.values())) == 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
