import sys
T = int(sys.stdin.readline())
mil = [sys.stdin.readline().strip() for _ in range(T)]
for mi in mil:
    H, W, N = map(int, mi.split())
    number = (N - 1) // H + 1
    floor = N % H
    if floor == 0:
        floor = H
    print(f"{floor}{str(number).zfill(2)}")