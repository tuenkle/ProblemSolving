import sys
from collections import deque
testcase = int(sys.stdin.readline())
for _ in range(testcase):
    N, M = map(int, sys.stdin.readline().split())
    al = map(int, sys.stdin.readline().split())
    mydeque = deque()
    index = 0
    for i in al:
        mydeque.append((index, i))
        index += 1
    count = 0
    while mydeque:
        popped = mydeque.popleft()
        for i in mydeque:
            if popped[1] < i[1]:
                mydeque.append(popped)
                break
        else:
            count += 1
            if popped[0] == M:
                break
    print(count)