import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
mylist = [i + 1 for i in range(N)]
for i in list(combinations(mylist, M)):
    for j in i:
        print(j, end=" ")
    print()