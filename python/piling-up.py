from collections import deque


def isVerticallyStackable(pile):
    vertical_stack = []
    while pile:
        largest_cube, cube_sizes = remove_largest_cube_from_pile(pile)
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
        return (None, cube_sizes)
    elif(cube_sizes[0] > cube_sizes[-1]):
        largest_cube = cube_sizes.popleft()
        return (largest_cube, cube_sizes)
    else:
        largest_cube = cube_sizes.pop()
        return (largest_cube, cube_sizes)



num_test_cases = int(input())
for i in range(num_test_cases):
    num_cubes = int(input())
    pile = deque(map(int, input().strip().split(" ")))
    if(isVerticallyStackable(pile)):
        print("Yes")
    else:
        print("No")
