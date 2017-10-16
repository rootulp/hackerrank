#!/bin/python3

import sys


house_left, house_right = map(int, input().strip().split(' '))
house_location = range(house_left, house_right + 1)
apple_tree, orange_tree = map(int, input().strip().split(' '))
_, _ = map(int, input().strip().split(' '))
apple_distances = map(int, input().strip().split(' '))
orange_distances = map(int, input().strip().split(' '))
print(len(list((filter(lambda apple_distance: apple_tree + apple_distance in house_location, apple_distances)))))
print(len(list(filter(lambda orange_distance: orange_tree + orange_distance in house_location, orange_distances))))
