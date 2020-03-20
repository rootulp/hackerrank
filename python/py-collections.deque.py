from collections import deque

d = deque()

number_of_operations = int(input().strip())
for index in range(number_of_operations):
    operation = input().strip()
    if(operation.startswith("appendleft")):
        method, value = operation.split(" ")
        d.appendleft(value)
    elif(operation.startswith("append")):
        method, value = operation.split(" ")
        d.append(value)
    elif(operation == "popleft"):
        d.popleft()
    elif(operation == "pop"):
        d.pop()


print(" ".join(d))
