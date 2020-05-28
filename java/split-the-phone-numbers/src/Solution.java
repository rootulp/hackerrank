import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String trash = sc.nextLine();

    for (int i = 0; i < n; i++) {
      String phoneNumber = sc.nextLine();
      Pattern phonePattern = Pattern.compile("([0-9]{1,3})[-\\s]([0-9]{1,3})[-\\s]([0-9]{4,10})");
      Matcher m = phonePattern.matcher(phoneNumber);
      if (m.matches()) {
        String countryCode = m.group(1);
        String localAreaCode = m.group(2);
        String number = m.group(3);
        System.out.println(
            "CountryCode=" + countryCode + ",LocalAreaCode=" + localAreaCode + ",Number=" + number);
      }
    }
  }
}
