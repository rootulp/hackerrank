#!/bin/python3

import sys


house_left, house_right = map(int, input().strip().split(' '))
house_location = range(house_left, house_right + 1)
apple_tree, orange_tree = map(int, input().strip().split(' '))
_, _ = map(int, input().strip().split(' '))
apple_distances = map(int, input().strip().split(' '))
orange_distances = map(int, input().strip().split(' '))


def fruit_that_hit_house(tree, distances):
    return list(filter(lambda distance: tree + distance in house_location,
                       distances))


print(len(fruit_that_hit_house(apple_tree, apple_distances)))
print(len(fruit_that_hit_house(orange_tree, orange_distances)))
