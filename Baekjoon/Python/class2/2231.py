import sys
N = int(sys.stdin.readline())
answer = 0
for i in range(max(N - 9 * len(str(N)), 1), N):
    if sum(map(int, str(i))) + i == N:
        answer = i
        break
print(answer)