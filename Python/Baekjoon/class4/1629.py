import sys
A, B, C = map(int, sys.stdin.readline().split())
def temp(b):
    if b % 2 == 0:
        return ((temp(b // 2) % C) ** 2) % C
    elif b == 1:
        return A % C
    else:
        return ((((temp(b // 2) % C) ** 2) % C) * temp(1)) % C
print(temp(B))
