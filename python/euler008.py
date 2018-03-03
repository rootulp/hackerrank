#!/bin/python3

import sys
from functools import reduce

class LargestProduct:

    def __init__(self, num, num_consecutive_digits):
        self.num = num
        self.num_consecutive_digits = num_consecutive_digits

    def largest_product(self):
        return max(map(LargestProduct.product, LargestProduct.slices(LargestProduct.digits(self.num), self.num_consecutive_digits)))

    @staticmethod
    def slices(array, slice_length):
        return [array[i:i + slice_length] for i in range(len(array) - slice_length)]

    @staticmethod
    def digits(num):
        return [int(x) for x in str(num)]

    @staticmethod
    def product(array):
        return reduce((lambda x, y: x * y), array)

t = int(input().strip())
for a0 in range(t):
    _, num_consecutive_digits = map(int, input().strip().split(' '))
    num = input().strip()
    lp = LargestProduct(num, num_consecutive_digits)
    print (lp.largest_product())
