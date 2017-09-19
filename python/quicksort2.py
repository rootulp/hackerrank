def print_arr(arr):
    print(" ".join(map(str, arr)))

def divide(arr, pivot_i=0):
    if len(arr) <= 1:
        return arr
    pivot = arr[pivot_i]
    left = []
    right = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        
    sorted_arr = divide(left) + [pivot] + divide(right)
    print_arr(sorted_arr)
    return sorted_arr

n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
divide(arr)

