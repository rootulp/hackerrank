from itertools import combinations

string, k = input().strip().split()
string = sorted(string)
k = int(k)

for length in range(1, k + 1):
    for combination in combinations(string, length):
        print("".join(combination))
