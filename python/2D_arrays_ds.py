#!/bin/python3


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# returns the hourglass sum for the hourglass with center (x, y)


def calculate_hourglass_sum(x, y):
    topleft = arr[x - 1][y - 1]
    topmid = arr[x - 1][y]
    topright = arr[x - 1][y + 1]
    mid = arr[x][y]
    botleft = arr[x + 1][y - 1]
    botmid = arr[x + 1][y]
    botright = arr[x + 1][y + 1]
    return topleft + topmid + topright + mid + botleft + botmid + botright


hourglass_sums = []
for x in range(1, 5):
    for y in range(1, 5):
        hourglass_sums.append(calculate_hourglass_sum(x, y))

print(max(hourglass_sums))
