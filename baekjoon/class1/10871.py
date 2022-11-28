import sys
input_data = [sys.stdin.readline().strip() for i in range(2)]
N, X = map(int, input_data[0].split())
A = map(int, input_data[1].split())
for i in A:
    if i < X:
        print(i, end=" ")
