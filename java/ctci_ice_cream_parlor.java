import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int trips = in.nextInt();
    for (int trip_i = 0; trip_i < trips; trip_i++) {
      int money = in.nextInt();
      int flavors = in.nextInt();
      int costs[] = new int[flavors];
      for (int cost_i = 0; cost_i < flavors; cost_i++) {
        costs[cost_i] = in.nextInt();
      }
      for (int i = 0; i < flavors - 1; i++) {
        for (int j = i + 1; j < flavors; j++) {
          if (costs[i] + costs[j] == money) {
            System.out.print(i + 1);
            System.out.print(" ");
            System.out.println(j + 1);
            break;
          }
        }
      }
    }
  }
}
