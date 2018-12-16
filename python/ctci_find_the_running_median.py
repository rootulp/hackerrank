#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop

class MinHeap:
    """A lightweight wrapper around Pythons Min heap implementation."""

    def __init__(self):
        self.store = []

    def heap_push(self, value):
        heappush(self.store, value)
        print("Store is now: " + str(self.store))


    def heap_pop(self):
        return heappop(self.store)
        print("Store is now: " + str(self.store))

class MaxHeap:

    def __init__(self):
        self.store = []

    def heap_push(self, value):
        """Add value to the heap while maintaining the max heap property."""
        self.store.append(value)
        value_idx = len(self.store) - 1
        self.sift_up(self.get_parent_idx(value_idx), value_idx)
        print("Store is now: " + str(self.store))


    def heap_pop(self):
        """Pop the value off the top of the heap while maintaining the heap property."""
        self.swap(0, len(self.store) - 1)
        result = self.store.pop()
        self.sift_down(0)
        print("Store is now: " + str(self.store))
        return result

    def sift_up(self, parent_idx, child_idx):
        """Compare the values at parent_idx and child_idx
           If they are in the incorrect order, swap them and sift up with the new parent.
           If they are in the correct order then stop sifting up.
        """
        if (self.store[child_idx] > self.store[parent_idx]):
            print("Swapping {} and {}".format(child_idx, parent_idx))
            self.swap(child_idx, parent_idx)
            return self.sift_up(self.get_parent_idx(parent_idx), parent_idx)

    def sift_down(self, idx):
        """Sift down the value at position idx.
           Compare value with it's larger child.
           If the child is larger than value, swap them.
           Repeat with swapped idx.
        """
        larger_child_idx = self.get_larger_child_idx(idx)
        if (larger_child_idx is None):
            return

        if(self.store[idx] < self.store[larger_child_idx]):
            print("Swapping {} and {}".format(self.store[idx], self.store[larger_child_idx]))
            self.swap(idx, larger_child_idx)
            return self.sift_down(larger_child_idx)

    def get_larger_child_idx(self, idx):
        """Gets the larger child for value at idx"""
        left_child_idx = self.get_left_child_idx(idx)
        right_child_idx = self.get_right_child_idx(idx)

        if(left_child_idx is None):
            return None
        elif(right_child_idx is None):
            return left_child_idx
        else:
            left_child = self.store[left_child_idx]
            right_child = self.store[right_child_idx]
            return left_child_idx if left_child > right_child else right_child_idx


    def get_left_child_idx(self, idx):
        """Returns the left child index for value if it exists.
           Returns None if the value at idx does not have a left child.
        """
        left_child_idx = 2 * idx + 1
        if(left_child_idx >= self.size()):
            return None
        return left_child_idx

    def get_right_child_idx(self, idx):
        """Returns the right child index for value if it exists.
           Returns None if the value at idx does not have a right child.
        """
        right_child_idx = 2 * idx + 2
        if(right_child_idx >= self.size()):
            return None
        return right_child_idx

    def get_parent_idx(self, idx):
        """Return the parent index for node at idx."""
        return idx // 2

    def swap(self, idx_1, idx_2):
        """Swap the values at position idx_1 and idx_2."""
        self.store[idx_1], self.store[idx_2] = self.store[idx_2], self.store[idx_1]

    def size(self):
        """Returns the current heap size."""
        return len(self.store)

    def peek(self):
        """Returns the value at the top of the heap"""
        return self.store[0]


class RunningMedian:

    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def push(self, value):
        return self.min_heap.heap_push(value)

    def get_median(self):
        """Returns the current median."""
        return 0

    def test_pops(self):
        while self.max_heap.size() > 0:
            popped_val = self.max_heap.heap_pop()
            print("Popped value: {}".format(popped_val))


if __name__ == '__main__':
    running_median = RunningMedian();

    n = int(input())
    for _ in range(n):
        running_median.push(int(input()))
        # print(running_median.get_median())

