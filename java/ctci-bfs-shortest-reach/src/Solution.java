import java.io.*;
import java.util.*;

public class Solution {

  private int nodes;
  private int edges;
  private List<Set<Integer>> adjacencyLists;

  public Solution(int nodes, int edges) {
    this.nodes = nodes;
    this.edges = edges;
    this.adjacencyLists = new ArrayList<Set<Integer>>();
    for (int i = 0; i < nodes; i++) {
      adjacencyLists.add(i, new HashSet<Integer>());
    }
  }

  public void addEdge(int nodeA, int nodeB) {
    this.adjacencyLists.get(nodeA).add(nodeB);
    this.adjacencyLists.get(nodeB).add(nodeA);
  }

  public String distancesFrom(int startNode) {
    Map<Integer, Integer> visited = breadthFirstSearch(startNode);
    List<Integer> distancesFrom = new ArrayList<Integer>();
    for (int i = 0; i < this.nodes; i++) {
      if (i != startNode) {
        distancesFrom.add(visited.getOrDefault(i, -1));
      }
    }
    return spaceDelimit(distancesFrom);
  }

  public String spaceDelimit(List<Integer> list) {
    StringJoiner joiner = new StringJoiner(" ");
    for (Integer i : list) {
      joiner.add(i.toString());
    }
    return joiner.toString();
  }

  private Map<Integer, Integer> breadthFirstSearch(int startNode) {
    Map<Integer, Integer> visited = new HashMap<Integer, Integer>();
    Queue<Integer> nodesToVisit = new LinkedList<Integer>();
    Queue<Integer> nodesToVisitDepth = new LinkedList<Integer>();

    nodesToVisit.add(startNode);
    nodesToVisitDepth.add(0);

    while (nodesToVisit.size() != 0) {
      int currentNode = nodesToVisit.poll();
      int currentDepth = nodesToVisitDepth.poll();
      for (int neighbor : this.adjacencyLists.get(currentNode)) {
        if (!visited.containsKey(neighbor)) {
          nodesToVisit.add(neighbor);
          nodesToVisitDepth.add(currentDepth + 6);
        }
      }
      if (!visited.containsKey(currentNode) || visited.get(currentNode) > currentDepth) {
        visited.put(currentNode, currentDepth);
      }
    }
    return visited;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int queries = in.nextInt();
    for (int query = 0; query < queries; query++) {
      int nodes = in.nextInt();
      int edges = in.nextInt();
      Solution graph = new Solution(nodes, edges);
      for (int edge = 0; edge < edges; edge++) {
        int nodeA = in.nextInt();
        int nodeB = in.nextInt();
        graph.addEdge(nodeA - 1, nodeB - 1);
      }
      int startNode = in.nextInt();
      System.out.println(graph.distancesFrom(startNode - 1));
    }
  }
}
