import sys
input = sys.stdin.readline
N, M = map(int, input().split())
al = list(map(int, input().split()))
lo, hi = 0, max(al)
while lo + 1 < hi:
    mid = (lo + hi) // 2
    tree_sum = 0
    for i in al:
        if i > mid:
            tree_sum += i - mid
    if tree_sum > M:
        lo = mid
    elif tree_sum < M:
        hi = mid
    else:
        print(mid)
        break
else:
    print(lo)