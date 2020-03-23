number_of_test_cases = int(input().strip())
for _ in range(number_of_test_cases):
    try:
        a, b = map(int, input().strip().split(" "))
        print(a // b)
    except Exception as e:
        print("Error Code:", e)
