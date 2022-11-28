import sys
N = int(sys.stdin.readline())
il = [int(sys.stdin.readline()) for _ in range(N)]
il.sort()
for i in il:
    print(i)