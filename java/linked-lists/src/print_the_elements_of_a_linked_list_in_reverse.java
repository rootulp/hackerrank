/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/
    // This is a "method-only" submission.
    // You only need to complete this method.

void ReversePrint(Node head) {

  // Base case
  if (head == null) {
    return;
  }

  // Recursively call Reverse Print on next node
  ReversePrint(head.next);

  // Print contents
  System.out.println(head.data);

}
