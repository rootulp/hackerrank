#!/bin/python3

import sys


house_left, house_right = map(int, input().strip().split(' '))
apple_tree, orange_tree = map(int, input().strip().split(' '))
_, _ = map(int, input().strip().split(' '))
apple_distances = map(int, input().strip().split(' '))
orange_distances = map(int, input().strip().split(' '))
print(len(list((filter(lambda apple_distance: house_left <= apple_tree + apple_distance <= house_right, apple_distances)))))
print(len(list(filter(lambda orange_distance: house_left <= orange_tree + orange_distance <= house_right, orange_distances))))
