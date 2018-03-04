#!/bin/python3

import sys

class PythagoreanTriplet(object):

    def __init__(self, n):
        self.n = n

    def maximum_abc(self):
        m, n = self.find_triplet()
        # print("m is:", m)
        # print("n is:", n)
        if(m):
            return self.product_of_abc(m, n)
        else:
            return -1

    def find_triplet(self):
        for m in range(self.n, 0, -1):
            n = self.compute_n(m)
            # print("trying to find m is:", m)
            # print("trying to find n is:", n)
            if(n.is_integer() and m > n and n > 0):
                return m, int(n)
        return False, False

    def compute_n(self, m):
        return (self.n - 2 * m ** 2) / (2 * m)

    def product_of_abc(self, m, n):
        return self.compute_a(m, n) * self.compute_b(m, n) * self.compute_c(m, n)

    def compute_a(self, m, n):
        return m ** 2 - n ** 2

    def compute_b(self, m, n):
        return 2 * m * n

    def compute_c(self, m, n):
        return m ** 2 + n ** 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(PythagoreanTriplet(n).maximum_abc())
