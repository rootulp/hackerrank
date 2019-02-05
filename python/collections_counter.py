from collections import Counter

num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

# Dict from shoe_size to num of remaining shoes at that size
available_shoes = Counter(shoe_sizes)
total = 0

for customer in range(num_customers):
    desired_shoe_size, willing_to_pay = map(int, input().split())
    if available_shoes[desired_shoe_size] > 0:
        total += willing_to_pay
        available_shoes[desired_shoe_size] -= 1

print(total)
