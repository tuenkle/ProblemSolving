import sys
sys.setrecursionlimit(10**7)
n, r, c = map(int, sys.stdin.readline().split())
def get_answer(length, r, c, start):
    if length == 1:
        print(start + (r - 1) * 2 + c - 1)
        return
    if r <= length // 2:
        if c <= length // 2:
            get_answer(length // 2, r, c, start)
        else:
            get_answer(length // 2, r, c - length // 2, start + (length // 2) ** 2)
    else:
        if c <= length // 2:
            get_answer(length // 2, r - length // 2, c, start + (length // 2) ** 2 * 2)
        else:
            get_answer(length // 2, r - length // 2, c - length // 2, start + (length // 2) ** 2 * 3)
get_answer(2 ** n, r + 1, c + 1, 0)