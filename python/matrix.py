#!/bin/python3

import math
import os
import random
import re
import sys

class Matrix:

    def __init__(self, roads, num_cities, machines):
        self.roads = roads
        self.num_cities = num_cities
        self.machines = machines
        self.time = 0

    def min_time(self):
        """
        Return an integer representing the minimum time required to disrupt the
        connections among all machines.
        """
        while self.any_machines_connected():
            machine1, machine2 = self.get_connected_machines()
            roads = self.get_roads_connecting(machine1, machine2)
            minimal_road = self.get_minimal_road(roads)
            self.remove_road(minimal_road)
            self.add_time(minimal_road)
        return self.time


    def any_machines_connected(self):
        for machine in self.machines:
            if self.is_connected_to_another_machine(machine):
                return True
        return False

    def is_connected_to_another_machine(self, machine):
        breadth_first_search



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    num_cities, num_machines = map(int, input().split())

    roads = []
    for _ in range(num_cities - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = [] # these are cities machines are in
    for _ in range(num_machines):
        machines.append(int(input()))

    matrix = Matrix(roads, num_cities, machines)
    result = matrix.min_time()

    fptr.write(str(result) + '\n')
    fptr.close()
