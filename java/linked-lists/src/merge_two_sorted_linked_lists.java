/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/

Node MergeLists(Node list1, Node list2) {
  if (list1 == null) { return list2; }
  if (list2 == null) { return list1; }

  Node head = null;

  if (list1.data <= list2.data) {
    head = list1;
    head.next = MergeLists(list1.next, list2);
  } else {
    head = list2;
    head.next = MergeLists(list1, list2.next);
  }

  return head;
}
