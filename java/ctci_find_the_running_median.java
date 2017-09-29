import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class MedianHeap {

  public PriorityQueue<Integer> minHeap;
  public PriorityQueue<Integer> maxHeap;

  public MedianHeap(int capacity) {
    this.minHeap = new PriorityQueue(capacity);
    this.maxHeap = new PriorityQueue(capacity, Collections.reverseOrder());
  }

  public void add(int num) {
    if (isEmpty() || num > median()) {
      this.minHeap.add(num);
    } else {
      this.maxHeap.add(num);
    }
    rebalanceHeaps();
  }

  public double median() {
    if (minHeap.size() > maxHeap.size()) {
      return minHeap.peek();
    } else if (minHeap.size() < maxHeap.size()) {
      return maxHeap.peek();
    } else {
      return ((minHeap.peek() + maxHeap.peek()) / 2.0);
    }
  }

  private boolean isEmpty() {
    return (minHeap.size() == 0 && maxHeap.size() == 0);
  }

  private void rebalanceHeaps() {
    if (minHeap.size() - maxHeap.size() > 1) {
      maxHeap.add(minHeap.poll());
    }
    if (maxHeap.size() - minHeap.size() > 1) {
      minHeap.add(maxHeap.poll());
    }
  }
}

public class Solution {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int capacity = in.nextInt();
    int[] list = new int[capacity];
    MedianHeap medianHeap = new MedianHeap(capacity);

    for (int i = 0; i < capacity; i++) {
      list[i] = in.nextInt();
      medianHeap.add(list[i]);
      System.out.printf("%.1f\n", medianHeap.median());
    }
  }
}
