#!/bin/python3

import math
import os
import random
import re
import sys

class FriendCircle:

    POPULATION = 10 ** 9

    def __init__(self):
        self.circles = {}
        self.circle_sizes = {}
        self.largest_friend_circle = 1

    def befriend(self, friend_a, friend_b):
        self.maybe_init_circle(friend_a)
        self.maybe_init_circle(friend_b)

        circle_a = self.find_circle(friend_a)
        circle_b = self.find_circle(friend_b)

        if circle_a != circle_b:
            self.circles[circle_b] = circle_a
            new_circle_size = self.circle_sizes[circle_a] + self.circle_sizes[circle_b]
            self.circle_sizes[circle_a] = new_circle_size
            self.circle_sizes[circle_b] = new_circle_size

            if new_circle_size > self.largest_friend_circle:
                self.largest_friend_circle = self.circle_sizes[circle_a]

    def find_circle(self, person):
        while self.circles[person] != person:
            person = self.circles[person]
        return person

    def maybe_init_circle(self, person):
        if person not in self.circles:
            self.circles[person] = person
            self.circle_sizes[person] = 1


if __name__ == '__main__':
    friend_circle = FriendCircle()
    num_queries = int(input())
    for _ in range(num_queries):
        friend_a, friend_b = tuple(map(int, input().rstrip().split()))
        friend_circle.befriend(friend_a, friend_b)
        print(friend_circle.largest_friend_circle)
