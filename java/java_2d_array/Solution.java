import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int[][] matrix = new int[6][6]; // hardcoded dimensions

    for (int i = 0; i < 6; i++) { // hardcoded
      for (int j = 0; j < 6; j++) { // hardcoded
        matrix[i][j] = sc.nextInt();
      }
    }

    int max = -64; // (-9 * 7) -1

    for (int i = 1; i < 5; i++) {
      for (int j = 1; j < 5; j++) {
        int curr =
            matrix[i][j]
                + matrix[i - 1][j - 1]
                + matrix[i - 1][j]
                + matrix[i - 1][j + 1]
                + matrix[i + 1][j - 1]
                + matrix[i + 1][j]
                + matrix[i + 1][j + 1];
        if (curr > max) {
          max = curr;
        }
      }
    } // fix up hardcoded hourglass shape indexes

    System.out.println(max);
  }
}
