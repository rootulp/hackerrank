num_test_cases = raw_input()
test_cases = []

for i in range(int(num_test_cases)):
    test_cases.append(raw_input())

gem_stones = []
gem_stones.extend(test_cases.pop())
gem_stones = list(set(gem_stones))  # delete duplicates

not_gem_stones = []

for x in range(len(test_cases)):
    for y in range(len(gem_stones)):
        if test_cases[x].count(gem_stones[y]) == 0:
            not_gem_stones.append(gem_stones[y])

gem_stones = set(gem_stones) - set(not_gem_stones)
print(len(gem_stones))
