from collections import Counter

strings = Counter()
n = int(input().strip())
for _ in range(n):
    strings.update([input().strip()])
q = int(input().strip())
for _ in range(q):
    print(strings[input().strip()])
