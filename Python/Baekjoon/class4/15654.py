import sys
import itertools
input = sys.stdin.readline
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
for i in list(itertools.permutations(input_list, M)):
    for j in i:
        print(j, end=" ")
    print()
