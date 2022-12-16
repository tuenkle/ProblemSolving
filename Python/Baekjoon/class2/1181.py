import sys
N = int(sys.stdin.readline())
input_set = set()
for _ in range(N):
    input_set.add(sys.stdin.readline().rstrip())
input_list = list(input_set)
input_list.sort(key=lambda x : (len(x), x))
for i in input_list:
    print(i)