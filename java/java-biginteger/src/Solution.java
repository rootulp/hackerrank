import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    BigInteger a = new BigInteger(sc.next(), 10);
    BigInteger b = new BigInteger(sc.next(), 10);

    System.out.println(a.add(b));
    System.out.println(a.multiply(b));
  }
}
