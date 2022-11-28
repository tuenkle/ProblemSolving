import sys
N = int(sys.stdin.readline())
al = [int(sys.stdin.readline()) for _ in range(N)]
al.sort()
for i in al:
    print(i)
