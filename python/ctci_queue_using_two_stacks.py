class MyQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def peek(self):
        self.migrate_stacks_if_necessary()
        return self.stack_2[-1]

    def pop(self):
        self.migrate_stacks_if_necessary()
        return self.stack_2.pop()

    def put(self, value):
        self.stack_1.append(value)

    def migrate_stacks_if_necessary(self):
        if len(self.stack_2) == 0:
            self.migrate_stacks()

    def migrate_stacks(self):
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
