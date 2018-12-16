#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop

class MinHeap:
    """A lightweight wrapper around Python's heap implementation."""

    def __init__(self):
        self.heap = []

    def push(self, value):
        heappush(self.heap, value)

    def pop(self):
        return heappop(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

# class MaxHeap:
#     """A lightweight wrapper around Python's heap implementation."""

#     def __init__(self):
#         self.heap = []

#     def push(self, value):
#         heappush(self.heap, -value)

#     def pop(self):
#         return -1.0 * heappop(self.heap)

#     def peek(self):
#         if not self.heap:
#             return None
#         return -1.0 * self.heap[0]

#     def __len__(self):
#         return len(self.heap)

#     def __str__(self):
#         return str(self.heap)

class MaxHeap:

    def __init__(self):
        self.heap = []

    def push(self, value):
        """Add value to the heap while maintaining the max heap property."""
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        """Pop the value off the top of the heap while maintaining the heap property."""
        self.swap(0, len(self.heap) - 1)
        result = self.heap.pop()
        self.sift_down(0)
        return result

    def sift_up(self, idx):
        """Recursively sift up the element at idx.
           Compare the value at idx with its parent
           If they are in the incorrect order, swap them and sift up with the new parent.
           If they are in the correct order then stop sifting up.
        """
        parent = self.get_parent(idx)

        if (parent is None):
            return

        if (self.heap[idx] > self.heap[parent]):
            self.swap(idx, parent)
            return self.sift_up(parent)

    def sift_down(self, idx):
        """Sift down the value at position idx.
           Compare value with it's larger child.
           If the child is larger than value, swap them.
           Repeat with swapped idx.
        """
        larger_child = self.get_larger_child(idx)
        if (larger_child is None):
            return

        if(self.heap[idx] < self.heap[larger_child]):
            self.swap(idx, larger_child)
            return self.sift_down(larger_child)

    def get_larger_child(self, idx):
        """Get the index for the larger child of idx"""
        left_child_idx = self.get_left_child(idx)
        right_child_idx = self.get_right_child(idx)

        if(left_child_idx is None):
            return None
        elif(right_child_idx is None):
            return left_child_idx
        else:
            left_child = self.heap[left_child_idx]
            right_child = self.heap[right_child_idx]
            return left_child_idx if left_child > right_child else right_child_idx


    def get_left_child(self, idx):
        """Returns the left child index for value if it exists.
           Returns None if the value at idx does not have a left child.
        """
        left_child_idx = 2 * idx + 1
        if(left_child_idx >= len(self.heap)):
            return None
        return left_child_idx

    def get_right_child(self, idx):
        """Returns the right child index for value if it exists.
           Returns None if the value at idx does not have a right child.
        """
        right_child_idx = 2 * idx + 2
        if(right_child_idx >= len(self.heap)):
            return None
        return right_child_idx

    def get_parent(self, idx):
        """Return the parent index for node at idx."""
        if(idx == 0):
            # Root of tree does not have a parent
            return None
        return (idx - 1) // 2

    def swap(self, a, b):
        """Swap the values at position a and b."""
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def peek(self):
        """Returns the value at the top of the heap."""
        if not self.heap:
            return None
        return self.heap[0]

    def __len__(self):
        """Returns the current heap length."""
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


class RunningMedian:

    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def push(self, value):
        self.min_heap.push(value)
        value = self.min_heap.pop()
        self.max_heap.push(value)
        value = self.max_heap.pop()

        if (len(self.min_heap) <= len(self.max_heap)):
            self.min_heap.push(value)
        else:
            self.max_heap.push(value)


    def get_median(self):
        """Returns the current median."""
        if (len(self.min_heap) == len(self.max_heap) == 0):
            return 0
        elif (len(self.min_heap) > len(self.max_heap)):
            return self.min_heap.peek()
        elif (len(self.min_heap) < len(self.max_heap)):
            return self.max_heap.peek()
        elif (len(self.min_heap) == len(self.max_heap)):
            return (self.min_heap.peek() + self.max_heap.peek()) / 2.0


if __name__ == '__main__':
    running_median = RunningMedian();

    n = int(input())
    for _ in range(n):
        running_median.push(int(input()))
        current_median = float(running_median.get_median())
        print("{:.1f}".format(current_median))
