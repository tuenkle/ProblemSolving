import sys
N = int(sys.stdin.readline())
j = 0
while True:
    if j == 0:
        N -= 1
    else:
        N -= 6 * j
    if N <= 0:
        break
    j += 1
print(j + 1)

