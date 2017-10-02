/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/
Node Insert(Node head,int x) {

  // Create new node
  Node temp = new Node();
  temp.data = x;
  temp.next = null;

  // Move to end of list
  Node curr = head;
  while (curr.next!= null) { curr = curr.next; }

  // Append new node
  curr.next = temp;

  // Return head
  return head;
}
