#!/bin/python3

# Note this solution times out on test case 9 with Python3.
# However, this solution passes test case 9 with Pypy3.

from collections import deque


class CastleOnGrid:

    CELL_BLOCKED_TOKEN = 'X'

    def __init__(self, grid, grid_size, start, goal):
        self.grid = grid
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.to_visit = deque()
        self.visited = []

    def min_moves(self):
        self.to_visit.append((self.start, 0))
        self.visited.append(self.start)

        current_coords = None
        while current_coords != self.goal:
            current_coords, current_depth = self.to_visit.popleft()
            for move in self.possible_moves(current_coords):
                # This is an optimization necessary to avoid timeouts on test
                # case 11.
                if move == self.goal:
                    return current_depth + 1
                else:
                    self.to_visit.append((move, current_depth + 1))
                    self.visited.append(move)

        return current_depth

    def possible_moves(self, coords):
        row, col = coords
        for row_i in range(row + 1, self.grid_size):
            if self.grid[row_i][col] == self.CELL_BLOCKED_TOKEN:
                break
            elif (row_i, col) in self.visited:
                continue
            else:
                yield (row_i, col)

        for row_i in range(row - 1, -1, -1):
            if self.grid[row_i][col] == self.CELL_BLOCKED_TOKEN:
                break
            elif (row_i, col) in self.visited:
                continue
            else:
                yield (row_i, col)

        for col_i in range(col + 1, self.grid_size):
            if self.grid[row][col_i] == self.CELL_BLOCKED_TOKEN:
                break
            elif (row, col_i) in self.visited:
                continue
            else:
                yield (row, col_i)

        for col_i in range(col - 1, -1, -1):
            if self.grid[row][col_i] == self.CELL_BLOCKED_TOKEN:
                break
            elif (row, col_i) in self.visited:
                continue
            else:
                yield (row, col_i)


if __name__ == '__main__':
    grid_size = int(input())
    grid = []

    for _ in range(grid_size):
        grid.append(list(input()))

    coords = list(map(int, input().split()))
    start = (coords[0], coords[1])
    goal = (coords[2], coords[3])

    castle_on_grid = CastleOnGrid(grid, grid_size, start, goal)
    print(castle_on_grid.min_moves())
