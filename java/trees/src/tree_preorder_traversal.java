/* you only have to complete the function given below.
Node is defined as

class Node {
    int data;
    Node left;
    Node right;
}

*/

void Preorder(Node root) {
    if (root == null) { return; }
    System.out.print(root.data + " ");
    Preorder(root.left);
    Preorder(root.right);
}
