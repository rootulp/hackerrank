#!/bin/python3

def super_digit(n, k):
    digits = map(int, list(n))
    return get_super_digit(str(sum(digits) * k))

def get_super_digit(p):
    if len(p) == 1:
        return int(p)
    else:
        digits = map(int, list(p))
        return get_super_digit(str(sum(digits)))

if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = super_digit(n, k)
    print(result)
