import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        sc.close();

        System.out.println(isPalindrome(word) ? "Yes" : "No");

    }

    private static boolean isPalindrome(String word) {
        return word.equals(reverse(word));
    }

    // Copied from
    // https://www.baeldung.com/java-reverse-string
    private static String reverse(String word) {
       if (word == null) {
           return word;
       }

       String output = "";

       for (int i = word.length() - 1; i >= 0; i--) {
           output = output + word.charAt(i);
       }

       return output;
    }
}
