
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    print("n {}, c_lib {}, c_road {}, cities {}".format(n, c_lib, c_road, cities))
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_queries = int(input())

    for _query in range(num_queries):
        n, m, c_lib, c_road = list(map(int, input().split()))
        cities = []

        for _city in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        fptr.write(str(result) + '\n')
    fptr.close()
