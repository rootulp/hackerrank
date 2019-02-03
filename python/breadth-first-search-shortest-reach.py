#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

class Node:

    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor_id):
        self.neighbors.append(neighbor_id)

    def __repr__(self):
        return "Node ID: {}, Neighbors: {}".format(self.node_id, self.neighbors)

class Graph:

    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.nodes = []

        for node_id in range(num_nodes):
            self.nodes.append(Node(node_id + 1))

        for node_a, node_b in edges:
            self.nodes[node_a - 1].add_neighbor(node_b)
            self.nodes[node_b - 1].add_neighbor(node_a)

    def shortest_reach(self, starting_node):
        self.mark_all_nodes_unvisited()
        shortest_reach_to_nodes = [-1 for i in range(self.num_nodes)]

        nodes_to_visit = deque()
        nodes_to_visit.append((self.nodes[starting_node - 1], 0))
        while nodes_to_visit:
            current_node, depth = nodes_to_visit.popleft()
            current_node.visited = True
            shortest_reach_to_nodes[current_node.node_id - 1] = 6 * depth
            for node_id in current_node.neighbors:
                node = self.nodes[node_id - 1]
                if node.visited == False:
                    nodes_to_visit.append((node, depth + 1))

        del shortest_reach_to_nodes[starting_node - 1] # remove the starting node
        return shortest_reach_to_nodes


    def mark_all_nodes_unvisited(self):
        for node in self.nodes:
            node.visited = False


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for _ in range(q):
        num_nodes, num_edges = list(map(int, input().split()))
        edges = []
        for _ in range(num_edges):
            edges.append(list(map(int, input().rstrip().split())))

        starting_node = int(input())

        graph = Graph(num_nodes, edges)
        # print(graph.nodes)
        shortest_reach = graph.shortest_reach(starting_node)

        fptr.write(' '.join(map(str, shortest_reach)))
        fptr.write('\n')

    fptr.close()
