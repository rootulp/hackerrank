#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

class CastleOnGrid:

    def __init__(self, grid, grid_size, start, goal):
        self.grid = grid
        self.grid_size = grid_size
        self.start = start
        self.goal = goal

    def min_moves(self):
        to_visit = deque()
        visited = []

        to_visit.append((self.start, 0))
        visited.append(self.start)

        current_coords = None
        while current_coords != self.goal:
            current_coords, current_depth = to_visit.popleft()
            for move in self.possible_moves(current_coords):
                if move not in visited:
                    to_visit.append((move, current_depth + 1))
                    visited.append(move)

        return current_depth

    def possible_moves(self, coords):
        possible = []

        row, col = coords
        for row_i in range(row + 1, self.grid_size):
            if self.grid[row_i][col] == 'X':
                break
            else:
                possible.append((row_i, col))

        for row_i in range(row - 1, -1, -1):
            if self.grid[row_i][col] == 'X':
                break
            else:
                possible.append((row_i, col))

        for col_i in range(col + 1, self.grid_size):
            if self.grid[row][col_i] == 'X':
                break
            else:
                possible.append((row, col_i))

        for col_i in range(col - 1, -1, -1):
            if self.grid[row][col_i] == 'X':
                break
            else:
                possible.append((row, col_i))

        return possible



if __name__ == '__main__':
    grid_size = int(input())
    grid = []

    for _ in range(grid_size):
        grid.append(list(input()))

    coords = list(map(int, input().split()))
    start = (coords[0], coords[1])
    goal = (coords[2], coords[3])

    castle_on_grid = CastleOnGrid(grid, grid_size, start, goal)
    # print(castle_on_grid.possible_moves((1, 1)))
    min_moves = castle_on_grid.min_moves()
    print(min_moves)
