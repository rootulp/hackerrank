#!/bin/python3

import math
import os
import random
import re
import sys


class Crossword():

    EMPTY = "-"
    BLOCKED = "+"

    def __init__(self, grid, words):
        self.grid = grid
        self.words = words

    def solve(self):
        while self.is_unsolved():
            word = self.words.pop()
            positions = self.get_potential_positions(word)
            for position in positions:
                self.fill_word(word, position)
                self.solve()

                # if we get here, we need to revert this word
                self.revert_fill_word(word, position)
            self.words.append(word)
        return self.grid

    def get_potential_positions(self, word):
        pass

    def fill_word(self, word, position):
        pass

    def revert_fill_word(self, word, position):
        pass

    def is_unsolved(self):
        for row in self.grid:
            for token in row:
                if token == self.EMPTY:
                    return True
        return False


if __name__ == '__main__':
    grid = []
    for _ in range(10):
        grid.append(list(input()))
    words = input().split(";")

    puzzle = Crossword(grid, words)
    print(puzzle.solve())
