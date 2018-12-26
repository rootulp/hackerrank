
#!/bin/python3

import math
import os
import random
import re
import sys

# Note the name of the file is based on this URL:
# https://www.hackerrank.com/challenges/torque-and-development/problem
# The problem name is "Roads and Libraries"


def roadsAndLibraries(num_cities, cost_lib, cost_road, obstructed_roads):
    # It is cheaper to build a library in each city than it is to build a road
    if cost_lib <= cost_road:
        return cost_lib * num_cities
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
