_ = int(input())
set_a = set(map(int, input().split(" ")))

num_commands = int(input())
for _ in range(num_commands):
    command, _ = input().split(" ")
    set_b = set(map(int, input().split(" ")))
    if command == "intersection_update":
        set_a.intersection_update(set_b)
    elif command == "update":
        set_a.update(set_b)
    elif command == "symmetric_difference_update":
        set_a.symmetric_difference_update(set_b)
    elif command == "difference_update":
        set_a.difference_update(set_b)

print(sum(set_a))

