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
        
    def add_key(self, key):
        node = self.root

        for char in key:
            node = self.create_child_if_absent(char, node)

        node.terminal = True

    def create_child_if_absent(self, char, node):
        if char not in node.children:
            self.create_child(char, node)
        return node.children.get(char)
    
    def create_child(self, char, node):
        node.children[char] = Node()

    def find(self, chars, node):
        if chars:
            current_char = chars.popleft()
            child = node.children.get(current_char)
            if child:
                return self.find(chars, child)
            else:
                return False
        else:
            return node


    def count_terminals(self, node):
        count = 0
        if node.terminal:
            count += 1
        for child in node.children.values():
            count += self.count_terminals(child)
        return count


class Contacts:
    
    def __init__(self):
        self.trie = Trie()
    
    def perform(self, operation, contact):
        if operation == 'add':
            self.add(contact)
        elif operation == 'find':
            print(self.find(contact))


    def add(self, contact):
        self.trie.add_key(contact)
        
        
    def find(self, contact):
        chars = deque(list(contact))
        found_contact = self.trie.find(chars, self.trie.root)
        if (found_contact):
            return self.trie.count_terminals(found_contact)
        else:
            return 0


num_operations = int(input().strip())
contacts = Contacts()

for _ in range(num_operations):
    operation, contact = input().strip().split(' ')
    contacts.perform(operation, contact)
