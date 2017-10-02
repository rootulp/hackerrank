Node RemoveDuplicates(Node head) {
    Node curr = head;
    while (curr.next != null){
        if (curr.data == curr.next.data){
            curr.next = curr.next.next; // Delete node
        } else {
            curr = curr.next;
        }
    }
    return head;
}
