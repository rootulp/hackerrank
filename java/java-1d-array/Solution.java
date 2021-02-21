import java.util.*;

public class Solution {

    public static boolean canWin(int leap, int[] array, int currentLocation) {
      if (currentLocation >= array.length) {
        return true;
      }
      if (currentLocation < 0 || array[currentLocation] == 1) {
        return false;
      }

      // mark current location as visited
      array[currentLocation] = 1;
      return canWin(leap, array, currentLocation - 1) ||
             canWin(leap, array, currentLocation + 1) ||
             canWin(leap, array, currentLocation + leap);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();

            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println(canWin(leap, game, 0) ? "YES" : "NO");
        }
        scan.close();
    }
}
