from collections import Counter


size = int(input().strip())
counts = Counter((map(int, input().strip().split(' '))))
element, count = counts.most_common(1)[0]
print(size - count)
