import java.util.*;

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
        System.out.println("Foo");
        // Regex
        // <([\w\d\s]+)>([\w\d\s]+)(<\/\1>)
    }
}
