current_petrol = 0
current_position = 0
n = int(input().strip())
for i in range(n):
    petrol, distance = map(int, input().strip().split(' '))
    current_petrol += petrol
    if (current_petrol > distance):
        current_petrol -= distance
    else:
        current_petrol = 0
        current_position = i
print(current_position + 1)
