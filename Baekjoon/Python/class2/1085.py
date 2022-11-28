import sys
x, y, w, h = map(int, sys.stdin.readline().split())
ans = w
ans = min(x, ans)
ans = min(y, ans)
ans = min(w- x, ans)
ans = min(h -y, ans)
print(ans)