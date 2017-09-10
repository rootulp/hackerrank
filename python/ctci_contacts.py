from collections import deque

class Node:

    def __init__(self, terminal = False):
        self.children = dict()
        self.terminal = terminal

    def __repr__(self):
        return "Children: (" + str(self.children) + ") and Terminal: (" + str(self.terminal)  + ")"


class Trie:
    
    def __init__(self):
        self.root = Node()
        

    def add(self, chars, node):
        if chars:
            self.add_char(chars, node)
        else:
            node.terminal = True
    
    def add_char(self, chars, node):
        current_char = chars.popleft()
        child = node.children.get(current_char)
        if child:
            self.add(chars, child)
        else:
            new_child = Node()
            node.children[current_char] = new_child
            self.add(chars, new_child)


    def find(self, chars):
        return False


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
        chars = deque(list(contact))
        self.trie.find(chars)


num_operations = int(input().strip())
contacts = Contacts()

for _ in range(num_operations):
    operation, contact = input().strip().split(' ')
    contacts.perform(operation, contact)
    print(contacts.trie.root)
