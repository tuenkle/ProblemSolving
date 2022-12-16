import sys
input_data = [int(sys.stdin.readline()) for _ in range(10)]
answer_set = set()
for i in input_data:
    answer_set.add(i % 42)
print(len(answer_set))