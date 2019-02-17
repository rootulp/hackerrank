#!/bin/python3

import math
import os
import random
import re
import sys

class CastleOnGrid:

    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def min_moves(self):
        pass

if __name__ == '__main__':
    grid_size = int(input())
    grid = []

    for _ in range(grid_size):
        grid.append(list(input()))

    coords = list(map(int, input().split()))
    start = (coords[0], coords[1])
    goal = (coords[2], coords[3])

    castle_on_grid = CastleOnGrid(grid, start, goal)
    min_moves = castle_on_grid.min_moves()
    print(min_moves)
