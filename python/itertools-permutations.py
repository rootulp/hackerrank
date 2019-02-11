from itertools import permutations

string, k = input().split(" ")
permutation_len = int(k)
for permutation in sorted(permutations(string, permutation_len)):
    print("".join(permutation))
