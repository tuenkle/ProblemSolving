import sys
import itertools
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
answer_list = itertools.permutations(num_list, M)
answer_set = set()
for i in answer_list:
    if i in answer_set:
        continue
    for j in i:
        print(j, end=" ")
    print()
    answer_set.add(i)