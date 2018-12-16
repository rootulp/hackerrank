from collections import deque


def array_left_rotation(a, n, k):
    queue = deque(a)
    for x in range(k):
        queue.append(queue.popleft())
    return list(queue)


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
