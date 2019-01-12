
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Note the name of the file is based on this URL:
# https://www.hackerrank.com/challenges/torque-and-development/problem
# The problem name is "Roads and Libraries"


class DisjointSet:

    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0] * n
        self.merges = 0
        self.subgroups = n

    def find(self, node):
        if node != self.set[node]:
            # Path compression
            self.set[node] = self.find(self.set[node])
        return self.set[node]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        # Already in same group
        if x_root == y_root:
            return

        # Else merge groups
        self.merges += 1
        self.subgroups -= 1

        if self.rank[x_root] > self.rank[y_root]:
            self.set[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.set[x_root] = y_root
        else:
            self.set[y_root] = x_root
            self.rank[x_root] += 1

    def num_merges(self):
        return self.merges

    def num_subgroups(self):
        return self.subgroups - 1

    def __str__(self):
        return r"Set: {}\nRank: {}\Merges: {}\nSubgroups: {}".format(
            self.set, self.rank, self.merges, self.subgroups)


def roadsAndLibraries(num_cities, cost_lib, cost_road, roads):
    if cost_lib <= cost_road:
        # It is cheaper to build a library than it is to build a road.
        # Therefore build a library in every city and do not build any roads.
        return cost_lib * num_cities
    else:
        # Use the disjoint set data structure
        distjoint_set = DisjointSet(num_cities + 1)
        for source, destination in roads:
            distjoint_set.union(source, destination)

        return (cost_road * distjoint_set.num_merges()) + \
            (cost_lib * distjoint_set.num_subgroups())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_queries = int(input())
    for _query in range(num_queries):
        num_cities, num_roads, cost_lib, cost_road = list(
            map(int, input().split()))
        roads = []

        for _road in range(num_roads):
            roads.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(num_cities, cost_lib, cost_road, roads)
        fptr.write(str(result) + '\n')
    fptr.close()
