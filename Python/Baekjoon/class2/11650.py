import sys
N = int(sys.stdin.readline())
al2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
al2.sort(key=lambda x: (x[0], x[1]))
for i in al2:
    print(i[0], i[1])
