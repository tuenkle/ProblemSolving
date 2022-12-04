import sys
input = sys.stdin.readline
N, M = map(int, input().split())
id_to_name = {}
name_to_id = {}
for i in range(1, N + 1):
    name = input().rstrip()
    id_to_name[i] = name
    name_to_id[name] = i
for _ in range(M):
    a = input().rstrip()
    if a.isdecimal():
        print(id_to_name[int(a)])
    else:
        print(name_to_id[a])
