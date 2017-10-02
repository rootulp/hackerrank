/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
     Node prev;
  }
*/

Node Reverse(Node head) {

    // Check for empty list
    if (head == null) { return head; }

    // Check if we reached tail
    if (head.next == null) {
        head.next = head.prev;
        head.prev = null;
        return head;
    }

    // Swap next and prev pointers
    Node temp = head.prev;
    head.prev = head.next;
    head.next = temp;

    // Call reverse on next node in list
    return Reverse(head.prev);

}
