import sys
A, B, V = map(int, sys.stdin.readline().split())
days = 0
start = 0
while True:
    days += 1
    start += A
    if start >= V:
        break
    start -= B
print(days)

