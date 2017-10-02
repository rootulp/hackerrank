import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int t = in.nextInt();
    for (int i = 0; i < t; i++) {
      try {
        long num = in.nextLong();
        System.out.println(num + " can be fitted in:");
        printValidDatatypes(num);
      } catch (Exception e) {
        String invalid = in.next();
        System.out.println(invalid + " can't be fitted anywhere.");
      }
    }
  }

  public static void printValidDatatypes(long num) {
    if (num >= -Math.pow(2, 7) && num < Math.pow(2, 7)) {
      System.out.println("* byte");
    }
    if (num >= -Math.pow(2, 15) && num < Math.pow(2, 15)) {
      System.out.println("* short");
    }
    if (num >= -Math.pow(2, 31) && num < Math.pow(2, 31)) {
      System.out.println("* int");
    }
    if (num >= -Math.pow(2, 63) && num < Math.pow(2, 63)) {
      System.out.println("* long");
    }
  }
}
