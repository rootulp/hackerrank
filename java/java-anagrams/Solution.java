import java.util.Scanner;

public class Solution {

    private static boolean isAnagram(String a, String b) {
        return countOfCharacters(a.toLowerCase()).equals(countOfCharacters(b.toLowerCase()));
    }

    // HACKHACK
    // HackerRank is preventing me from modifying the template solution that
    // only imports import java.util.Scanner. If this limitation were removed,
    // use `Map` and `HashMap` below and extract imports to the top of the file.
    private static java.util.Map<Character, Integer> countOfCharacters(String word) {
        java.util.Map<Character, Integer> counts = new java.util.HashMap<>();
        for(char c : word.toCharArray()) {
            counts.put(c, 1 + counts.getOrDefault(c, 0));
        }
        return counts;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
