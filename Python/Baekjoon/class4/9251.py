# import sys
# input = sys.stdin.readline
# a = input().rstrip()
# b = input().rstrip()
# if len(a) > len(b):
#     a_reverse = a[::-1]
#     alist = [0 for _ in range(len(a))]
#     for i in b:
#         for j, v in enumerate(a_reverse):
#             if v == i:
#                 real_index = len(a) - 1 - j
#                 if real_index == 0:
#                     alist[0] = 1
#                 else:
#                     alist[real_index] = max(alist[real_index], max(alist[:real_index]) + 1)
#     print(max(alist))
# else:
#     b_reverse = b[::-1]
#     blist = [0 for _ in range(len(b))]
#     for i in a:
#         for j, v in enumerate(b_reverse):
#             if v == i:
#                 real_index = len(b) - 1 - j
#                 if real_index == 0:
#                     blist[0] = 1
#                 else:
#                     blist[real_index] = max(blist[real_index], max(blist[:real_index]) + 1)
#     print(max(blist))