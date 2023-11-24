import sys
input = sys.stdin.readline
N, M = map(int, input().split())
from itertools import product
for i in product(range(1, N+1), repeat=M):
    breakkk = False
    for j in range(len(i)):
        if breakkk:
            break
        for k in range(j, len(i)):
            if i[j] > i[k]:
                breakkk = True
                break
    if not breakkk:
        for j in i:
            print(j, end=" ")
        print()