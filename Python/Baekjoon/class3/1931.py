import sys
input = sys.stdin.readline
N = int(input())
input_list = [tuple(map(int, input().split())) for _ in range(N)]
input_list.sort(key=lambda x:(x[0], x[1]))
i = 1
answerlist = [input_list[0]]
while i < len(input_list):
    if answerlist[-1][1] <= input_list[i][0]:
        answerlist.append(input_list[i])
    elif answerlist[-1][1] >= input_list[i][1]:
        answerlist[-1] = input_list[i]
    i += 1
print(len(answerlist))
