import sys
a = [int(sys.stdin.readline().strip()) for _ in range(9)]
print(max(a))
print(a.index(max(a)) + 1)
