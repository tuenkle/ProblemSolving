import sys
N, M = map(int, sys.stdin.readline().split())
al2 = [sys.stdin.readline().rstrip() for _ in range(N)]
answer = 10000000
for i in range(N-7):
    for j in range(M-7):
        first_w_count = 0
        first_b_count = 0
        current_w = True
        temp_current_w = current_w
        for a in [al2[x][j:j+8] for x in range(i, i+8)]:
            for k in a:
                if k == "W":
                    if current_w:
                        first_b_count += 1
                    else:
                        first_w_count += 1
                else:
                    if current_w:
                        first_w_count += 1
                    else:
                        first_b_count += 1
                current_w = not current_w
            current_w = not temp_current_w
            temp_current_w = not temp_current_w
        answer = min(answer, min(first_w_count, first_b_count))
print(answer)