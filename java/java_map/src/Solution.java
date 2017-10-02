import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {
    Map<String, Integer> contacts = new HashMap<String, Integer>();
    Scanner sc = new Scanner(System.in);

    int n = Integer.parseInt(sc.nextLine()); // number of contacts

    for (int i = 0; i < n; i ++) {
      String name = sc.nextLine();
      Integer number = Integer.parseInt(sc.nextLine());
      contacts.put(name, number);
    }

    while (sc.hasNext()) {
      String query = sc.nextLine();
      if (contacts.containsKey(query)) {
        System.out.println(query + "=" + contacts.get(query));
      } else {
        System.out.println("Not found");
      }
    }
  }

}
