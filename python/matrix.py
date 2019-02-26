#!/bin/python3

import math
import os
import random
import re
import sys

# Let's use an adapted form of Kruskal.
# 1. Construct a set for each city.
# 2. Iterate through edges in descending order of "cost to destroy".
# 3. If the edge connects two machines, we must destroy it so add to total time.
#    If the edge does not connect two machines, we do not need to destroy it.
# 4. After iterating through all edges, return total time

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


class Matrix:

    MACHINE = "MACHINE"

    def __init__(self, roads, num_cities, machines):
        self.roads = roads
        self.num_cities = num_cities
        self.machines = machines

        self.sets = [[city] for city in range(num_cities)]
        self.set_member_lookup = {city: city for city in range(num_cities)}

        self.mark_cities_with_machines(machines)

    def mark_cities_with_machines(self, machines):
        for machine in machines:
            city_with_machine = self.get_set_for_city(machine)
            city_with_machine.append(self.MACHINE)

    def get_set_for_city(self, city):
        return self.sets[self.find_set(city)]

    def find_set(self, city):
        return self.set_member_lookup[city]

    def build_road(self, city_a, city_b):
        set_a = self.get_set_for_city(city_a)
        set_b = self.get_set_for_city(city_b)

        if set_a is not None and set_b is not None:
            set_a.extend(set_b)
            set_a_lookup = self.find_set(city_a)
            for city in set_b:
                self.set_member_lookup[city] = set_a_lookup
            set_b = None

    def min_time(self):
        """
        Return an integer representing the minimum time required to disrupt the
        connections among all machines.
        """
        total_time = 0
        descending_roads = list(
            reversed(
                sorted(
                    self.roads,
                    key=lambda tuple: tuple[2])))
        for road in descending_roads:
            city_a, city_b, time_to_destroy = road
            set_a = self.get_set_for_city(city_a)
            set_b = self.get_set_for_city(city_b)
            if self.MACHINE in set_a and self.MACHINE in set_b:
                total_time += time_to_destroy
            else:
                self.build_road(city_a, city_b)
        return total_time


if __name__ == '__main__':
    num_cities, num_machines = map(int, input().split())

    roads = []
    for _ in range(num_cities - 1):
        roads.append(tuple(map(int, input().rstrip().split())))

    machines = []  # these are cities machines are in
    for _ in range(num_machines):
        machines.append(int(input()))

    matrix = Matrix(roads, num_cities, machines)
    print(matrix.min_time())
