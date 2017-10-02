class StackWithMax:

    def __init__(self):
        self.stack = []

    def push(self, element):
        if self.stack and self.getMax() > element:
            self.stack.append((element, self.getMax()))
        else:
            self.stack.append((element, element))

    def pop(self):
        self.stack.pop()

    def getMax(self):
        return self.stack[-1][1]


stackWithMax = StackWithMax()
n = int(input().strip())
for _ in range(n):
    command, *element = tuple(map(int, input().strip().split(' ')))
    if command == 1:
        stackWithMax.push(*element)
    elif command == 2:
        stackWithMax.pop()
    elif command == 3:
        print(stackWithMax.getMax())

