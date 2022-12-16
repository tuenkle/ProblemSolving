import sys
a, b = map(int, sys.stdin.readline().split())
def cal_gcd(x, y):
    while True:
        remain = x % y
        if remain == 0:
            return y
        x = y
        y = remain
gcd = cal_gcd(a, b)
lcm = int(a * b / gcd)
print(gcd)
print(lcm)