# import sys
# N = int(sys.stdin.readline())
# count = 0
# mydict = {1:0, 2:1, 3:1}
# def get_min(n):
#     if n in mydict:
#         return mydict[n]
#     if n % 3 == 0:
#         mydict[n] = get_min(n // 3) + 1
#         return mydict[n]
#     min_value = get_min(n - 1)
#     if n % 2 == 0:
#         min_value = min(min_value, get_min(n // 2))
#     mydict[n] = min_value + 1
#     return min_value + 1
# print(get_min(N))
import sys
N = int(sys.stdin.readline())
