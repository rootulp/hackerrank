import java.math.BigDecimal;
import java.util.*;

class Solution {
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] s = new String[n + 2];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next();
        }
        sc.close();

        //Write your code here
        Arrays.sort(s, Collections.reverseOrder(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1 != null && o2 != null) {
                    BigDecimal d1 = new BigDecimal(o1);
                    BigDecimal d2 = new BigDecimal(o2);
                    return d1.compareTo(d2);
                }
                return 0;
            }
        }));

        //Output
        for(int i = 0; i < n; i++)
        {
            System.out.println(s[i]);
        }
    }
}
