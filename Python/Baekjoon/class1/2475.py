import sys
a = map(int, sys.stdin.readline().split())
sum = 0
for i in a:
    sum += i * i
print(sum % 10)