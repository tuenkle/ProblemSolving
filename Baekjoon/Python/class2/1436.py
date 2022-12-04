# import sys
# N = int(sys.stdin.readline())
# 666 1 * 1 + 1 * 0 -> 1
# 1666 2666 3666 4666 5666 -> 2
# 6660 6661 6662 6663 6664 6665 6666 6667 6668 6669
# 7666 8666 9666  1 * 10 + 1 * 9
# 10666 11666 1 * 100 + 2 * 90 -> 3
# 100666 1 * 1000 + 3 * 900
# def get_number_666(i, N):
#
# if N == 1:
#     print("666")
# N -= 1
# for i in range(1, 4):
#     index = (10 ** i) + (10 ** (i - 1)) * 9
#     if N > index:
#         N -= index
#         continue
#     else:
#         get_number_666(i, N)