cache = {
    1: 1,
    2: 2,
    3: 4
}


def staircase(num_stairs):
    if num_stairs not in cache:
        cache[num_stairs] = (staircase(num_stairs - 1) +
                             staircase(num_stairs - 2) +
                             staircase(num_stairs - 3))
    return cache[num_stairs]


test_cases = int(input().strip())
for _ in range(test_cases):
    num_stairs = int(input().strip())
    print(staircase(num_stairs))
