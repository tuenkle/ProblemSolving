import sys
input = sys.stdin.readline
N, M = map(int, input().split())
square_matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
square_matrix = [[0] * len(square_matrix[0])] + square_matrix

for i in range(1, N + 1):
    for j in range(1, N + 1):
        square_matrix[i][j] = square_matrix[i - 1][j] + square_matrix[i][j - 1] + square_matrix[i][j] - square_matrix[i-1][j-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = square_matrix[x2][y2] - square_matrix[x2][y1 - 1] - square_matrix[x1 - 1][y2] + square_matrix[x1-1][y1-1]
    print(answer)

