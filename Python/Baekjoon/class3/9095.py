import sys
T = int(sys.stdin.readline())
hashmap = {1:1, 2:2, 3:3}
for _ in range(T):
    n = int(sys.stdin.readline())
    combination = []
    while n > 0:
        if n >= 3:
            n -= 3
            combination.append(3)
        elif n == 2:
            n -= 2
            combination.append(2)
        elif n == 1:
            n -= 1
            combination.append(1)
    if 2 in combination:
