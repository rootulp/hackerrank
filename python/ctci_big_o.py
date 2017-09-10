from collections import deque


class Sieve(object):

    def __init__(self, upper_bound):
        self.upper_bound = upper_bound + 1
        self.primes = []
        self.populate_primes()
        # print("Primes " + str(self.primes))

    def is_prime(self, potential_prime):
        return potential_prime in self.primes

    def populate_primes(self,):
        remaining = deque(range(2, self.upper_bound))
        while remaining:
            prime = remaining.popleft()
            self.primes.append(prime)
            for multiple in self.multiples(prime):
                if multiple in remaining:
                    remaining.remove(multiple)

    def multiples(self, num):
        return range(num, self.upper_bound, num)


NUM_CASES = int(input().strip())
TEST_CASES = []
for _ in range(NUM_CASES):
    TEST_CASES.append(int(input().strip()))

# print("Max: " + str(max(TEST_CASES)))
SIEVE = Sieve(max(TEST_CASES))
for test_case in TEST_CASES:
    if SIEVE.is_prime(test_case):
        print("Prime")
    else:
        print("Not prime")
