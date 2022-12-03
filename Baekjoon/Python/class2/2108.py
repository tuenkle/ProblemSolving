import sys
from collections import Counter
N = int(sys.stdin.readline())
al = [int(sys.stdin.readline()) for _ in range(N)]
al.sort()
counter = Counter(al)
print(round(sum(al)/N))
print(al[N//2])
two_min_list = [500000, 500000]
mode_list = counter.most_common(2)
if len(mode_list) == 1 or mode_list[0][1] > mode_list[1][1]:
    print(mode_list[0][0])
else:
    print(mode_list[1][0])
print(al[-1] - al[0])