import sys
N = int(sys.stdin.readline())
iset = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
i2set = map(int, sys.stdin.readline().split())
for i in i2set:
    if i in iset:
        print(1)
    else:
        print(0)