import sys
from collections import deque
N = int(sys.stdin.readline())
myqueue = deque()
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "pop":
        print(myqueue.popleft()) if myqueue else print(-1)
    elif cmd == "size":
        print(len(myqueue))
    elif cmd == "empty":
        print(0) if myqueue else print(1)
    elif cmd == "front":
        print(myqueue[0]) if myqueue else print(-1)
    elif cmd == "back":
        print(myqueue[-1]) if myqueue else print(-1)
    else:
        num = int(cmd.split()[1])
        myqueue.append(num)