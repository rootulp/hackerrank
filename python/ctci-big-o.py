import math


def is_prime(test_case):
    if test_case == 1:
        return False
    for factor in range(2, math.ceil(math.sqrt(test_case) + 1)):
        if test_case != factor and test_case % factor == 0:
            return False
    return True


NUM_CASES = int(input().strip())
for _ in range(NUM_CASES):
    test_case = int(input().strip())
    if is_prime(test_case):
        print("Prime")
    else:
        print("Not prime")
