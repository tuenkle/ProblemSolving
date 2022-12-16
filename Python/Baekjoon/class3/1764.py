import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
a = set()
b = set()
for _ in range(N):
    a.add(input().rstrip())
for _ in range(M):
    b.add(input().rstrip())
c = list(a & b)
c.sort()
print(len(c))
for i in c:
    print(i)