import sys
N = int(sys.stdin.readline())
multiple_input = list(map(int, sys.stdin.readline().split()))
M = max(multiple_input)
sum = 0
for i in multiple_input:
    sum += i / M * 100
print(sum / N)
