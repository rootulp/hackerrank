from collections import deque

class Node(object):

    # Hacky optimization necessary to pass test case # 12
    __slots__ = ['children', 'word_count']

    def __init__(self, terminal = False):
        self.children = dict()
        self.word_count = 0


    def __repr__(self):
        return "Children: (" + str(self.children) + ") and Word Count: (" + str(self.word_count)  + ")"


class Trie:
    
    def __init__(self):
        self.root = Node()
        
    def add_key(self, key):
        node = self.root

        for char in key:
            node = self.create_child_if_absent(char, node)
            node.word_count += 1

    def find_key(self, key):
        node = self.root

        for char in key:
            if char in node.children:
                node = node.children.get(char)
            else:
                return False

        return node

    def create_child_if_absent(self, char, node):
        if char not in node.children:
            self.create_child(char, node)
        return node.children.get(char)
    
    def create_child(self, char, node):
        node.children[char] = Node()


class Contacts:
    
    def __init__(self):
        self.trie = Trie()
    
    def perform(self, operation, contact):
        if operation == 'add':
            self.trie.add_key(contact)
        elif operation == 'find':
            print(self.find(contact))
        
    def find(self, contact):
        found_contact = self.trie.find_key(contact)

        if (found_contact):
            return found_contact.word_count
        else:
            return 0


num_operations = int(input().strip())
contacts = Contacts()

for _ in range(num_operations):
    operation, contact = input().strip().split(' ')
    contacts.perform(operation, contact)
