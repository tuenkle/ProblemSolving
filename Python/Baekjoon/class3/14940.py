import sys
input = sys.stdin.readline
n, m = map(int, input().split())
startpoint_x = 0
startpoint_y = 0
lines = []
for j in range(n):
    line = list(map(int, input().split()))
    for i, value in enumerate(line):
        if value == 2:
            startpoint_y = j
            startpoint_x = i
    lines.append(line)

answerlines = [[-1 for _ in range(m)] for _ in range(n)]
answerlines[startpoint_y][startpoint_x] = 0

from collections import deque
queue = deque()
queue.append((0, startpoint_x, startpoint_y))
while queue:
    current = queue.popleft()
    current_x = current[1]
    current_y = current[2]
    if 0 <= current_x+1 < m:
        if lines[current_y][current_x+1] != 0 and answerlines[current_y][current_x+1] == -1:
            answerlines[current_y][current_x+1] = current[0]+1
            queue.append((current[0]+1, current_x+1, current_y))
    if 0 <= current_x-1 < m:
        if lines[current_y][current_x-1] != 0 and answerlines[current_y][current_x-1] == -1:
            answerlines[current_y][current_x-1] = current[0]+1
            queue.append((current[0]+1, current_x-1, current_y))
    if 0 <= current_y+1 < n:
        if lines[current_y+1][current_x] != 0 and answerlines[current_y+1][current_x] == -1:
            answerlines[current_y+1][current_x] = current[0]+1
            queue.append((current[0]+1, current_x, current_y+1))
    if 0 <= current_y-1 < n:
        if lines[current_y-1][current_x] != 0 and answerlines[current_y-1][current_x] == -1:
            answerlines[current_y-1][current_x] = current[0]+1
            queue.append((current[0]+1, current_x, current_y-1))
for i, value in enumerate(lines):
    for i2, value2 in enumerate(value):
        if value2 == 0:
            answerlines[i][i2] = 0
for i in answerlines:
    for j in i:
        print(j,end=" ")
    print()
