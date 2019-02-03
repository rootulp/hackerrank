#!/bin/python3

import math
import os
import random
import re
import sys


class Node:
    pass

class Graph:
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_nodes, num_edges = map(int, input().split())
    edges = []

    for i in range(num_edges):
        edge = list(map(int, input().split()))
        edges.append(edge)

    color_ids = list(map(int, input().rstrip().split()))
    color_to_find = int(input())

    graph = Graph(num_nodes, num_edges, edges, color_ids)
    result = graph.smallest_path_length(color_to_find)

    fptr.write(str(result) + '\n')
    fptr.close()
