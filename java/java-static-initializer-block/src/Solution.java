import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {
  private static boolean flag;
  private static int B;
  private static int H;

  static {

    // Note: this is a poor example of using static initialization blocks.
    // This exercise was very poorly written.
    Scanner sc = new Scanner(System.in);
    B = Integer.parseInt(sc.nextLine());
    H = Integer.parseInt(sc.nextLine());

    if (B <= 0 || H <= 0) {
      flag = false;
      // Note: this is a bad practice. This exercise is poorly written. Instead this should throw an
      // error.
      System.out.println("java.lang.Exception: Breadth and height must be positive");
    } else {
      flag = true;
    }
  }

  public static void main(String[] args) {
    if (flag) {
      int area = B * H;
      System.out.print(area);
    }
  } // end of main
} // end of class
