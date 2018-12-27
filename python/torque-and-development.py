
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

class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacencey_list = defaultdict(list)

    def add_edge(self, source, destination):
        if destination not in self.adjacencey_list[source]:
            self.adjacencey_list[source].append(destination)
        if source not in self.adjacencey_list[destination]:
            self.adjacencey_list[destination].append(source)



    def get_connected_components(self):
        num_nodes_in_connected_components = []
        visited = [False] * self.num_vertices

        # Repeat until we have visited all nodes
        while False in visited:
            next_node_to_visit = visited.index(False)

            component = self.get_connected_component(next_node_to_visit)
            num_nodes_in_connected_component = component.count(True)
            num_nodes_in_connected_components.append(num_nodes_in_connected_component)

            for node, visitedInComponent in enumerate(component):
                if not visited[node] and visitedInComponent:
                    visited[node] = True

        # print ("num_nodes_in_connected_components {}", num_nodes_in_connected_components)
        return num_nodes_in_connected_components


    def get_connected_component(self, node):
        # Traverse all nodes connected to node.
        # Return a list of the connected nodes.

        # Mark all the vertices as unvisited
        visited = [False] * self.num_vertices

        # Call the recursive function dfs to traverse
        self.dfs(node, visited)

        # Return the number of visited nodes
        return visited

    def dfs(self, node, visited):
        # Visit the current node
        visited[node] = True
        print("Visited node: {}".format(node))

        # Recursively visit all the vertices adjacent to this vertex
        for neighbor in self.adjacencey_list[node]:
            print("Neighbor of node: {}, neighbor {}, visited {}".format(node, neighbor, visited))
            if visited[neighbor] == False:
                self.dfs(neighbor, visited)


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
            # print(graph)

        connected_components = graph.get_connected_components()

        # Put 1 library in each component, and the total per component cost is
        # simply ct-1 (a road to connect to each node in the compomnent) * cost of a
        # road + cost of one library.
        total_cost = 0
        for num_nodes_in_connected_component in connected_components:
            cost_to_connect_all_nodes = cost_road * num_nodes_in_connected_component - 1
            cost_for_component = cost_to_connect_all_nodes + cost_lib
            total_cost += cost_for_component

        return total_cost



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
