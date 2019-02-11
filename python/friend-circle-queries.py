#!/bin/python3

import math
import os
import random
import re
import sys

class FriendCircle:

    POPULATION = 10 ** 9

    def __init__(self):
        self.circles = [set([i]) for i in range(self.POPULATION)]

    def make_friendship(self, friend_a, friend_b):
        friends_of_a = self.find_set(friend_a)
        friends_of_b = self.find_set(friend_b)

        new_circle = friends_of_a.union(friends_of_b)
        self.circles.remove(friends_of_a)
        self.circles.remove(friends_of_b)
        self.circles.append(new_circle)

    def find_set(self, person):
        for subset in self.circles:
            if person in subset:
                return subset

    def largest_friend_circle(self):
        return max([len(circle) for circle in self.circles])

if __name__ == '__main__':

    friend_circle = FriendCircle()
    num_queries = int(input())
    for _ in range(num_queries):
        friend_a, friend_b = tuple(map(int, input().rstrip().split()))
        friend_circle.make_friendship(friend_a, friend_b)
        print(friend_circle.largest_circle_size())
