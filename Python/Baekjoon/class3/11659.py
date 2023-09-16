import sys
input = sys.stdin.readline
N, M = map(int, input().split())
inputlist = list(map(int, input().split()))
sumlist = [inputlist[0]]
for i in range(1, N):
    sumlist.append(sumlist[i-1]+inputlist[i])
for _ in range(M):
    i, j = map(int, input().split())
    if i-2 < 0:
        print(sumlist[j-1])
    else:
        print(sumlist[j-1]-sumlist[i-2])