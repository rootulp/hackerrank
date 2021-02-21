import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    private static final String DELETE = "Delete";
    private static final String INSERT = "Insert";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sizeOfList = scanner.nextInt();
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < sizeOfList; i++) {
            list.add(scanner.nextInt());
        }

        int numberOfQueries = scanner.nextInt();
        for (int i = 0; i < numberOfQueries; i++) {
            String operation = scanner.next().trim();
            scanner.nextLine();
            String input = scanner.nextLine().trim();
            executeQuery(list, operation, input);
        }

        System.out.println(String.join(" ", list.stream()
                                            .map(s -> String.valueOf(s))
                                            .collect(Collectors.toList())));
        scanner.close();
    }

    public static void executeQuery(List<Integer> list, String operation, String input) {
        if (operation.equals(DELETE)) {
            list.remove(Integer.parseInt(input));
        } else if (operation.equals(INSERT)) {
            String[] splitString = input.split(" ");
            int index = Integer.parseInt(splitString[0]);
            int value = Integer.parseInt(splitString[1]);
            if (index > list.size()) {
                list.add(value);
            } else {
                list.add(index, value);
            }
        } else {
            throw new Error(String.format("Unsupported operation %s", operation));
        }
    }
}
