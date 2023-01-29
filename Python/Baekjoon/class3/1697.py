import sys
sys.setrecursionlimit(10 ** 8)
import time

N, K = map(int, sys.stdin.readline().split())
array = [1000000] * (K + 1)
def myfunc(n, count):
    if n < 0 or n > 100000:
        return
    if K == n:
        if array[K] > count:
            array[K] = count
        else:
            return
    elif K < n:
        if array[K] > count + n - K:
            array[K] = count + n - K
        else:
            return
    else:
        if (n - 1) > 0 and (n - 1) < 100000:
            myfunc(n - 1, count + 1)
        if (n + 1) > 0 and (n + 1) < 100000:
            myfunc(n + 1, count + 1)
        if n * 2 > 0 and n * 2 < 100000:
            myfunc(n * 2, count + 1)
start = time.time()
myfunc(N, 0)
print(array[K])
end = time.time()
print(f"{end-start:.4f}")
# if array[K] >= 0:
#     if array[K] <= count:
#         return
# if array[n] >= 0:
#     if array[n] <= count:
#         return
# array[n] = count
# if n == K:
#     for i in range(n, 100001):
#         array[i] = count + i
#     return
# if K < n:
#     if array[K] >= 0:
#         if array[K] > count + n - K:
#             for i in range(K, 100001):
#                 array[i] = count + n - K + i
#             return
#     else:
#         for i in range(K, 100001):
#             array[i] = count + n - K + i
#         return
# else:
#     if array[n - 1] < 0 or array[n - 1] > count + 1:
#         myfunc(n - 1, count + 1)
#     if array[n + 1] < 0 or array[n + 1] > count + 1:
#         myfunc(n + 1, count + 1)
#     if array[n + 1] < 0 or array[n + 1] > count + 1:
#         myfunc(n * 2, count + 1)