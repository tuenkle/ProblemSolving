import sys
N, M = map(int, sys.stdin.readline().split())
il = list(map(int, sys.stdin.readline().split()))
deviation = 3000000
answer = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum = il[i] + il[j] + il[k]
            if deviation > M - sum and M >= sum:
                deviation = M - sum
                answer = sum
print(answer)