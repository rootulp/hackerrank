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
    command = tuple(map(int, input().strip().split(' ')))
    if command[0] == 1:
        stackWithMax.push(command[1])
    elif command[0] == 2:
        stackWithMax.pop()
    elif command[0] == 3:
        print(stackWithMax.getMax())
