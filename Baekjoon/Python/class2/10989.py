import sys
N = int(sys.stdin.readline())
my_dic = {}

for _ in range(N):
    a = int(sys.stdin.readline())
    my_dic[a] = my_dic.get(a, 0) + 1
for i in sorted(my_dic.keys()):
    for _ in range(my_dic[i]):
        print(i)
