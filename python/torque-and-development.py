
#!/bin/python3

import math
import os
import random
import re
import sys

# Note the name of the file is based on this URL:
# https://www.hackerrank.com/challenges/torque-and-development/problem
# The problem name is "Roads and Libraries"


def roadsAndLibraries(num_cities, cost_lib, cost_road, roads):
    print("num_cities {}, c_lib {}, c_road {}, cities {}".format(num_cities, cost_lib, cost_road, roads))
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_queries = int(input())

    for _query in range(num_queries):
        num_cities, num_roads, cost_lib, cost_road = list(map(int, input().split()))
        roads = []

        for _road in range(num_roads):
            roads.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(num_cities, cost_lib, cost_road, roads)
        fptr.write(str(result) + '\n')
    fptr.close()
