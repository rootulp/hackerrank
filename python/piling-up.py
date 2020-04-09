from collections import deque


def isVerticallyStackable(pile):
    vertical_stack = []
    while pile:
        largest_cube = remove_largest_cube_from_pile(pile)
        if vertical_stack == []:
            vertical_stack.append(largest_cube)
        else:
            top_of_stack = vertical_stack[-1]
            if(top_of_stack < largest_cube):
                return False
            vertical_stack.append(largest_cube)
    return True


def remove_largest_cube_from_pile(cube_sizes):
    if(cube_sizes == []):
        return None
    elif(cube_sizes[0] > cube_sizes[-1]):
        return cube_sizes.popleft()
    else:
        return cube_sizes.pop()



num_test_cases = int(input())
for i in range(num_test_cases):
    num_cubes = int(input())
    pile = deque(map(int, input().strip().split(" ")))
    if(isVerticallyStackable(pile)):
        print("Yes")
    else:
        print("No")
