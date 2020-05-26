import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            System.out.println("================================");
            for(int i = 0; i < 3 ; i++) {
                String s1 = sc.next();
                int n = sc.nextInt();
                System.out.printf("%-15s%03d%n", s1, n);
            }
            System.out.println("================================");
    }
}

