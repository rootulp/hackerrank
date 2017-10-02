/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/
int HasCycle(Node head) {
    Node runner = head;

    while (runner != null){
        head = head.next;
        runner = runner.next;
        if  (runner == null) { return 0; }
        runner = runner.next;
        if (head == runner) { return 1; }
    }

    return 0;
}
