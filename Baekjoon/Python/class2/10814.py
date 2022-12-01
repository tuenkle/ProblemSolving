import sys
N = int(sys.stdin.readline())
al2 = []
for _ in range(N):
    al = sys.stdin.readline().rstrip().split()
    al[0] = int(al[0])
    al2.append(al)
al2.sort(key=lambda x: x[0])
for i in al2:
    print(i[0], i[1])
