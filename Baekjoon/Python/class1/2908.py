import sys
a, b = sys.stdin.readline().strip().split()
a = a[::-1]
b = b[::-1]
print(max(a, b))