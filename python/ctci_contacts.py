from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.children = set()

    def add_child(self, child):
        self.children.add(child)
        
    def get_child(self, data):
        for child in self.children:
            if child.data == data:
                return child

    def __str__(self):
        return "Data: (" + self.data + "), Children: (" + self.children_str() + ")"
    
    def children_str(self):
        return ', '.join([str(child) for child in self.children])


class Trie:
    
    def __init__(self):
        self.root = Node('ROOT')
        
    def add(self, chars, node):
        # print(node)
        # print(chars)
        if chars:
            current_char = chars.popleft()
            child = node.get_child(current_char)
            if child:
                self.add(chars, child)
            else:
                new_child = Node(current_char)
                node.add_child(new_child)
                self.add(chars, new_child)


class Contacts:
    
    def __init__(self):
        self.trie = Trie()
    
    def perform(self, operation, contact):
        if operation == 'add':
            self.add(contact)
        elif operation == 'find':
            print(self.find(contact))


    def add(self, contact):
        chars = deque(list(contact))
        self.trie.add(chars, self.trie.root)
        
        
    def find(self, contact):
        self.trie.find(contact)
    

num_operations = int(input().strip())
contacts = Contacts()

for _ in range(num_operations):
    operation, contact = input().strip().split(' ')
    contacts.perform(operation, contact)
    # print(contacts.trie.root)
