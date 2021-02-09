import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<List<Integer>> numbers = getNumbersFromInput(scanner);

        // It may be more appropriate to store queries as a tuple
        List<List<Integer>> queries = getQueriesFromInput(scanner);

        executeQueries(numbers, queries);
    }

    private static void executeQueries(List<List<Integer>> numbers, List<List<Integer>> queries) {
        for (List<Integer> query : queries) {
            Integer x = query.get(0);
            Integer y = query.get(1);

            try {
                System.out.println(numbers.get(x - 1).get(y - 1));
            } catch (IndexOutOfBoundsException e){
                System.out.println("ERROR!");
            }
        }
    }

    private static List<List<Integer>> getNumbersFromInput(Scanner scanner) {
        Integer numberOfLines = scanner.nextInt();
        List<List<Integer>> lines = new ArrayList<>();

        for (int i = 0; i < numberOfLines; i++) {
            Integer numberOfElements = scanner.nextInt();
            List<Integer> numbers = new ArrayList<Integer>();
            for (int j = 0; j < numberOfElements; j++) {
                numbers.add(scanner.nextInt());
            }
            lines.add(numbers);
        }

        return lines;
    }

    private static List<List<Integer>> getQueriesFromInput(Scanner scanner) {
        Integer numberOfQueries = scanner.nextInt();
        List<List<Integer>> queries = new ArrayList<>();

        for (int i = 0; i < numberOfQueries; i++) {
            List<Integer> query = new ArrayList<Integer>();
            query.add(scanner.nextInt());
            query.add(scanner.nextInt());
            queries.add(query);
        }

        return queries;
    }
}
