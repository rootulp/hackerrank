/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/
int FindMergeNode(Node headA, Node headB) {

    // Make two temp nodes to iterate through lists
    Node currA = headA;
    Node currB = headB;

    while (currA != currB){ // Stop when nodes find merge
        if (currA.next == null) {currA = headB; } // Jump A node to list B
        if (currB.next == null) {currB = headA; } // Jump B node to list A
        currA = currA.next;
        currB = currB.next;
    }

    return currA.data;
}
