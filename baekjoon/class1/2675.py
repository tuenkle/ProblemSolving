import sys
T = int(sys.stdin.readline())
input_data = [sys.stdin.readline() for _ in range(T)]
for j in input_data:
    R, S = j.split()
    R = int(R)
    S = S.strip()
    for i in S:
        print(i * R, end="")
    print()
