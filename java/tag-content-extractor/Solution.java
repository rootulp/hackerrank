import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int numberOfTestCases = Integer.parseInt(in.nextLine());
        for (int i = 0; i< numberOfTestCases; i++) {
			String line = in.nextLine();
            printContentEnclosedWithinTags(line);
		}
        in.close();
	}

    public static void printContentEnclosedWithinTags(String line) {
        Pattern pattern = Pattern.compile("<(.+)>([^<]+)</\\1>");
        Matcher matcher = pattern.matcher(line);
        boolean matchFound = false;

        while (matcher.find()) {
            System.out.println(matcher.group(2));
            matchFound = true;
        }

        if (!matchFound) {
            System.out.println("None");
        }
    }
}
