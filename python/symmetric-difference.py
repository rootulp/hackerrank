# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
M = set(map(int, input().split()))
_ = input()
N = set(map(int, input().split()))
print("\n".join(map(str, sorted(M.symmetric_difference(N)))))
