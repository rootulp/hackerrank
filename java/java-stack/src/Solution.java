import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

  private static final Map<Character, Character> validChars = populateValidChars();

  private static Map<Character, Character> populateValidChars() {
    Map<Character, Character> map = new HashMap<Character, Character>();
    map.put('[', ']');
    map.put('{', '}');
    map.put('(', ')');
    return map;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNext()) {
      String str = sc.next();
      System.out.println(valid(str));
    }
  }

  public static boolean valid(String str) {
    Stack<Character> stack = new Stack<Character>();

    for (int i = 0; i < str.length(); i++) {
      char c = str.charAt(i);

      if (validChars.containsKey(c)) { // opening paren
        stack.push(c);
      } else if (validChars.containsValue(c) && !stack.empty()) { // closing paren
        char closingParen = validChars.get(stack.pop());
        if (c != closingParen) {
          return false;
        }
      } else { // invalid character
        return false;
      }
    }

    return stack.empty();
  }
}
