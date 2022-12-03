import sys
from collections import deque
N = int(sys.stdin.readline())
myqueue = deque(i for i in range(1, N + 1))
remove_turn = True
while len(myqueue) > 1:
    if remove_turn:
        myqueue.popleft()
    else:
        myqueue.append(myqueue.popleft())
    remove_turn = not remove_turn

print(myqueue.pop())