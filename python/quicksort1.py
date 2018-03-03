def divide(arr):
    pivot = arr[0]
    left = []
    right = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        return left + [pivot] + right


n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
print(" ".join(map(str, divide(arr))))
