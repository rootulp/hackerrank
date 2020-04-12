num_elements = int(input())
s = set(map(int, input().split()))
num_operations = int(input())
for _ in range(num_operations):
    operation = input().split(" ")
    if(operation[0] == "pop"):
        s.pop()
    else:
        op, val = operation
        s.discard(int(val))

print(sum(s))
