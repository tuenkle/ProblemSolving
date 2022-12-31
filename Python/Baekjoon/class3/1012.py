import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    al2 = set([tuple(map(int, input().split())) for __ in range(K)])
    count = 0
    while al2:
        stack = []
        current = al2.pop()
        while True:
            for i in al2.copy():
                if abs(current[0] - i[0]) + abs(current[1] - i[1]) == 1:
                    stack.append(i)
                    al2.remove(i)
            if not stack:
                count += 1
                break
            current = stack.pop()
    print(count)