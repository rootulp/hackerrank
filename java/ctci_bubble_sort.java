import java.io.*;
import java.util.*;

class BubbleSort {

    public int[] array;
    public int swaps;

    public BubbleSort(int[] array) {
        this.array = array;
        this.swaps = 0;
    }

    public void sort() {
        int traversalSwaps = 0;
        do {
            traversalSwaps = 0;
            for (int i = 0; i < array.length - 1; i++) {
                if (array[i] > array[i + 1]) {
                    swap(i, i + 1);
                    traversalSwaps++;
                }
            }
        } while (traversalSwaps > 0);
    }
    
    private void swap(int index1, int index2) {
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
        swaps++;
    }
}

public class Solution {    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] array = new int[n]; 
        for(int i = 0; i < n; i++) {
            array[i] = in.nextInt();
        }

        BubbleSort bubbleSort = new BubbleSort(array);
        bubbleSort.sort();
        System.out.println("Array is sorted in " + bubbleSort.swaps + " swaps.");
        System.out.println("First Element: " + bubbleSort.array[0]);
        System.out.println("Last Element: " + bubbleSort.array[array.length - 1]);
    }
}