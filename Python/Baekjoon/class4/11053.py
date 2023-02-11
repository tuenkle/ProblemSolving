import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
mylist = [1]
for i in range(1, N):
    max_temp = 0
    for j in range(i):
        if A[j] < A[i] and mylist[j] > max_temp:
            max_temp = mylist[j]
    mylist.append(max_temp + 1)
print(max(mylist))