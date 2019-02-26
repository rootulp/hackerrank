#!/bin/python3

def superDigit(n, k):
    p = create_p(n, k)
    return get_super_digit(p)

def get_super_digit(p):
    if len(p) == 1:
        return int(p)
    else:
        digits = map(int, list(p))
        return get_super_digit(str(sum(digits)))

def create_p(n, k):
    return n * k

if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    print(result)
