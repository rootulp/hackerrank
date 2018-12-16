""" Tries: Contacts """


class Node(object):
    """ Trie Node """

    # Hacky optimization necessary to pass test case # 12
    __slots__ = ['children', 'word_count']

    def __init__(self):
        self.children = dict()
        self.word_count = 0

    def __repr__(self):
        return ("Word Count: " + str(self.word_count) +
                " Children: " + str(self.children))


class Trie(object):
    """ Trie Node """

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

    @staticmethod
    def create_child(char, node):
        node.children[char] = Node()


class Contacts(object):

    def __init__(self):
        self.trie = Trie()

    def perform(self, operation, contact):
        if operation == 'add':
            self.trie.add_key(contact)
        elif operation == 'find':
            print(self.find(contact))

    def find(self, contact):
        found = self.trie.find_key(contact)
        return found.word_count if found else 0


NUM_OPERATIONS = int(input().strip())
CONTACTS = Contacts()

for _ in range(NUM_OPERATIONS):
    op, name = input().strip().split(' ')
    CONTACTS.perform(op, name)
