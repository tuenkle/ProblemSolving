import sys
input = sys.stdin.readline
N = int(input())
al = list(map(int, input().split()))
sorted_al = sorted(list(set(al)))
hashmap = {}
for i, value in enumerate(sorted_al):
    hashmap[value] = i
for i in al:
    print(hashmap[i], end=" ")
