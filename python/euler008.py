#!/bin/python3

from functools import reduce


class LargestProduct(object):

    def __init__(self, num, num_consecutive_digits):
        self.num = num
        self.num_consecutive_digits = num_consecutive_digits

    def largest_product(self):
        return max(self.product_of_consecutive_digits())

    def product_of_consecutive_digits(self):
        return map(LargestProduct.product, self.consecutive_digits())

    def consecutive_digits(self):
        return LargestProduct.slices(LargestProduct.digits(self.num),
                                     self.num_consecutive_digits)

    @staticmethod
    def slices(array, slice_length):
        return [array[i:i + slice_length] for i in
                range(len(array) - slice_length)]

    @staticmethod
    def digits(num):
        return [int(i) for i in str(num)]

    @staticmethod
    def product(array):
        return reduce((lambda x, y: x * y), array)


t = int(input().strip())
for a0 in range(t):
    _, num_consecutive_digits = map(int, input().strip().split(' '))
    num = input().strip()
    lp = LargestProduct(num, num_consecutive_digits)
    print(lp.largest_product())
