import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
count = 0
while K > 0:
    coin = coins.pop()
    remove_coins = K // coin
    count += remove_coins
    K -= coin * (K // coin)
print(count)