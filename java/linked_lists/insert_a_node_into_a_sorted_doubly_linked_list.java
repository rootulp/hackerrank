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

Node SortedInsert(Node head,int data) {

    // Create new node
    Node temp = new Node();
    temp.data = data;
    temp.next = null;
    temp.prev = null;

    // Check if list is empty
    if (head == null) { return temp; }


    // Insert at head
    Node curr = head;
    if (temp.data <= curr.data) {
        curr.prev = temp;
        temp.next = curr;
        return temp; // Return new head
    }

    // Iterate through list
    while (curr.next != null){
        if (temp.data <= curr.data){
            curr.prev.next = temp;
            temp.prev = curr.prev;
            temp.next = curr;
            curr.prev = temp;
            return head;
        }
        curr = curr.next;
    }

    // At last node
    if (temp.data <= curr.data){ // Insert before last node
        curr.prev.next = temp;
        temp.prev = curr.prev;
        temp.next = curr;
        curr.prev = temp;
        return head;
    }

    // Insert at tail
    curr.next = temp;
    temp.prev = curr;
    return head;

}
