(_, d) = tuple(map(int, input().strip().split(' ')))
arr = list(map(int, input().strip().split(' ')))
new_arr = arr[d:] + arr[:d]
print(' '.join(map(str, new_arr)))
