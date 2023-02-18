import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    input_list = [list(map(int, input().split())) for _ in range(2)]
    input_list.append([0] * len(input_list[0]))
    answer_list = [[input_list[0][0]] + [0] * (len(input_list[0]) - 1)] + [[input_list[1][0]] + [0] * (len(input_list[0]) - 1)] + [[0] * (len(input_list[0]))]
    for i in range(1, len(input_list[0])):
        answer_list[0][i] = max(answer_list[1][i-1], answer_list[2][i-1]) + input_list[0][i]
        answer_list[1][i] = max(answer_list[0][i-1], answer_list[2][i-1]) + input_list[1][i]
        answer_list[2][i] = max(answer_list[0][i-1], answer_list[1][i-1])
    print(max(answer_list[0][-1], answer_list[1][-1], answer_list[2][-1]))
