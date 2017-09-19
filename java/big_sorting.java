import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.math.BigInteger;

public class Solution {

    class StringComparator implements Comparator {
        public int compare(Object o1, Object o2) {
            String s1 = (String) o1;
            String s2 = (String) o2;
            if (s1.length() != s2.length()) {
                return s1.length() - s2.length();
            } else {
                BigInteger i1 = new BigInteger(s1);
                BigInteger i2 = new BigInteger(s2);
                return i1.compareTo(i2);
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] unsorted = new String[n];
        for(int unsorted_i=0; unsorted_i < n; unsorted_i++){
            unsorted[unsorted_i] = in.next();
        }
        List<String> list = Arrays.asList(unsorted);
        Collections.sort(list, new Solution().new StringComparator());
        for (String str : list) {
            System.out.println(str);
        }
    }
}
