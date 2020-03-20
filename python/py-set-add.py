# Enter your code here. Read input from STDIN. Print output to STDOUT
distinct_stamps = set()
number_of_stamps = int(input().strip())
for stamp in range(number_of_stamps):
    distinct_stamps.add(input().strip())

print(len(distinct_stamps))
