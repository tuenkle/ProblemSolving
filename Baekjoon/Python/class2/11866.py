import sys
N, K = map(int, sys.stdin.readline().split())
a = [i + 1 for i in range(N)]
answer = []
while len(a) > 0:
    for i in range(K):
        if i == K - 1:
            answer.append(a.pop(0))
        else:
            a.append(a.pop(0))
print("<", end="")
for i, j in enumerate(answer):
    if i == len(answer) - 1:
        print(j, end=">")
    else:
        print(j, end=", ")