import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    String str = sc.next();
    int k = sc.nextInt(); // substring length

    String max = str.substring(0, k);
    String min = str.substring(0, k);

    for (int i = 0; i <= str.length() - k; i++){
      if (max.compareTo(str.substring(i, i+k)) < 0) { max = str.substring(i, i+k);}
      if (min.compareTo(str.substring(i, i+k)) > 0) { min = str.substring(i, i+k);}
    }

    System.out.println(min);
    System.out.println(max);
  }
}
