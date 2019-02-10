#!/bin/python3

import math
import os
import random
import re
import sys

# Let's use an adapted form of Kruskal.
# 1. Construct a set for each city.
# 2. Iterate through edges in descending order of "cost to destroy".
# 3. If the edge connects two machines, we must destroy it so add to total time.
#    If the edge does not connect two machines, we do not need to destroy it.
# 4. After iterating through all edges, return total time

# From https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Pseudocode
# KRUSKAL(G):
# A = ∅
# foreach v ∈ G.V:
#    MAKE-SET(v)
# foreach (u, v) in G.E ordered by weight(u, v), increasing:
#    if FIND-SET(u) ≠ FIND-SET(v):
#       A = A ∪ {(u, v)}
#       UNION(u, v)
# return A

class Matrix:

    def __init__(self, roads, num_cities, machines):
        self.roads = roads
        self.num_cities = num_cities
        self.machines = machines

    def min_time(self):
        """
        Return an integer representing the minimum time required to disrupt the
        connections among all machines.
        """
        pass



if __name__ == '__main__':
    num_cities, num_machines = map(int, input().split())

    roads = []
    for _ in range(num_cities - 1):
        roads.append(tuple(map(int, input().rstrip().split())))

    machines = [] # these are cities machines are in
    for _ in range(num_machines):
        machines.append(int(input()))

    matrix = Matrix(roads, num_cities, machines)
    print(matrix.min_time())
