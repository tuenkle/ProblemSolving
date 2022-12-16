import sys
from collections import deque
N = int(sys.stdin.readline())
mydeque = deque()
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith("push_front"):
        num = int(cmd.split()[1])
        mydeque.appendleft(num)
    elif cmd.startswith("push_back"):
        num = int(cmd.split()[1])
        mydeque.append(num)
    elif cmd == "pop_front":
        print(mydeque.popleft()) if mydeque else print(-1)
    elif cmd == "pop_back":
        print(mydeque.pop()) if mydeque else print(-1)
    elif cmd == "size":
        print(len(mydeque))
    elif cmd == "empty":
        print(0) if mydeque else print(1)
    elif cmd == "front":
        print(mydeque[0]) if mydeque else print(-1)
    else:
        print(mydeque[-1]) if mydeque else print(-1)
