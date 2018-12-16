#!/bin/python3

import copy
import operator
from collections import Counter
from collections import defaultdict
from functools import reduce


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


class HashableDict(dict):
    def __key(self):
        return tuple((k, self[k]) for k in sorted(self))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()


class CoinChange(object):

    def __init__(self, available_coins, n):
        self.available_coins = available_coins
        self.n = n
        self.solutions = defaultdict(lambda: set())

    def make_change(self, dollars, coins_used=Counter()):
        current = sum(list(map(prod, dict(coins_used).items())))
        if current >= dollars:
            return
        elif (current != 0 and
              HashableDict(coins_used) not in self.solutions[current]):
            self.solutions[current].add(HashableDict(coins_used))
            return coins_used
        else:
            for coin in self.available_coins:
                coins = copy.deepcopy(coins_used)
                coins[coin] += 1
                coins_used_in_here = self.make_change(dollars, coins)
                self.solutions[current].add(HashableDict(coins_used_in_here))


n, m = map(int, input().strip().split(' '))
available = [int(coins_temp) for coins_temp in input().strip().split(' ')]
coin_change = CoinChange(available, n)
coin_change.make_change(n)
print(coin_change.solutions)
