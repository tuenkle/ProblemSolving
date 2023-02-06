import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
input_list2 = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
for y, v in enumerate(input_list2):
    for x, v2 in enumerate(v):
        if v2 == 1:
            queue.append((x, y, 0))

def verifying(x, y):
    if x == -1 or x == M or y == -1 or y == N:
        return False
    if input_list2[y][x] == 1 or input_list2[y][x] == -1:
        return False
    return True
last_day = 0
while queue:
    x, y, day = queue.popleft()
    last_day = max(day, last_day)
    for k in range(-1, 2, 2):
        newX = x + k
        newY = y
        if verifying(newX, newY):
            input_list2[newY][newX] = 1
            queue.append((newX, newY, day + 1))
        newX = x
        newY = y + k
        if verifying(newX, newY):
            input_list2[newY][newX] = 1
            queue.append((newX, newY, day + 1))
for i in input_list2:
    if 0 in i:
        print(-1)
        break
else:
    print(last_day)

