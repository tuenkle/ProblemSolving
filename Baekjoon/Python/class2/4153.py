import sys
while True:
    mi = list(map(int, sys.stdin.readline().split()))
    if mi[0] == 0 and mi[1] == 0 and mi[2] == 0:
        break
    max_i = max(mi)
    sum = 0
    for i in mi:
        if i != max_i:
            sum += i ** 2
    if max_i ** 2 == sum:
        print("right")
    else:
        print("wrong")

