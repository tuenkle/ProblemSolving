import sys
N = int(sys.stdin.readline())
answer_list = [0, 1, 1]
def get_min(number):
    if number <= len(answer_list):
        return answer_list[number - 1]
    for i in range(len(answer_list), number):
        answer = answer_list[i - 1]
        real_number = i + 1
        if real_number % 3 == 0:
            answer = min(answer, answer_list[real_number // 3 - 1])
        if real_number % 2 == 0 :
            answer = min(answer, answer_list[real_number // 2 - 1])
        answer_list.append(answer + 1)
    return answer_list[number - 1]
print(get_min(N))