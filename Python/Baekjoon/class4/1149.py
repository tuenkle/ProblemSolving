import sys
input = sys.stdin.readline
N = int(input())
input_list = [tuple(map(int, input().split())) for _ in range(N)]
answer_matrix = [list(input_list[0])] + [[1000000000] * 3 for _ in range(N - 1)]

def find_next(x, y):
    if x == 0 and y == 1:
        return 2
    if x == 0 and y == 2:
        return 1
    if x == 1 and y == 2:
        return 0
    if x == 1 and y == 0:
        return 2
    if x == 2 and y == 1:
        return 0
    if x == 2 and y == 0:
        return 1
for i in range(1, N):
    for j in range(3):
        if j == 0:
            answer_matrix[i][j] = min(answer_matrix[i][j], input_list[i][j] + answer_matrix[i - 1][1])
            answer_matrix[i][j] = min(answer_matrix[i][j], input_list[i][j] + answer_matrix[i - 1][2])
        elif j == 1:
            answer_matrix[i][j] = min(answer_matrix[i][j], input_list[i][j] + answer_matrix[i - 1][0])
            answer_matrix[i][j] = min(answer_matrix[i][j], input_list[i][j] + answer_matrix[i - 1][2])
        elif j == 2:
            answer_matrix[i][j] = min(answer_matrix[i][j], input_list[i][j] + answer_matrix[i - 1][0])
            answer_matrix[i][j] = min(answer_matrix[i][j], input_list[i][j] + answer_matrix[i - 1][1])
print(min(answer_matrix[-1]))
