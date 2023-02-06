import sys
import math
input = sys.stdin.readline
m, n = map(int, input().split())
print(math.comb(m, n))