import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int size = sc.nextInt();
    int[] arr = new int[size];
    for (int i = 0; i < size; i++) {
      arr[i] = sc.nextInt();
    }

    int count = 0;
    for (int i = 0; i < size; i++) {
      int sum = 0;
      for (int j = i; j < size; j++) {
        sum += arr[j];
        if (sum < 0) {
          count++;
        }
      }
    }
    System.out.println(count);
  }
}
