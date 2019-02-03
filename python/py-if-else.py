def is_odd(n):
    return n % 2 == 1

def is_weird(n):
    if is_odd(n):
        return True
    else:
        # n is even
        if 2 <= n <= 5:
            return False
        elif 6 <= n <= 20:
            return True
        elif 20 < n:
            return False

n = int(input())

if (is_weird(n)):
    print("Weird")
else:
    print("Not Weird")
