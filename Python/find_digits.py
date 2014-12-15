test_cases = int(raw_input())

for y in range(test_cases):
    num = raw_input()
    count = 0
    for index in range(len(num)):
        if int(num[index]) == 0:
            continue
        if int(num) % int(num[index]) == 0:
            count += 1

    print count
