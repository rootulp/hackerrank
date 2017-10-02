/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/

int GetNode(Node head,int n) {

    // Create runner and curr nodes
    Node runner = head;
    Node curr = head;

    // Move runner node n spaces ahead of curr
    for (int i = 0; i < n; i++){ runner = runner.next; }

    // Increment both until runner reaches end of list
    while(runner.next != null){
        runner = runner.next;
        curr = curr.next;
    }

    // Return curr's data
    return curr.data;

}
