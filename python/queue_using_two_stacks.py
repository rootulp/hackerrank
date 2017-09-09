class Queue:

    def __init__(self):
        self.stack_most_recent_on_top = []
        self.stack_least_recent_on_top = []

    def enqueue(self, element):
        self.stack_most_recent_on_top.append(element)

    def dequeue(self):
        self.move_stacks()
        return self.stack_least_recent_on_top.pop()

    def peek(self):
        self.move_stacks()
        return (self.stack_least_recent_on_top[-1])

    # We only need to move elements from most_recent_on_top to
    # least_recent_on_top if least_recent_on_top is empty
    def move_stacks(self):
        if not self.stack_least_recent_on_top:
            while self.stack_most_recent_on_top:
                self.stack_least_recent_on_top.append(
                    self.stack_most_recent_on_top.pop()
                )

queue = Queue()
q = int(input().strip())
for _ in range(q):
    query = list(map(int, input().strip().split(' ')))
    if query[0] == 1:
        queue.enqueue(query[1])
    elif query[0] == 2:
        queue.dequeue()
    elif query[0] == 3:
        print(queue.peek())
