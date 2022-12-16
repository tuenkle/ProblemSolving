import sys
N = int(sys.stdin.readline())
for i in range(N//3 + 1):
    remain = N - i * 3
    if remain % 5 == 0:
        print(i + remain // 5)
        break
else:
    print(-1)
