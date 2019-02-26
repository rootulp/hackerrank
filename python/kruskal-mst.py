#!/bin/python3

import math
import os
import random
import re
import sys

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


class Kruskal:

    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.sets = []
        self.initialize_sets()

    def initialize_sets(self):
        for node in range(self.num_nodes):
            self.sets.append(set([node + 1]))

    def find_set(self, node):
        for subset in self.sets:
            if node in subset:
                return subset

    def union(self, set_a, set_b):
        self.sets.remove(set_a)
        self.sets.remove(set_b)
        self.sets.append(set_a.union(set_b))

    def weight_of_minimum_spanning_tree(self):
        """
        Returns an integer denoting the total weight of the Really Special SubTree.
        """
        total_weight = 0
        edges_ascending = sorted(edges, key=lambda tup: tup[2])
        for edge in edges_ascending:
            node_a, node_b, weight = edge  # unpack tuple
            set_a = self.find_set(node_a)
            set_b = self.find_set(node_b)
            if set_a != set_b:
                total_weight += weight
                self.union(set_a, set_b)
        return total_weight


if __name__ == '__main__':
    num_nodes, num_edges = map(int, input().rstrip().split())

    edges = []
    for i in range(num_edges):
        edges.append(tuple(map(int, input().rstrip().split())))

    kruskal = Kruskal(num_nodes, edges)
    print(str(kruskal.weight_of_minimum_spanning_tree()))
