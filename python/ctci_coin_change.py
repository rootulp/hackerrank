#!/bin/python3

import sys
import copy
from collections import Counter

class hashabledict(dict):
  def __key(self):
    return tuple((k,self[k]) for k in sorted(self))
  def __hash__(self):
    return hash(self.__key())
  def __eq__(self, other):
    return self.__key() == other.__key()

class CoinChange(object):

    def __init__(self, available_coins, n):
        self.available_coins = available_coins
        self.n = n
        self.solutions = set()

    def make_change(self, n, coins_used = Counter()):
        if n < 0:
            return
        elif n == 0:
            self.solutions.add(hashabledict(coins_used))
        else:
            for coin in self.available_coins:
                coins = copy.deepcopy(coins_used)
                coins[coin] += 1
                self.make_change(n - coin, coins)


n, m = map(int, input().strip().split(' '))
available_coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
coin_change = CoinChange(available_coins, n)
coin_change.make_change(n)
print(len(coin_change.solutions))
