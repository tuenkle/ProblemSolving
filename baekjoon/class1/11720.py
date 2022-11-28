import sys
N = int(sys.stdin.readline())
input_data = sys.stdin.readline().strip()
sum = 0
for i in input_data:
    sum += int(i)
print(sum)
