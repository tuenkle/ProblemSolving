import sys
A, B, V = map(int, sys.stdin.readline().split())

last_v = V - A
days = last_v // (A - B) + 1
if last_v % (A - B) != 0:
    days += 1
print(days)