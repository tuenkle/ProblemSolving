import sys
input = sys.stdin.readline
n = int(input())
maxi = 0
mini = 1000000000
for _ in range(n):
    x = int(input())
    maxi = max(x, maxi)
    mini = min