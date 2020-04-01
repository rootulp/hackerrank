from itertools import combinations_with_replacement

string, k = input().strip().split()
string = sorted(string)
k = int(k)

for combination in combinations_with_replacement(string, k):
    print("".join(combination))
