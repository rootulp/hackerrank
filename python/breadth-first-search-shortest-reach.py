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
        self.marked_to_visit = False

    def add_neighbor(self, neighbor_id):
        self.neighbors.append(neighbor_id)

    def __repr__(self):
        return "Node ID: {}, Neighbors: {}, Marked to visit: {}".format(
            self.node_id, self.neighbors, self.marked_to_visit)


class Graph:

    EDGE_DISTANCE = 6

    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.nodes = []

        self.initialize_nodes()
        self.initialize_edges()

    def shortest_reach(self, starting_node):
        self.mark_all_nodes_unvisited()
        shortest_reach_to_nodes = [-1 for i in range(self.num_nodes)]

        nodes_to_visit = deque()
        nodes_to_visit.append((self.nodes[starting_node - 1], 0))
        self.nodes[starting_node - 1].marked_to_visit = True

        while nodes_to_visit:
            current_node, depth = nodes_to_visit.popleft()
            shortest_reach_to_nodes[current_node.node_id] = depth * \
                self.EDGE_DISTANCE
            for node_id in current_node.neighbors:
                node = self.nodes[node_id]
                if not node.marked_to_visit:
                    nodes_to_visit.append((node, depth + 1))
                    node.marked_to_visit = True

        # remove the starting node
        del shortest_reach_to_nodes[starting_node - 1]
        return shortest_reach_to_nodes

    def initialize_nodes(self):
        for node_id in range(self.num_nodes):
            self.add_node(node_id)

    def initialize_edges(self):
        for edge in edges:
            node_a, node_b = edge
            self.add_edge(node_a - 1, node_b - 1)

    def add_node(self, node_id):
        self.nodes.append(Node(node_id))

    def add_edge(self, node_a, node_b):
        self.nodes[node_a].add_neighbor(node_b)
        self.nodes[node_b].add_neighbor(node_a)

    def mark_all_nodes_unvisited(self):
        for node in self.nodes:
            node.marked_to_visit = False


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
        shortest_reach = graph.shortest_reach(starting_node)

        fptr.write(' '.join(map(str, shortest_reach)))
        fptr.write('\n')

    fptr.close()
