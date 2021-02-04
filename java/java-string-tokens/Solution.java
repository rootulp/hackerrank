import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        if(!scan.hasNext()) {
            System.out.print(0);
            scan.close();
            return;
        }

        String sentence = scan.nextLine().trim();
        scan.close();

        String delimeters = "[ !,?._'@]+";
        String[] tokens = sentence.split(delimeters);
        System.out.println(tokens.length);
        for (String token: tokens) {
            System.out.println(token);
        }
    }
}
