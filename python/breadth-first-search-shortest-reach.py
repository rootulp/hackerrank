#!/bin/python3

import math
import os
import random
import re
import sys


class Graph:
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for _ in range(q):
        num_nodes, num_edges = list(map(int, input().split()))
        edges = []
        for _ in range(num_edges):
            edges.append(list(map(int, input().rstrip().split())))

        starting_node = int(input())

        graph = Graph(num_nodes, num_edges)
        shortest_reach = graph.shortest_reach(starting_node)

        fptr.write(' '.join(map(str, shortest_reach)))
        fptr.write('\n')

    fptr.close()
