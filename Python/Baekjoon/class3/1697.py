import sys
from collections import deque
import time

input = sys.stdin.readline
N, K = map(int, input().split())
start_time = time.time()
queue = deque([[N, 0]])
checklist = [False for i in range(100001)]
if N == K:
    print(0)
else:
    while True:
        current = queue.popleft()
        if current[0] * 2 == K:
            print(current[1] + 1)
            break
        elif 0 <= current[0] * 2 and current[0] * 2 <= 100000:
            if not checklist[current[0] * 2]:
                checklist[current[0] * 2] = True
                queue.append([current[0] * 2, current[1] + 1])
        if current[0] + 1 == K:
            print(current[1] + 1)
            break
        elif 0 <= current[0] + 1 and current[0] + 1 <= 100000:
            if not checklist[current[0] + 1]:
                checklist[current[0] + 1] = True
                queue.append([current[0] + 1, current[1] + 1])

        if current[0] - 1 == K:
            print(current[1] + 1)
            break
        elif 0 <= current[0] - 1 and current[0] - 1 <= 100000:
            if not checklist[current[0] - 1]:
                checklist[current[0] - 1] = True
                queue.append([current[0] - 1, current[1] + 1])
