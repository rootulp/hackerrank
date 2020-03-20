from collections import defaultdict

n, m = map(int, input().strip().split(" "))
occurences = defaultdict(list)
for index in range(n):
    character = str(input().strip())
    occurences[character].append(str(index + 1))

for index in range(m):
    character = str(input().strip())
    if character in occurences:
        print(" ".join(occurences[character]))
    else:
        print("-1")
