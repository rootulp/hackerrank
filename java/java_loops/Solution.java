import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            solve(a, b, n);
        }
    }

    public static void solve(Integer a, Integer b, Integer n) {
        for (int n1 = 0; n1 < n; n1++) {
            int term = a;
            for (int n2 = 0; n2 <= n1; n2++) {
                term += b * Math.pow(2, n2);
            }
            System.out.print(term + " "); // Prints extra space at end of line
        }
        System.out.println();
    }
}
