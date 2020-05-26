#!/bin/python3

import sys
import re

s = input().strip()
print(len(re.findall('[A-Z]', s)) + 1)
