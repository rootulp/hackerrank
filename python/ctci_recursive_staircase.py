def staircase(num_stairs):
    if num_stairs == 1:
        return 1
    elif num_stairs == 2:
        return 2
    elif num_stairs == 3:
        return 4
    else:
        return staircase(num_stairs - 1) + staircase(num_stairs - 2) + staircase(num_stairs - 3)

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(staircase(n))
