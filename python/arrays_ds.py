n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print (' '.join(map(str, reversed(arr))))
