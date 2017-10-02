/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/
int CompareLists(Node headA, Node headB) {
    if (headA.data != headB.data) { return 0; }
    if (headA.next == null && headB.next == null) { return 1; }
    if (headA.next == null || headB.next == null) { return 0; }
    return CompareLists(headA.next, headB.next);
}
