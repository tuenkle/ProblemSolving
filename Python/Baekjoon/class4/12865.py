import sys
input = sys.stdin.readline
N, K = map(int, input().split())
mylist = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, input().split())
    if W <= K:
        for i in range(K, W-1, -1):
            mylist[i] = max(mylist[i], mylist[i - W] + V)
print(max(mylist))