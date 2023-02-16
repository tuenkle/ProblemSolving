import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
mydict = {}
for _ in range(N - 1):
    x, y = map(int, input().split())
    mydict.setdefault(x, []).append(y)
    mydict.setdefault(y, []).append(x)
node_to_parent = {}
queue = deque([[1]])

while queue:
    current = queue.popleft()
    for k in current:
        for j in mydict[k]:
            if not j in node_to_parent:
                node_to_parent[j] = k
                if queue:
                    queue[-1].append(j)
                else:
                    queue.append([j])
for j in range(2, N + 1):
    print(node_to_parent[j])
