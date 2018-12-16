#!/bin/python3

import sys

_ = int(input().strip())
candle_heights = list(map(int, input().strip().split(' ')))
print(candle_heights.count(max(candle_heights)))
