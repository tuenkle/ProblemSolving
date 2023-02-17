import sys
input = sys.stdin.readline
n = int(input())
input_triangle = []
answer_triangle = []
for i in range(n):
    input_list = list(map(int, input().split()))
    input_triangle.append(input_list)
    answer_triangle.append(input_list.copy())
for i in range(len(input_triangle) - 1):
    for j in range(len(input_triangle[i])):
        answer_triangle[i + 1][j] = max(answer_triangle[i + 1][j], answer_triangle[i][j] + input_triangle[i+1][j])
        answer_triangle[i + 1][j+1] = max(answer_triangle[i + 1][j+1], answer_triangle[i][j] + input_triangle[i+1][j+1])

print(max(answer_triangle[-1]))