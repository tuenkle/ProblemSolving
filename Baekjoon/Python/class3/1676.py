import sys
import math
N = int(sys.stdin.readline())
count = 0
for i in str(math.factorial(N))[::-1]:
    if i == "0":
        count += 1
    else:
        break
print(count)