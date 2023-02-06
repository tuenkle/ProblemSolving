import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    erased_set = set()
    for i in range(k):
        command, arg = input().split()
        arg = int(arg)
        if command == "I":
            heapq.heappush(min_heap, (arg, i))
            heapq.heappush(max_heap, (-arg, i))
        else:
            if arg == 1:
                while True:
                    if not max_heap:
                        break
                    uniqueID = heapq.heappop(max_heap)[1]
                    if not uniqueID in erased_set:
                        erased_set.add(uniqueID)
                        break
            else:
                while True:
                    if not min_heap:
                        break
                    uniqueID = heapq.heappop(min_heap)[1]
                    if not uniqueID in erased_set:
                        erased_set.add(uniqueID)
                        break
    is_empty = False
    while True:
        if not max_heap:
            is_empty = True
            break
        max_temp = heapq.heappop(max_heap)
        if not max_temp[1] in erased_set:
            print(-max_temp[0], end=" ")
            break
    while True:
        if not min_heap:
            is_empty = True
            break
        min_temp = heapq.heappop(min_heap)
        if not min_temp[1] in erased_set:
            print(min_temp[0])
            break
    if is_empty:
        print("EMPTY")