
#!/bin/python3

import math
import os
import random
import re
import sys

# Note the name of the file is based on this URL:
# https://www.hackerrank.com/challenges/torque-and-development/problem
# The problem name is "Roads and Libraries"

class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacencey_list = [[] for i in range(num_vertices)]

    def add_edge(self, source, destination):
        if destination not in self.adjacencey_list[source]:
            self.adjacencey_list[source].append(destination)
        if source not in self.adjacencey_list[destination]:
            self.adjacencey_list[destination].append(source)

    def __str__(self):
        return "Graph num vertices: {}, with adjacencey list {}".format(self.num_vertices, self.adjacencey_list)



def roadsAndLibraries(num_cities, cost_lib, cost_road, obstructed_roads):
    if cost_lib <= cost_road:
        # It is cheaper to build a library than it is to build a road.
        # Therefore build a library in every city and do not build any roads.
        return cost_lib * num_cities
    else:
        graph = Graph(num_cities)
        for obstructed_road in obstructed_roads:
            # Obstructed roads are one-indexed.
            graph.add_edge(obstructed_road[0] - 1, obstructed_road[1] - 1)
            print(graph)


        return ((cost_lib * num_forests(num_cities, obstructed_roads)) +
               (cost_road * num_roads_to_build(num_cities, obstructed_roads)))


def num_forests(num_cities, obstructed_roads):
    # Return the number of disjoint unions of trees in a graph
    return 0

def num_roads_to_build(num_cities, obstructed_roads):
    # Return the minimum number of roads to build to connect all trees in the graph
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_queries = int(input())
    for _query in range(num_queries):
        num_cities, num_roads, cost_lib, cost_road = list(map(int, input().split()))
        obstructed_roads = []

        for _obstructed_road in range(num_roads):
            obstructed_roads.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(num_cities, cost_lib, cost_road, obstructed_roads)
        fptr.write(str(result) + '\n')
    fptr.close()
