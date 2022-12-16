import sys
K, N = map(int, sys.stdin.readline().split())
al = [int(sys.stdin.readline()) for _ in range(K)]
a0 = 1
a2 = sum(al) // N
while True:
    a1 = (a0 + a2) // 2
    count = 0
    for a in al:
        q = a // a1
        count += q
    if count >= N:
        if a2 - a0 < 2:
            a1 += 1
            count = 0
            for a in al:
                q = a // a1
                count += q
            if count >= N:
                print(a1)
            else:
                print(a1 - 1)
            break
        else:
            a0 = a1
    else:
        if a2 - a0 < 2:
            print(1)
            break
        a2 = a1
