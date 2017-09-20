import java.io.*;
import java.util.*;

public class Solution {

    private int nodes;
    private int edges;
    private LinkedList<Integer>[] adjacency_lists;


    public Solution(int nodes, int edges) {
        this.nodes = nodes;
        this.edges = edges;
        this.adjacency_lists = new LinkedList[nodes];
        for (int i = 0; i < nodes; i++) {
            adjacency_lists[i] = new LinkedList<Integer>();
        }
    }

    public void add_edge(int node_a, int node_b) {
        this.adjacency_lists[node_a].add(node_b);
        this.adjacency_lists[node_b].add(node_a);
    }

    public String distances_from(int start_node) {
        Map<Integer, Integer> visited = breadth_first_search(start_node);

        List<Integer> distances_from = new ArrayList<Integer>();
        for (int i = 0; i < this.nodes; i++) {
            if (i == start_node) {
                continue;
            } else if (visited.containsKey(i)) {
                distances_from.add(visited.get(i) * 6);
            } else {
                distances_from.add(-1);
            }
        }
        return space_delimit(distances_from);
    }

    public String space_delimit(List<Integer> list) {
        StringJoiner joiner = new StringJoiner(" ");
        for (Integer i : list) {
            joiner.add(i.toString());
        }
        return joiner.toString();
    }

    private Map<Integer, Integer> breadth_first_search(int startNode) {
        Map<Integer, Integer> visited = new HashMap();
        Queue<Integer> nodesToVisit = new LinkedList<Integer>();
        Queue<Integer> nodesToVisitDepth = new LinkedList<Integer>();

        nodesToVisit.add(startNode);
        nodesToVisitDepth.add(0);

        while (nodesToVisit.size() != 0) {
            int currentNode = nodesToVisit.poll();
            int currentDepth = nodesToVisitDepth.poll();
            for (int neighbor : this.adjacency_lists[currentNode]){
                if (!visited.containsKey(neighbor)) {
                    nodesToVisit.add(neighbor);
                    nodesToVisitDepth.add(currentDepth + 1);
                }
            }
            if (!visited.containsKey(currentNode) || visited.get(currentNode) > currentDepth) {
                //System.out.println("Putting: " + Integer.toString(currentNode) + " Depth: " + Integer.toString(currentDepth));
                visited.put(currentNode, currentDepth);
            }
        }
        //System.out.println(visited);
        return visited;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int queries = in.nextInt();
        for (int query_i = 0; query_i < queries; query_i++) {
            int nodes = in.nextInt();
            int edges = in.nextInt();
            Solution graph = new Solution(nodes, edges);
            for (int edge_i = 0; edge_i < edges; edge_i++) {
                int node_a = in.nextInt();
                int node_b = in.nextInt();
                graph.add_edge(node_a - 1, node_b - 1);
            }
            int start_node = in.nextInt();
            System.out.println(graph.distances_from(start_node - 1));
        }
    }
}

