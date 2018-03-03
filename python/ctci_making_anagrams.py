from collections import Counter


def number_needed(a, b):
    counts = Counter(a)
    counts.subtract(Counter(b))
    return sum(map(abs, counts.values()))


a = input().strip()
b = input().strip()
print(number_needed(a, b))
