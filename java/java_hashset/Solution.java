import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {

    HashSet<String> pairs = new HashSet<String>();
    Scanner sc = new Scanner(System.in);

    int n = Integer.parseInt(sc.nextLine()); // number of pairs

    for (int i = 0; i < n; i ++) {
      String pair = sc.nextLine();
      pairs.add(pair);
      System.out.println(pairs.size());
    }
  }
}
