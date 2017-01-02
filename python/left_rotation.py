(_, d) = tuple(map(int, input().strip().split(' ')))
arr = list(map(int, input().strip().split(' ')))

print(*(arr[d:] + arr[:d]))
