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

Node Delete(Node head, int position) {

    // Delete head
    if (position == 0) {
      head = head.next;
      return head;
    }

    // Iterate through list to find node prior to insert point
    Node curr = head;
    for (int i = 0; i < position - 1; i++){
        curr = curr.next;
    }

    // Delete node
    curr.next = curr.next.next;

    return head;
}
