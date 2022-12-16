import sys
N = int(sys.stdin.readline())
il2 = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
rank_list = []
for i in il2:
    rank = 1
    for j in il2:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1
    rank_list.append(rank)
for i in rank_list:
    print(i, end=" ")