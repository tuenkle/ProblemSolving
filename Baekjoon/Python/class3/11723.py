import sys
input = sys.stdin.readline
M = int(input())
myset = set()
for _ in range(M):
    a = input().split()
    cmd = a[0]
    if len(a) == 2:
        x = int(a[1])
        if cmd == "add":
            myset.add(x)
        elif cmd == "remove":
            myset.discard(x)
        elif cmd == "check":
            print(1) if x in myset else print(0)
        elif cmd == "toggle":
            myset.remove(x) if x in myset else myset.add(x)
    else:
        if cmd == "all":
            myset = {i for i in range(1, 21)}
        elif cmd == "empty":
            myset = set()
