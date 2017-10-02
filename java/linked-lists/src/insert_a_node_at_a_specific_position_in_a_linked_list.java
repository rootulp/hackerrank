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

Node InsertNth(Node head, int data, int position) {

    // Create new node
    Node temp = new Node();
    temp.data = data;

    // Insert at head
    if (position == 0) {
      temp.next = head;
      return temp;
    }

    // Iterate through list to find node prior to insert point
    Node curr = head;
    for (int i = 0; i < position - 1; i++){
        curr = curr.next;
    }

    // Insert node
    temp.next = curr.next;
    curr.next = temp;

    return head;
}
