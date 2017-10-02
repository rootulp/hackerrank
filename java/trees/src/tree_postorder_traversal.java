/* you only have to complete the function given below.
Node is defined as

class Node {
    int data;
    Node left;
    Node right;
}

*/
void Postorder(Node root) {
    if (root == null) { return; }
    Postorder(root.left);
    Postorder(root.right);
    System.out.print(root.data + " ");
}
